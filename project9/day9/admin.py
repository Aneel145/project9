from django.contrib import admin
from.models import Student,Department
class StudentAdmin(admin.ModelAdmin):
    list_display = ('name', 'age', 'email',)
    search_fields = ('name', 'email','age')
admin.site.register(Student,StudentAdmin)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('name', 'head', 'number_of_students',)
    search_fields = ('name', 'head','number_of_students')
admin.site.register(Department, DepartmentAdmin)
# Register your models here.
