from django.urls import path
from . import views
from .views import TaskListView, TaskCreateView, TaskEditView, TaskDeleteView, UserTaskView, \
    task_group_detail, TaskGroupListView, TodoEditView

urlpatterns = [
    path('', TaskListView.as_view(), name='todo-home'),
    path('about/', views.about, name='todo-about'),
    path('task/new/', TaskCreateView.as_view(), name='task-create'),
    path('task/<int:pk>/edit/', TaskEditView.as_view(), name='task-edit'),
    path('task/<int:pk>/delete/', TaskDeleteView.as_view(), name='task-delete'),
    path('task/<str:username>/', UserTaskView.as_view(), name='user-task'),
    path('task/<int:pk>/detail/', task_group_detail, name='task-group-detail'),
    path('task/<int:pk>/view/', TaskGroupListView.as_view(), name='task-group-list-view'),
    path('task/<int:pk1>/edit/<int:pk>/', TodoEditView.as_view(), name='todo-edit'),
]