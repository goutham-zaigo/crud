from rest_framework import serializers
from .models import Employee, WorkAssignment, Project

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = '__all__'

class WorkAssignmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = WorkAssignment
        fields = '__all__'

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = '__all__'