from django.db import models

# Create your models here.
class ClassManager(models.Manager):
    def get_by_course_number(self, course_number):
        return self.get(course_number=course_number)

class djangoClasses(models.Model):
    title = models.CharField(max_length=255)
    course_number =  models.IntegerField()
    instructor_name = models.CharField(max_length=255)
    duration = models.FloatField()

    def __str__(self):
        return f"{self.title} ({self.course_number})"

    class Meta:
        verbose_name_plural = "Django Classes"