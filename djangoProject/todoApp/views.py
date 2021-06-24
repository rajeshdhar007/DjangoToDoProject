from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import TodoItem

# Create your views here.

def todoView(request):
    # return HttpResponse('Hello World!')
    items = TodoItem.objects.all()
    return render(request, 'todo.html', 
        { 'allItems': items })

def addTodoItem(request):
    # return HttpResponse('Hello World!')
    content = TodoItem(content = request.POST['content'])
    content.save()
    return HttpResponseRedirect('/todo/')

def delTodoItem(request, todo_id):
    # return HttpResponse('Hello World!')
    itemToDel = TodoItem.objects.get(id=todo_id)
    itemToDel.delete()
    return HttpResponseRedirect('/todo/')