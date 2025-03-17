from rest_framework import serializers
from .models import WorkAssignment, Employee, Project


class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = ['id', 'name', 'email']


class WorkAssignmentSerializer(serializers.ModelSerializer):
    employee = EmployeeSerializer()

    class Meta:
        model = WorkAssignment
        fields = ['id', 'employee', 'task_name', 'description', 'due_date']


class ProjectSerializer(serializers.ModelSerializer):
    employees = EmployeeSerializer(many=True)

    class Meta:
        model = Project
        fields = ['id', 'name', 'employees']
