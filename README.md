**Library Management System Clone with Django REST Framework.**

This project is a library management system API built using Django REST Framework (DRF). It allows users to manage libraries, books, authors, and loan processes.

**Technologies Used**

1. Python 3.11
2. Django
3. Django REST Framework (DRF)

**Requirements**

1. Python 3.11 installed
2. Django installed
3. Installation

**Installation**

1. Clone this repository: git clone https://github.com/Abdul12majid/LMS_api.git
2. Navigate to the project directory: cd LMS_api
3. Create a virtual environment (recommended): pythom -m venv py_env
4. Activate virtual environment: source py_env/scripts/activate
5. Install project dependencies: pip install -r requirements.txt
6. Migrate the database (assuming using a database like PostgreSQL): python manage.py migrate
7. Create a superuser account (optional, for initial admin access): winpty python manage.py createsuperuser

   
**Usage**

Start the development server: python manage.py runserver
Access the API documentation at - http://127.0.0.1:8000/api/docs/


**Features**

1. User registration and login
2. Library Management - Create, read, update, and delete libraries.
3. Book Management - Create, read, update, and delete books with details like title, author, ISBN, and publication date.
4. Author Management - Create, read, update, and delete authors.
5. Loan Management, 3 conditions used.
6. Manage book loans for users, including borrowing, returning, and overdue handling..

**Contact Me**

For any questions or feedback, feel free to reach out to Majid at yisaabdulmajid@gmail.com or open an issue on the GitHub repository.
