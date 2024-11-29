"""
URL configuration for Grievance project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.IndexPage,name="index"),
    path('login/',views.LoginPage,name="login"),
    path('register/',views.RegistrationPage,name="register"),
    path('logout/',views.LogoutPage,name='logout'),
    #Complaint-related URLs
    path('complaints/register/', views.register_complaint, name='register_complaint'),  # User registers complaints
    path('complaints/list/', views.list_complaints, name='list_complaints'),  # List complaints (user/admin view)
    path('complaints/<int:pk>/manage/', views.manage_complaint, name='manage_complaint'),  # Admin manages a specific complaint

    #admin
    path('manage-complaints/<int:pk>/', views.manage_complaint, name='manage_complaints'),
    path('admin/manage-department/', views.manage_department, name='manage_department'),
]
