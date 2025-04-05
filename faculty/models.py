from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.


class User(AbstractUser):
    roles=[
        ('student', 'Student'),
        ('faculty', 'Faculty'),
    ]
    role = models.CharField(max_length=10,choices=roles)

    def __str__(self):
        return f'{self.username} - {self.role}'
    
class Course(models.Model):
    course_name = models.CharField(max_length=100)
    course_code = models.CharField(max_length=10, unique=True)
    offered_by = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.course_name


