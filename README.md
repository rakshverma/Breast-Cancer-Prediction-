# Breast Cancer Prediction Web Application

A Django-based web application that uses machine learning to predict breast cancer diagnosis based on medical features.

## Features
- User Authentication
- Real-time Cancer Prediction  
- CSV File Upload Support
- Responsive Design
- Docker Support

## Tech Stack
- Django
- NumPy
- Docker 
- HTML/CSS/JavaScript

## Installation with Docker

1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/cancer-prediction.git
    ```

2. Build Docker image:
    ```bash
    docker build -t cancer-prediction .
    ```

3. Run the container:
    ```bash
    docker run -p 8000:8000 cancer-prediction
    ```

## Installation without Docker

1. Create a virtual environment:
    ```bash
    python -m venv venv
    ```

2. Activate virtual environment:
    ```bash
    # Windows
    venv\Scripts\activate
    
    # Linux/Mac
    source venv/bin/activate
    ```

3. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

4. Run migrations:
    ```bash
    python manage.py migrate
    ```

5. Start development server:
    ```bash
    python manage.py runserver
    ```

## Usage

1. Access the application at `http://localhost:8000`
2. Register/Login to your account
3. Enter medical parameters or upload CSV file
4. Get instant prediction results

## Project Structure
./ ├── myapp/ │ ├── model_params.json │ ├── scaler_params.json │ └── templates/ ├── Dockerfile ├── requirements.txt └── manage.py

