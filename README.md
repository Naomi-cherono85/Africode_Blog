# Flask Application

This repository contains a Flask application with user registration, login, account update, and password reset functionalities. The application uses Flask-WTF for form handling and validation.

## Features

- **User Registration**: Allows users to create an account.
- **User Login**: Users can log in with their email and password.
- **Account Update**: Users can update their username, email, and profile picture.
- **Post Creation**: Users can create posts with a title and content.
- **Password Reset**: Users can request a password reset and reset their password.

## Setup

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/yourusername/your-repository.git

2.**Navigate to the Project Directory**:
^^^bash
cd your-repository

3. **Install the Dependencies**:
bash
pip install -r requirements.txt

5. **Set Up the Database**:
bash
flask db init
flask db migrate
flask db upgrade

6. **Run the Application**:

bash

flask run

