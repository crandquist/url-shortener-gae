# URL Shortener

A URL shortening service built with Flask and deployed on Google App Engine.

## 🚀 Live Demo

Visit the live application: Coming Soon

## ✨ Features

- Create shortened URLs for any web address
- Track detailed visit statistics including user agents and timestamps
- View a dashboard of all shortened URLs
- Copy shortened URLs to clipboard with one click
- Responsive design works on mobile and desktop

## 🛠️ Technology Stack

- **Backend**: Python 3.9, Flask
- **Database**: Google Cloud Datastore
- **Frontend**: HTML5, CSS3, Bootstrap 5
- **Hosting**: Google App Engine (Standard Environment)

## 📋 Prerequisites

- Python 3.9 or higher
- Google Cloud SDK
- Google Cloud Platform account

## 🔧 Local Development

1. Clone this repository

   ```bash
   git clone https://github.com/crandquist/url-shortener-gae.git
   cd url-shortener-gae
   ```

2. Install dependencies

    ```bash
    pip install -r requirements.txt
    ```

3. Set up authentication

    ```bash
    gcloud auth application-default login
    ```

4. Run locally

    ```bash
    python main.py
    ```

5. Access at `http://localhost:8080`

## 🚀 Deployment

See [Deployment.md](docs/DEPLOYMENT.md) for detailed deployment instructions

## 📁 Project Structure

```bash
url-shortener-gae/
├── main.py               # Main Flask application
├── templates/            # HTML templates
│   ├── base.html         # Base template with common elements
│   ├── index.html        # Homepage with URL input form
│   ├── stats.html        # Statistics page
│   └── all_urls.html     # List of all URLs
├── static/               # Static files
│   └── css/              # CSS files
│       └── style.css     # Custom styles
├── app.yaml              # GAE configuration
└── requirements.txt      # Python dependencies
```

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👤 Author

Cat Randquist - [github.com/crandquist](https://github.com/crandquist)
