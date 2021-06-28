from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import TodoItem
import logging

# Get an instance of a logger
logger = logging.getLogger(__name__)


# Create your views here.

def todoView(request):
    # return HttpResponse('Hello World!')
    logger.debug('Serving todoView')
    items = TodoItem.objects.all()
    logger.info('Rendering the todo.html')
    return render(request, 'todo.html', 
        { 'allItems': items })

def addTodoItem(request):
    # return HttpResponse('Hello World!')
    logger.debug('Serving on addTodoItem')
    content = TodoItem(content = request.POST['content'])
    content.save()
    logger.info('Saved new todoItem: '+content.content)
    return HttpResponseRedirect('/todo/')

def delTodoItem(request, todo_id):
    # return HttpResponse('Hello World!')
    logger.debug('Serving on delTodoItem')
    itemToDel = TodoItem.objects.get(id=todo_id)
    logger.info('Delete todoItem: '+itemToDel.content)
    itemToDel.delete()
    return HttpResponseRedirect('/todo/')