from django.contrib import admin
from django.urls import path
from . import views
from .views import TaskListView, TaskCreateView, TaskEditView, UserTaskView

urlpatterns = [
    path('', TaskListView.as_view(), name='todo-home'),
    path('about/', views.about, name='todo-about'),
    path('task/new/', TaskCreateView.as_view(), name='task-create'),
    path('task/<int:pk>/edit/', TaskEditView.as_view(), name='task-edit'),
    path('task/<str:username>/', UserTaskView.as_view(), name='user-task'),
]