from flask import Blueprint
from app.controllers.task_controller import TaskController
from app.services.task_service import TaskService

task_bp = Blueprint('task_bp', __name__)

task_service = TaskService()
task_controller = TaskController(task_service)

task_bp.add_url_rule('/tasks', view_func=task_controller.create_task, methods=['POST'])
task_bp.add_url_rule('/tasks', view_func=task_controller.get_all_tasks, methods=['GET'])
task_bp.add_url_rule('/tasks/<int:id>', view_func=task_controller.get_task, methods=['GET'])
task_bp.add_url_rule('/tasks/<int:id>', view_func=task_controller.update_task, methods=['PUT'])
task_bp.add_url_rule('/tasks/<int:id>', view_func=task_controller.delete_task, methods=['DELETE'])
