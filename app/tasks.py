from celery import shared_task
from models import Test

@shared_task
def add_one():
	t = Test.objects.get(text="Count")
	t.number += 1
	t.save()
