from django.db import models

class Employee(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.name



class Employee(models.Model):
    name = models.CharField(max_length=100)
    position = models.CharField(max_length=100, default="developer")


class WorkAssignment(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    task_name = models.CharField(max_length=255)
    description = models.TextField()
    due_date = models.DateField()



class Project(models.Model):
    name = models.CharField(max_length=255)
    employees = models.ManyToManyField(Employee, related_name="projects")

    def __str__(self):
        return self.name
