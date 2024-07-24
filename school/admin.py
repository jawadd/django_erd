from django.contrib import admin
from .models import Student,Course,Enrollment

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('student_id', 'name', 'age', 'enrollment_date')
    search_fields = ('name',)
    list_filter = ('enrollment_date',)

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('course_id', 'course_name')
    search_fields = ('course_name',)
    list_filter = ('course_name',)

@admin.register(Enrollment)
class EnrollmentAdmin(admin.ModelAdmin):
    list_display = ('enrollment_id', 'student', 'course', 'enrollment_date')
    search_fields = ('student__name', 'course__course_name')
    list_filter = ('enrollment_date', 'course__course_name')
