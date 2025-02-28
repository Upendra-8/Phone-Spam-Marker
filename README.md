# Spam Detection API
## Overview
The Spam Detection API is a Django-based application that allows users to register, log in, search for contacts, mark phone numbers as spam, and view spam statistics. The system enables efficient phone number tracking and spam reporting using a relational database.

## Features
  - ## Authentication & User Management
    - User registration with phone number.
    - Secure login and logout.
    - Profile management to update user details.
  - ## Contact & Spam Management
    - Add and retrieve contact details.
    - Mark phone numbers as spam.
    - View spam statistics for reported numbers.
  - ## Search & Lookup
    - Search contacts by name or phone number.
    - Retrieve spam reports on specific phone numbers.

## Installation
## Prerequisites
Ensure you have the following installed:
  - Python 3.8+
  - Django 5.x or higher
  - Django REST Framework (DRF)

## Setup
1. Clone the repository:
git clone https://github.com/yourusername/Phone-Spam-Marker.git
Navigate to the project directory:
cd spam-detection-api

2. Create and activate a virtual environment:
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

## Install dependencies:
pip install -r requirements.txt

## Apply database migrations:
  - python manage.py makemigrations
  - python manage.py migrate

## Running the Application
1. Start the development server:
python manage.py runserver
2. Access the application at:
http://127.0.0.1:8000/

## Usage
You can use Postman or any API testing tool to interact with the endpoints.

## Contributing
We welcome contributions to improve the project. To contribute:
1. Fork the repository.
2. Create a new branch:
git checkout -b feature-branch
3. Make your changes.
4. Commit your changes:
git commit -am 'Add new feature'
5. Push your branch:
git push origin feature-branch
6. Open a Pull Request.

## Acknowledgments
**Django REST Framework:** Used for building the API endpoints.

