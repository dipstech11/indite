from django.http import HttpResponseRedirect
from django.shortcuts import render
from .models import TodoItem


def todoView(request):
    todo_items = TodoItem.objects.all()
    return render(request, 'todo.html', {'todo_items': todo_items})


def addTodo(request):
    # create a new TodoItem object and save
    new_content = request.POST['content']
    new_todo_item = TodoItem(content=new_content)
    new_todo_item.save()

    return HttpResponseRedirect('/todo/')


def deleteTodo(request, todo_id):
    # delete the TodoItem based on the id

    item_to_delete = TodoItem.objects.get(id=todo_id)
    item_to_delete.delete()

    return HttpResponseRedirect('/todo/')








