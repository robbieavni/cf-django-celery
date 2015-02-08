from django.shortcuts import render
from django.http import HttpResponse
from app.models import Test

# Create your views here.
def index(request):
	t = Test.objects.get(text='Count')
	return HttpResponse(t.number)
