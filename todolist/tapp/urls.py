from django.urls import path
from .views import (
    create_task,
    read_task,
    read_all_task,
    update_task,
    delete_task,
)

app_name = 'tasks'

urlpatterns = [
    path('task/create/', create_task),
    path('task/read/<int:pk>/', read_task),
    path('task/read/', read_all_task),
    path('task/update/<int:pk>/', update_task),
    path('task/delete/<int:pk>/', delete_task),
]