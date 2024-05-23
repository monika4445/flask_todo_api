from flasgger import Swagger

def configure_swagger(app):
    template = {
        "swagger": "2.0",
        "info": {
            "title": "ToDo List API ",
            "description": (
                "This API allows users to manage their to-do lists. Users can create, retrieve, "
                "update, and delete tasks. Each task consists of a title and an optional description. "
                "The API provides endpoints for the following operations:\n\n"
                "1. Create a task (POST /tasks)\n"
                "2. Get all tasks (GET /tasks)\n"
                "3. Get a task by ID (GET /tasks/{id})\n"
                "4. Update a task by ID (PUT /tasks/{id})\n"
                "5. Delete a task by ID (DELETE /tasks/{id})\n\n"
                "All responses are in JSON format and include timestamps for when tasks were created "
                "and last updated."
            ),            
            "version": "1.0.0"
        },
        "host": "localhost:5000", 
        "basePath": "/",
        "schemes": [
            "http",
            "https"
        ],
    }
    Swagger(app, template=template)
