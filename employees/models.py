from django.db import models

class Employee(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.name

class WorkAssignment(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name="assignments")
    task_name = models.CharField(max_length=255)
    description = models.TextField()
    due_date = models.DateField()

    def __str__(self):
        return self.task_name

class Project(models.Model):
    name = models.CharField(max_length=255)
    employees = models.ManyToManyField(Employee, related_name="projects")

    def __str__(self):
        return self.name
