from django.db import models
from django.contrib.auth.models import User
from datetime import timedelta
from django.utils.timezone import now

class Department(models.Model):
    """
    Model to represent a department. Created and managed by admins only.
    """
    name = models.CharField(max_length=100, unique=True)
    hod = models.OneToOneField(
        User, null=True, blank=True, on_delete=models.SET_NULL, related_name='department_hod'
    )  # HOD for the department

    def __str__(self):
        return self.name

class Category(models.Model):
    """
    Model to represent categories of complaints.
    """
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

class Complaint(models.Model):
    """
    Model to represent user complaints.
    """
    STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('In Progress', 'In Progress'),
        ('Resolved', 'Resolved'),
    ]
    PRIORITY_CHOICES = [
        ('Low', 'Low'),
        ('Medium', 'Medium'),
        ('High', 'High'),
    ]

    name = models.CharField(max_length=50)
    email = models.EmailField()
    complaintText = models.TextField()
    uploadFile = models.FileField(upload_to='files/', blank=True, null=True)
    date = models.DateField(auto_now_add=True)
    department = models.ForeignKey(Department, on_delete=models.CASCADE, related_name='complaints')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='category')
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Pending')
    priority = models.CharField(max_length=20, choices=PRIORITY_CHOICES, default='Low')
    assigned_to = models.ForeignKey(
        User, null=True, blank=True, on_delete=models.SET_NULL, related_name='assigned_complaints'
    )

    def auto_resolve_date(self):
        """
        Calculate the date after which the complaint should be automatically resolved.
        """
        return self.date + timedelta(days=3)

    def is_auto_resolvable(self):
        """
        Check if the complaint is due for auto-resolution.
        """
        return now().date() > self.auto_resolve_date()

    def __str__(self):
        return f"Complaint by {self.name} - {self.status}"
