from app.models.task import Task
from app import db

class TaskService:
    def create_task(self, title, description=None):
        task = Task(title=title, description=description)
        db.session.add(task)
        db.session.commit()
        return task.serialize()

    def get_all_tasks(self):
        tasks = Task.query.all()
        return [task.serialize() for task in tasks]

    def get_task(self, id):
        task = Task.query.filter_by(id=id).first()
        if task:
            return task.serialize()
        return None


    def update_task(self, id, data):
        task = Task.query.filter_by(id=id).first()
        if task:
            if 'title' in data:
                task.title = data['title']
            if 'description' in data:
                task.description = data['description']
            db.session.commit()
            return task.serialize()  # Serialize the updated task before returning
        return None

    def delete_task(self, id):
        task = Task.query.filter_by(id=id).first()
        if task:
            db.session.delete(task)
            db.session.commit()
            return True
        return False
