from django.urls import path
from tapp.views import TaskListView, TaskDetailView

app_name = 'tasks'

urlpatterns = [
    path('tasks/', TaskListView.as_view(), name='task-list'),
    path('tasks/<int:pk>/', TaskDetailView.as_view(), name='task-detail'),
]