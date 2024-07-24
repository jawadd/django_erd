from django.db import models
import uuid


class Student(models.Model):
    student_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    age = models.IntegerField()
    enrollment_date = models.DateField()
    bio = models.TextField()

    def __str__(self):
        return self.name


class Course(models.Model):
    course_id =  models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    course_name = models.CharField(max_length=255)
    course_description = models.TextField()

    def __str__(self):
        return self.course_name


class Enrollment(models.Model):
    enrollment_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    enrollment_date = models.DateField()

    def __str__(self):
        return f'{self.student.name} enrolled in {self.course.course_name}'
