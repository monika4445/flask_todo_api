import unittest
import json
from app import create_app, db
from app.models.task import Task

class TestTaskRoutes(unittest.TestCase):
    def setUp(self):
        self.app = create_app()
        self.client = self.app.test_client()
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    def test_create_task(self):
        # Test creating a new task
        task_data = {'title': 'Task 1', 'description': 'Description for Task 1'}
        response = self.client.post('/tasks/', json=task_data)
        self.assertEqual(response.status_code, 201)
        data = json.loads(response.data)
        self.assertIn('id', data)
        self.assertEqual(data['title'], 'Task 1')
        self.assertEqual(data['description'], 'Description for Task 1')

    def test_get_all_tasks(self):
        # Test getting all tasks
        task1 = Task(title='Task 1', description='Description for Task 1')
        task2 = Task(title='Task 2', description='Description for Task 2')
        db.session.add_all([task1, task2])
        db.session.commit()

        response = self.client.get('/tasks/')
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data)
        self.assertEqual(len(data), 2)
        self.assertEqual(data[0]['title'], 'Task 1')
        self.assertEqual(data[1]['title'], 'Task 2')

    def test_get_task_by_id(self):
        # Test getting a task by ID
        task = Task(title='Task 1', description='Description for Task 1')
        db.session.add(task)
        db.session.commit()

        response = self.client.get(f'/tasks/{task.id}')
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data)
        self.assertEqual(data['title'], 'Task 1')
        self.assertEqual(data['description'], 'Description for Task 1')

    def test_update_task(self):
        # Test updating a task
        task = Task(title='Task 1', description='Description for Task 1')
        db.session.add(task)
        db.session.commit()

        update_data = {'title': 'Updated Task 1', 'description': 'Updated Description'}
        response = self.client.put(f'/tasks/{task.id}', json=update_data)
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data)
        self.assertEqual(data['title'], 'Updated Task 1')
        self.assertEqual(data['description'], 'Updated Description')

    def test_delete_task(self):
        # Test deleting a task
        task = Task(title='Task 1', description='Description for Task 1')
        db.session.add(task)
        db.session.commit()

        response = self.client.delete(f'/tasks/{task.id}')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(Task.query.count(), 0)

if __name__ == '__main__':
    unittest.main()
