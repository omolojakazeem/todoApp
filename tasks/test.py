from django.test import TestCase
from .models import Task


class TaskTestCase(TestCase):
    def testPost(self):
        task = Task(title="My Title")
        self.assertEqual(task.title, "My Title")
        