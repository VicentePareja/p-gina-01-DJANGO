from django.shortcuts import render
from django.http import HttpResponse
from .models import ToDoList, Item

# Create your views here.

def index(response, name):
	ls = ToDoList.objects.get(name=name)
	item = ls.item_set.get(id=1)
	return HttpResponse("<h1 style= \"color: red;\">%s</h1><h1>Rosito es la más linda <br> SITIO 3</h1><br><br><br><br><br><br><br><p>%s</p>" % (ls.name, str(item.text)))
