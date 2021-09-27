from django.db import models
from django.db.models.deletion import CASCADE
from django.db.models.fields import DateTimeField

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=50)
    mobile = models.IntegerField()
    email = models.EmailField(max_length=50)
    city = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Teacher(models.Model):
    name = models.CharField(max_length=50)
    mobile = models.IntegerField()
    email = models.EmailField(max_length=50)

    def __str__(self):
        return self.name

class Lecture(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    time = models.DateTimeField()
    teacher = models.ForeignKey(Teacher, related_name='teacher', on_delete=models.DO_NOTHING)
    student = models.ManyToManyField(Student, related_name='student')

    def __str__(self):
        return self.name
