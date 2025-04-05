from django.db import models

from django.core.exceptions import ValidationError
from faculty.models import User,Course
# Create your models here.

        
class Registration(models.Model):
    student = models.ForeignKey(User, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    registration_date = models.DateTimeField(auto_now_add=True)

    def check_course_limit(self):
        if Registration.objects.filter(student=self.student).count() >= 2:
            raise ValidationError("students can register for a maximum of 2 courses")

    def save(self, *args, **kwargs):
        self.check_course_limit()
        super().save(*args, **kwargs)


