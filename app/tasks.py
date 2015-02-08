from celery import Celery
from models import Test

app = Celery('tasks', broker='amqp://guest@localhost')

@app.task
def add_one():
	t = Test.objects.get(text="Count")
	t.number += 1
	t.save()
