from flask import jsonify, request
from app.services.task_service import TaskService
import logging

class TaskController:
    def __init__(self, task_service: TaskService):
        self.task_service = task_service

    def create_task(self):
        try:
            data = request.json
            if not data or 'title' not in data:
                return jsonify({'error': 'Title is required'}), 400

            task = self.task_service.create_task(data.get('title'), data.get('description'))
            return jsonify(task), 201
        except Exception as e:
            logging.error(f"Error creating task: {e}")
            return jsonify({'error': 'Internal Server Error'}), 500

    def get_all_tasks(self):
        try:
            tasks = self.task_service.get_all_tasks()
            return jsonify(tasks)
        except Exception as e:
            logging.error(f"Error getting all tasks: {e}")
            return jsonify({'error': 'Internal Server Error'}), 500

    def get_task(self, id):
        try:
            task = self.task_service.get_task(id)
            if not task:
                return jsonify({'error': 'Task not found'}), 404
            return jsonify(task)
        except Exception as e:
            logging.error(f"Error getting task {id}: {e}")
            return jsonify({'error': 'Internal Server Error'}), 500

    def update_task(self, id):
        try:
            data = request.json
            task = self.task_service.update_task(id, data)
            if not task:
                return jsonify({'error': 'Task not found'}), 404
            return jsonify(task)
        except Exception as e:
            logging.error(f"Error updating task {id}: {e}")
            return jsonify({'error': 'Internal Server Error'}), 500

    def delete_task(self, id):
        try:
            success = self.task_service.delete_task(id)
            if not success:
                return jsonify({'error': 'Task not found'}), 404
            return jsonify({'message': 'Task deleted successfully'})
        except Exception as e:
            logging.error(f"Error deleting task {id}: {e}")
            return jsonify({'error': 'Internal Server Error'}), 500
