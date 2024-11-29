from django import forms
from .models import Complaint, Department, Category

class ComplaintSubmissionForm(forms.ModelForm):
    """
    Form for users to submit complaints. Only includes user-fillable fields.
    """
    class Meta:
        model = Complaint
        fields = ['name', 'email', 'complaintText', 'uploadFile', 'department','category']  # No admin-only fields

class ComplaintManagementForm(forms.ModelForm):
    """
    Form for admins or HODs to update complaint status, priority, and assignment.
    """
    class Meta:
        model = Complaint
        fields = ['status', 'priority', 'assigned_to']  # Includes admin-only fields

class DepartmentForm(forms.ModelForm):
    """
    Form for updating HOD of a department.
    """
    class Meta:
        model = Department
        fields = ['name', 'hod']  # Ensure 'hod' is defined in your Department model
