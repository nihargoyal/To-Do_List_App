from rest_framework import viewsets
from .models import Todo
from .serializers import TaskSerializer

class TodoItemViewSet(viewsets.ModelViewSet):
    queryset = Todo.objects.all()
    serializer_class = TaskSerializer