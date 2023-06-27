from rest_framework import status
from rest_framework.response import Response
from rest_framework import viewsets
from .models import Todo, Tag
from .serializers import TaskSerializer
from django.utils import timezone

class TodoItemViewSet(viewsets.ModelViewSet):
    queryset = Todo.objects.all()
    serializer_class = TaskSerializer

    def create(self, request, *args, **kwargs):
        tag_names = request.data.pop('tag', [])

        # Check if tags already exist or create new tags
        tags = []
        for tag_name in tag_names:
            tag, _ = Tag.objects.get_or_create(name=tag_name)
            tags.append(tag)

        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        due_date = serializer.validated_data.get('duedate')

        if due_date and due_date < timezone.now():
            return Response({'error': 'Due date cannot be in the past.'}, status=status.HTTP_400_BAD_REQUEST)

        self.perform_create(serializer)
        serializer.instance.tag.set(tags)

        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
