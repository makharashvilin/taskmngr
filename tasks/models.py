from django.db import models


STATUSES = {'draft':'Draft', 'in progres':'In Progress', 'completed':'Completed'}
class Task(models.Model):
    name = models.CharField(max_length=100)
    status = models.CharField(max_length=100,choices=STATUSES)
    description = models.CharField(max_length=100)


