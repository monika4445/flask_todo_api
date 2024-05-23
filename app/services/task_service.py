from app.models.task import Task
from app import db

class TaskService:
    def create_task(self, title, description=None):
        # Perform validation
        if not title:
            return {'message': 'Title is required'}

        # Create and save the task
        task = Task(title=title, description=description)
        db.session.add(task)
        db.session.commit()
        return task.serialize()

    def get_all_tasks(self):
        tasks = db.session.query(Task).all()
        return [task.serialize() for task in tasks]

    def get_task(self, id):
        # Perform validation
        if not id:
            return {'message': 'Task ID is required'}

        task = db.session.get(Task, id)
        if task:
            return task.serialize()
        return {'message': 'Task not found'}


    def update_task(self, id, data):
        # Perform validation
        if not id:
            return {'message': 'Task ID is required'}

        task = db.session.get(Task, id)
        if not task:
            return {'message': 'Task not found'}

        # Update task fields if provided
        if 'title' in data:
            task.title = data['title']
        if 'description' in data:
            task.description = data['description']

        db.session.commit()
        return task.serialize()

    def delete_task(self, id):
        # Perform validation
        if not id:
            return {'message': 'Task ID is required'}

        task = db.session.get(Task, id)
        if task:
            db.session.delete(task)
            db.session.commit()
            return {'message': 'Task deleted successfully'}
        return {'message': 'Task not found'}
