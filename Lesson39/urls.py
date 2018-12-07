"""Lesson39 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from todolist.views import tasks_view, create_task_view, edit_task_view, delete_task_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', tasks_view, name='tasks_view'),
    path('task/create', create_task_view, name='create_task'),
    path('task/edit/<int:task_id>', edit_task_view, name='edit_task'),
    path('task/delete/<int:task_id>', delete_task_view, name='delete_task'),
    path('task/delete/', delete_task_view, name='delete_task'),
]
