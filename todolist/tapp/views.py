from rest_framework import generics
from .models import Todo
from .serializers import TaskSerializer


class TaskListView(generics.ListCreateAPIView):
    queryset = Todo.objects.all()
    serializer_class = TaskSerializer

class TaskDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Todo.objects.all()
    serializer_class = TaskSerializer
