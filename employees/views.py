from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from .models import WorkAssignment, Employee
from .serializers import WorkAssignmentSerializer
from rest_framework.viewsets import ModelViewSet
from .models import Project
from .serializers import ProjectSerializer


class WorkAssignmentAPIView(APIView):

    def get(self, request, employee_id):
        """Retrieve all tasks assigned to an employee"""
        tasks = WorkAssignment.objects.filter(employee_id=employee_id)
        serializer = WorkAssignmentSerializer(tasks, many=True)
        return Response(serializer.data)

    def post(self, request):
        """Assign a new task to an employee"""
        serializer = WorkAssignmentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk):
        """Update task details"""
        task = get_object_or_404(WorkAssignment, pk=pk)
        serializer = WorkAssignmentSerializer(task, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        """Delete a specific task"""
        task = get_object_or_404(WorkAssignment, pk=pk)
        task.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



class ProjectViewSet(ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
