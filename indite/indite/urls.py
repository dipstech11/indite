from django.contrib import admin
from django.urls import path

from hello.views import myView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('sayHello/', myView)
]
