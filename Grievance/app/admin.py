from django.contrib import admin

# Register your models here.
from .models import Complaint, Department, Category

@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)

@admin.register(Complaint)
class ComplaintAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'department','category', 'status', 'date', 'assigned_to')
    list_filter = ('department', 'status', 'date')
    search_fields = ('name', 'email', 'complaintText')
