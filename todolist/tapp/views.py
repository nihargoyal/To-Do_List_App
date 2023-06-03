from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Todo
from .serializers import TaskSerializer

@api_view(['POST'])
def create_task(request):
    serializer = TaskSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)

@api_view(['GET'])
def read_task(request, pk):
    try:
        todo_item = Todo.objects.get(pk=pk)
        serializer = TaskSerializer(todo_item)
        return Response(serializer.data)
    except Todo.DoesNotExist:
        return Response(status=404)

@api_view(['GET'])
def read_all_task(request):
    todo_items = Todo.objects.all()
    serializer = TaskSerializer(todo_items, many=True)
    return Response(serializer.data)

@api_view(['PUT'])
def update_task(request, pk):
    try:
        todo_item = Todo.objects.get(pk=pk)
        serializer = TaskSerializer(todo_item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)
    except Todo.DoesNotExist:
        return Response(status=404)

@api_view(['DELETE'])
def delete_task(request, pk):
    try:
        todo_item = Todo.objects.get(pk=pk)
        todo_item.delete()
        return Response(status=204)
    except Todo.DoesNotExist:
        return Response(status=404)
