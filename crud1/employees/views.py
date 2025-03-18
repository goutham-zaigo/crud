from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from rest_framework.viewsets import ModelViewSet
from .models import WorkAssignment, Employee, Project
from .serializers import WorkAssignmentSerializer, ProjectSerializer
from rest_framework.pagination import PageNumberPagination


class WorkAssignmentAPIView(APIView):

    

    def get(self, request, employee_id):
        try:
            # Check if employee exists
            employee = Employee.objects.get(pk=employee_id)
        except Employee.DoesNotExist:
            return Response({"error": "Employee not found"}, status=status.HTTP_404_NOT_FOUND)

        # Get work assignments for that employee
        assignments = WorkAssignment.objects.filter(employee=employee)
        serializer = WorkAssignmentSerializer(assignments, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request, employee_id):
        data = request.data
        data['employee'] = employee_id
        serializer = WorkAssignmentSerializer(data=data)
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



class WorkAssignmentListView(APIView):
    def get(self, request, employee_id):
        assignments = WorkAssignment.objects.filter(employee_id=employee_id)
        
        # Apply pagination
        paginator = PageNumberPagination()
        paginated_assignments = paginator.paginate_queryset(assignments, request)

        # Serialize the paginated data
        serializer = WorkAssignmentSerializer(paginated_assignments, many=True)
        
        return paginator.get_paginated_response(serializer.data)


class ProjectViewSet(ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer