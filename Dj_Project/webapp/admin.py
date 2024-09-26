from django.contrib import admin
from webapp.models import Employee

# Register your models here.
class EmpAdmin(admin.ModelAdmin):
    list_display = ['id', 'emp_id', 'name', 'salary', 'job', 'company']

admin.site.register(Employee, EmpAdmin)