from flask import Blueprint, request, jsonify
from flasgger.utils import swag_from
from app.services.task_service import TaskService

task_bp = Blueprint('task_bp', __name__)
task_service = TaskService()

@task_bp.route('/tasks', methods=['POST'])
@swag_from({
    'tags': ['Tasks'],
    'summary': 'Create a new task',
    'description': 'Create a task: Method POST. Request parameters: JSON object with fields title (string) and description (string, optional).',
    'parameters': [
        {
            'name': 'body',
            'in': 'body',
            'required': True,
            'schema': {
                'type': 'object',
                'properties': {
                    'title': {
                        'type': 'string',
                        'description': 'The title of the task'
                    },
                    'description': {
                        'type': 'string',
                        'description': 'The description of the task'
                    }
                },
                'required': ['title']
            }
        }
    ],
    'responses': {
        201: {
            'description': 'Task created',
            'examples': {
                'application/json': {
                    'id': 1,
                    'title': 'New Task',
                    'description': 'This is a new task',
                    'created_at': '2024-05-23T15:00:00Z',
                    'updated_at': '2024-05-23T15:00:00Z'
                }
            }
        },
        400: {
            'description': 'Invalid input'
        }
    }
})
def create_task():
    data = request.get_json()
    result = task_service.create_task(data.get('title'), data.get('description'))
    return jsonify(result)

@task_bp.route('/tasks', methods=['GET'])
@swag_from({
    'tags': ['Tasks'],
    'summary': 'Get all tasks',
    'description': 'Get a list of tasks: Method GET. Response: JSON list of tasks.',
    'responses': {
        200: {
            'description': 'List of tasks',
            'examples': {
                'application/json': [
                    {
                        'id': 1,
                        'title': 'Sample Task',
                        'description': 'This is a sample task',
                        'created_at': '2024-05-23T15:00:00Z',
                        'updated_at': '2024-05-23T15:00:00Z'
                    }
                ]
            }
        }
    }
})
def get_all_tasks():
    result = task_service.get_all_tasks()
    return jsonify(result)

@task_bp.route('/tasks/<int:id>', methods=['GET'])
@swag_from({
    'tags': ['Tasks'],
    'summary': 'Get task by ID',
    'description': 'Get task information: Method GET. Response: JSON object with task information.',
    'parameters': [
        {
            'name': 'id',
            'in': 'path',
            'type': 'integer',
            'required': True,
            'description': 'ID of the task'
        }
    ],
    'responses': {
        200: {
            'description': 'Task details',
            'examples': {
                'application/json': {
                    'id': 1,
                    'title': 'Sample Task',
                    'description': 'This is a sample task',
                    'created_at': '2024-05-23T15:00:00Z',
                    'updated_at': '2024-05-23T15:00:00Z'
                }
            }
        },
        404: {
            'description': 'Task not found'
        }
    }
})
def get_task(id):
    result = task_service.get_task(id)
    return jsonify(result)

@task_bp.route('/tasks/<int:id>', methods=['PUT'])
@swag_from({
    'tags': ['Tasks'],
    'summary': 'Update task',
    'description': 'Update a task: Method PUT. Request parameters: JSON object with fields title and description.',
    'parameters': [
        {
            'name': 'id',
            'in': 'path',
            'type': 'integer',
            'required': True,
            'description': 'ID of the task to update'
        },
        {
            'name': 'body',
            'in': 'body',
            'required': True,
            'schema': {
                'type': 'object',
                'properties': {
                    'title': {
                        'type': 'string',
                        'description': 'The updated title of the task'
                    },
                    'description': {
                        'type': 'string',
                        'description': 'The updated description of the task'
                    }
                }
            }
        }
    ],
    'responses': {
        200: {
            'description': 'Task updated',
            'examples': {
                'application/json': {
                    'id': 1,
                    'title': 'Updated Task',
                    'description': 'This is an updated task',
                    'created_at': '2024-05-23T15:00:00Z',
                    'updated_at': '2024-05-23T15:10:00Z'
                }
            }
        },
        404: {
            'description': 'Task not found'
        }
    }
})
def update_task(id):
    data = request.get_json()
    result = task_service.update_task(id, data)
    return jsonify(result)

@task_bp.route('/tasks/<int:id>', methods=['DELETE'])
@swag_from({
    'tags': ['Tasks'],
    'summary': 'Delete task',
    'description': 'Delete a task: Method DELETE. Response: Success message.',
    'parameters': [
        {
            'name': 'id',
            'in': 'path',
            'type': 'integer',
            'required': True,
            'description': 'ID of the task to delete'
        }
    ],
    'responses': {
        200: {
            'description': 'Task deleted successfully',
            'examples': {
                'application/json': {
                    'message': 'Task deleted successfully'
                }
            }
        },
        404: {
            'description': 'Task not found'
        }
    }
})
def delete_task(id):
    result = task_service.delete_task(id)
    return jsonify(result)
