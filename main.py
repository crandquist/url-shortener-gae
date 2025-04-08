import datetime
import hashlib
import os
from flask import Flask, render_template, request, redirect, abort, url_for
from google.cloud import datastore

app = Flask(__name__)
datastore_client = datastore.Client()

def generate_short_url(long_url):
    """Generate a short URL code based on the hash of the original URL"""
    hash_object = hashlib.sha256(long_url.encode())
    hex_dig = hash_object.hexdigest()
    return hex_dig[:7]  # First 7 characters of hash

def store_url(long_url, short_code):
    """Store the URL mapping in Datastore"""
    key = datastore_client.key('URL', short_code)
    entity = datastore.Entity(key=key)
    entity.update({
        'long_url': long_url,
        'created': datetime.datetime.now(),
        'access_count': 0
    })
    datastore_client.put(entity)
    return short_code

def record_visit(short_code, request):
    """Record information about a visit to a shortened URL"""
    key = datastore_client.key('Visit')
    entity = datastore.Entity(key=key)
    entity.update({
        'short_code': short_code,
        'timestamp': datetime.datetime.now(),
        'user_agent': request.user_agent.string,
        'ip': request.remote_addr
    })
    datastore_client.put(entity)
    
    # Update the access count
    url_key = datastore_client.key('URL', short_code)
    url = datastore_client.get(url_key)
    if url:
        url['access_count'] += 1
        datastore_client.put(url)

def get_url(short_code):
    """Retrieve the original URL from a short code"""
    key = datastore_client.key('URL', short_code)
    return datastore_client.get(key)

def get_visits(short_code, limit=10):
    """Get visit records for a specific short URL"""
    query = datastore_client.query(kind='Visit')
    query.add_filter('short_code', '=', short_code)
    query.order = ['-timestamp']
    return list(query.fetch(limit=limit))

def get_all_urls():
    """Get all shortened URLs"""
    query = datastore_client.query(kind='URL')
    query.order = ['-created']
    return list(query.fetch())

@app.route('/')
def home():
    # Get the 5 most recently created URLs
    recent_urls = get_all_urls()[:5]
    return render_template('index.html', recent_urls=recent_urls)

@app.route('/shorten', methods=['POST'])
def shorten():
    long_url = request.form.get('url')
    if not long_url:
        return redirect('/')
    
    # Add protocol if missing
    if not long_url.startswith(('http://', 'https://')):
        long_url = 'https://' + long_url
    
    short_code = generate_short_url(long_url)
    store_url(long_url, short_code)
    
    host = request.host_url
    short_url = f"{host}{short_code}"
    
    return render_template('index.html', 
                          original_url=long_url, 
                          short_url=short_url,
                          recent_urls=get_all_urls()[:5])

@app.route('/<short_code>')
def redirect_to_url(short_code):
    url_mapping = get_url(short_code)
    if url_mapping:
        record_visit(short_code, request)
        return redirect(url_mapping['long_url'])
    else:
        abort(404)

@app.route('/all')
def all_urls():
    urls = get_all_urls()
    return render_template('all_urls.html', urls=urls)

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)