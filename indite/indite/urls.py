from django.contrib import admin
from django.urls import path

from hello.views import myView
from todo.views import todoView, addTodo, deleteTodo

urlpatterns = [
    path('admin/', admin.site.urls),
    path('sayHello/', myView),
    path('todo/', todoView),
    path('addTodo/', addTodo),
    path('deleteTodo/<int:todo_id>/', deleteTodo)
]
