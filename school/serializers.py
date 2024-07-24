from .models import Student,Course,Enrollment
from rest_framework import serializers


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['student_id','name', 'age','enrollment_date', 'bio']