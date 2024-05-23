import unittest
from app import create_app, db
from app.models.task import Task

class TestTaskRoutes(unittest.TestCase):
    def setUp(self):
        # Create a test app
        self.app = create_app()
        self.client = self.app.test_client()

        # Create a test database
        with self.app.app_context():
            db.create_all()

    def tearDown(self):
        with self.app.app_context():
            db.session.remove()
            db.drop_all()

    def test_create_task_route(self):
        # Test creating a task
        with self.app.app_context():
            response = self.client.post('/tasks', json={'title': 'Test Task'})
            task_id = response.json.get('id')
            task = db.session.get(Task, task_id)
            self.assertIsNotNone(task)
            self.assertEqual(task.title, 'Test Task')

    def test_get_all_tasks_route(self):
        # Test getting all tasks
        response = self.client.get('/tasks')
        self.assertIsInstance(response.json, list)

    def test_get_task_route(self):
        # Create a task for testing
        with self.app.app_context():
            task = Task(title='Test Task')
            db.session.add(task)
            db.session.commit()

            # Test getting a specific task
            response = self.client.get(f'/tasks/{task.id}')
            task = db.session.get(Task, task.id)
            self.assertEqual(response.json['title'], 'Test Task')

    def test_update_task_route(self):
        # Create a task for testing
        with self.app.app_context():
            task = Task(title='Test Task')
            db.session.add(task)
            db.session.commit()

            # Test updating a task
            response = self.client.put(f'/tasks/{task.id}', json={'title': 'Updated Task'})
            updated_task = db.session.get(Task, task.id)
            self.assertEqual(updated_task.title, 'Updated Task')

    def test_delete_task_route(self):
        # Create a task for testing
        with self.app.app_context():
            task = Task(title='Test Task')
            db.session.add(task)
            db.session.commit()

            # Test deleting a task
            response = self.client.delete(f'/tasks/{task.id}')
            deleted_task = db.session.get(Task, task.id)
            self.assertIsNone(deleted_task)

if __name__ == '__main__':
    unittest.main()
