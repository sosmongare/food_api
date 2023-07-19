# Food API

![Food API](food_api.png)

## Table of Contents

- [Food API](#food-api)
  - [Table of Contents](#table-of-contents)
  - [Introduction](#introduction)
  - [Features](#features)
  - [Technologies Used](#technologies-used)
  - [Setup and Installation](#setup-and-installation)
  - [API Endpoints](#api-endpoints)
  - [Request and Response Format](#request-and-response-format)
  - [API Usage Examples](#api-usage-examples)
  - [License](#license)

## Introduction

Welcome to the Food API! This is a RESTful API built using Django, a powerful web framework for Python, and MySQL as the database backend. The API allows users to manage food items by performing CRUD (Create, Read, Update, Delete) operations on them. Each food item has a name and description.

Whether you are building a food-related application, experimenting with APIs, or learning Django, this project can serve as a solid foundation to get started.

## Features

- Create a new food item with its name and description.
- Retrieve a list of all food items.
- Retrieve details of a specific food item by its ID.
- Update an existing food item's name and/or description.
- Delete a food item by its ID.

## Technologies Used

- Django: A high-level web framework written in Python.
- Django REST framework: A powerful and flexible toolkit for building Web APIs in Django.
- MySQL: A popular relational database management system.
- Python: The programming language used for backend development.
- Git: Version control system for tracking changes in source code.
- Heroku (Optional): Cloud platform for deploying and hosting the API.

## Setup and Installation

To run the Food API locally on your machine, follow these steps:

1. Ensure you have Python, MySQL, and pip installed. If not, refer to the prerequisites in the documentation.

2. Clone this repository to your local machine:

   ```bash
   git clone https://github.com/sosmongare/food_api.git
   cd food-api
   ```

3. Create and activate a virtual environment:

   ```bash
   python -m venv env
   # On Windows:
   . env/Scripts/activate
   # On macOS/Linux:
   source env/bin/activate
   ```

4. Install the required dependencies:

   ```bash
   pip install -r requirements.txt
   ```

5. Set up the MySQL database:

   - Create a MySQL database and update the database settings in `food_api/settings.py`.
  ```
  DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'your_mysql_db_name',
        'USER': 'your_mysql_username',
        'PASSWORD': 'your_mysql_password',
        'HOST': 'your_mysql_host',  # Use 'localhost' if the database is on the same machine
        'PORT': 'your_mysql_port',  # Typically 3306 for MySQL
    } 
}
```

1. Apply database migrations:

   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

2. Run the development server:

   ```bash
   python manage.py runserver
   ```

The API should now be accessible at `http://127.0.0.1:8000/food/`.

## API Endpoints

The following endpoints are available in the Food API:

- `GET /food/`: Get a list of all food items.
- `POST /food/`: Create a new food item.
- `GET /food/<int:pk>/`: Get details of a specific food item by ID.
- `PUT /food/<int:pk>/`: Update an existing food item by ID.
- `DELETE /food/<int:pk>/`: Delete a food item by ID.

## Request and Response Format

The API accepts and returns data in JSON format.

- Request format (POST and PUT):

  ```json
  {
      "name": "Food Name",
      "description": "Description of the food item."
  }
  ```

- Response format (GET and POST):

  ```json
  {
      "id": 1,
      "name": "Food Name",
      "description": "Description of the food item."
  }
  ```

## API Usage Examples

1. Get a list of all food items:

   ```
   GET http://127.0.0.1:8000/food/
   ```

2. Create a new food item:

   ```
   POST http://127.0.0.1:8000/food/
   {
       "name": "Pizza",
       "description": "Delicious pizza with cheese and toppings."
   }
   ```

3. Get details of a specific food item by ID:

   ```
   GET http://127.0.0.1:8000/food/1/
   ```

4. Update an existing food item by ID:

   ```
   PUT http://127.0.0.1:8000/food/1/
   {
       "name": "Pizza Margherita",
       "description": "Classic pizza with mozzarella, tomatoes, and basil."
   }
   ```

5. Delete a food item by ID:

   ```
   DELETE http://127.0.0.1:8000/food/1/
   ```

## License

This project is licensed under the [MIT License](LICENSE).


Happy Coding!!!