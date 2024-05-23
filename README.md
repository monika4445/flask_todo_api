**Flask Todo API**

This repository contains a Flask-based Todo API, allowing users to manage tasks effectively through RESTful endpoints. Below are the steps to clone the repository, install dependencies, run the application, and access the Swagger API documentation.

**How to Use:**

1. **Clone the Repository:**
   Clone the repository using the following command:
   ```
   git clone https://github.com/monika4445/flask_todo_api.git
   ```

2. **Install Dependencies:**
   Navigate to the root directory of the project and install the required dependencies from the `requirements.txt` file:
   ```
   cd flask_todo_api
   pip install -r requirements.txt
   ```

3. **Run the Application:**
   Run the Flask application using the following command:
   ```
   flask run
   ```

4. **Access Swagger API Documentation:**
   Once the application is running, you can access the Swagger API documentation by visiting the following link in your web browser:
   ```
   http://127.0.0.1:5000/apidocs/
   ```

5. **Run Tests:**
   To run the tests for the Todo API, execute the following command from the root directory:
   ```
   python -m unittest tests.test_task_routes
   ```
**Database Setup:**

This Todo API is designed to work with MySQL database. To set up the database and perform migrations, follow these steps:

1. **Database Configuration:**
   Ensure that you have MySQL installed and running on your system. Update the database connection settings in the `config/config.py` file located in the root directory to match your MySQL configuration.

2. **Database Migration:**
   Use Flask-Migrate to manage database migrations. To create an initial migration, execute the following command in the terminal:
   ```
   flask db init
   ```

3. **Perform Migrations:**
   Whenever there are changes to the database models, create a migration script using the following command:
   ```
   flask db migrate -m "your_migration_message"
   ```

4. **Apply Migrations:**
   Apply the migration to the database by running:
   ```
   flask db upgrade
   ```

**Description:**

This Todo API provides the following functionalities:

- **Create Task:** Allows users to create a new task by providing a title and optional description.
- **Get All Tasks:** Retrieves all tasks stored in the database.
- **Get Task:** Retrieves a specific task by its ID.
- **Update Task:** Updates an existing task's title and/or description.
- **Delete Task:** Deletes a task by its ID.

The API documentation is generated using Swagger, providing an interactive interface to explore and test the endpoints.
