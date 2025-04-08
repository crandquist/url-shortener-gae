# Deployment Guide

This document provides step-by-step instructions for deploying the URL Shortener application to Google App Engine.

## Prerequisites

1. Google Cloud Platform account
2. Google Cloud SDK installed locally
3. Project code cloned to your local machine

## Steps to Deploy

### 1. Set Up Google Cloud

```bash
# Install Google Cloud SDK (if not already installed)
# Visit https://cloud.google.com/sdk/docs/install for instructions

# Login to your Google Cloud account
gcloud auth login

# Create a new project (if not already created)
gcloud projects create [YOUR_PROJECT_ID] --name="URL Shortener"

# Set the project as active
gcloud config set project [YOUR_PROJECT_ID]

# Enable required APIs
gcloud services enable appengine.googleapis.com
gcloud services enable datastore.googleapis.com
```

### 2. Set Up Authentication

```bash
# Set up application default credentials
gcloud auth application-default login
```

### 3. Test Locally

```bash
# Install dependencies
pip install -r requirements.txt

# Run locally
python main.py

# Test at http://localhost:8080
```

### 4. Deploy to Google App Engine

```bash
# From your project directory
gcloud app deploy

# When prompted, select a region closest to you
# Wait for deployment to complete

# Open your deployed application
gcloud app browse
```

Your application will now be available at:

```bash
https://[YOUR_PROJECT_ID].[REGION_ID].appspot.com/
```

### 5. Monitoring and Management

- View logs: `gcloud app logs tail`
- View application status: `gcloud app describe`
- View Datastore entries: Visit Google Cloud Console > Datastore

## Troubleshooting

### Common Issues

1. Authentication Errors: Run `gcloud auth application-default login` again
2. API Not Enabled: Ensure you've enabled the Datastore API
3. Deployment Fails: Check logs with gcloud app logs tail

### Getting Help

If you encounter any issues, check the [Google App Engine documentation](https://cloud.google.com/appengine/docs) or open an issue in the repository.
