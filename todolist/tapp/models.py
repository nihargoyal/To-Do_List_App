from django.db import models

# Create your models here.
class Tag(models.Model):
    name = models.CharField(max_length=200, unique=True)

class Todo(models.Model):
    timestamp=models.DateTimeField(auto_now_add=True)
    title=models.CharField(max_length=200,)
    description=models.TextField(blank=True,)
    duedate=models.DateTimeField(blank=True, null=True)
    tag=models.ManyToManyField('Tag', blank=True)

    loan_status = [
        ('OPEN','Open'),
        ('WORKING','Working'),
        ('DONE','Done'),
        ('OVERDUE','Overdue'),
    ]

    status = models.CharField(max_length=10, choices=loan_status, blank=False, default='OPEN')