# easy-vector
Provides a simple API and Docker implementation for generating your own vector embeddings.

## Overview
This project provides a simple RESTful API for generating vector embeddings using the `fastembed` library. The application is containerized using Docker and served using Gunicorn for production readiness.

## Installation

1. **Clone the repository**:
   ```bash
   git clone <repository-url>
   cd easy-vector
   ```

2. **Set up a virtual environment** (optional but recommended):
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

### Running Locally

1. **Start the Flask application**:
   ```bash
   gunicorn -b 0.0.0.0:3000 app:app
   ```

2. **Test the API**:
   Use a tool like `curl` or Postman to test the `/embed` endpoint. For example:
   ```bash
   curl -X POST http://localhost:3000/embed -H "Content-Type: application/json" -d '{"documents": ["This is a test document.", "Another document."]}'
   ```

### Running with Docker

1. **Build the Docker image**:
   ```bash
   docker build -t easy-vector .
   ```

2. **Run the Docker container**:
   ```bash
   docker run -p 3000:3000 easy-vector
   ```

3. **Access the API**:
   The API will be accessible at `http://localhost:3000/embed`.

## Deployment

The Dockerfile uses Gunicorn (WSGI server) to serve the application in production in a way that can handle high traffic and multiple requests.
