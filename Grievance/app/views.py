from django.shortcuts import render, HttpResponse, get_object_or_404, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required, user_passes_test
from .models import Complaint, Department
from .forms import ComplaintSubmissionForm, ComplaintManagementForm


# Create your views here.

@login_required(login_url='login')
def IndexPage(req):
    context = {
        'username': req.user.username,
        'email': req.user.email,
    }
    return render(req, 'index.html', context)

def LoginPage(req):
    if req.method == 'POST':
        username = req.POST.get('username')
        pass1 = req.POST.get('pass')
        user = authenticate(req, username=username, password=pass1)
        if user is not None:
            login(req, user)
            return redirect('index')
        else:
            return HttpResponse("Username or Password is incorrect!!!")
    return render(req, 'login.html')

def LogoutPage(req):
    logout(req)
    return redirect('login')

def RegistrationPage(req):
    if req.method == 'POST':
        uname = req.POST.get('username')
        email = req.POST.get('email')
        pass1 = req.POST.get('password1')
        pass2 = req.POST.get('password2')
        role = req.POST.get('role')
        if pass1 != pass2:
            return HttpResponse("Your password and confirm password are not the same!")
        else:
            myUser = User.objects.create_user(uname, email, pass1)
            myUser.save()
            return redirect('login')
    return render(req, 'registration.html')

@login_required
def register_complaint(request):
    if request.method == 'POST':
        form = ComplaintSubmissionForm(request.POST, request.FILES)
        if form.is_valid():
            # Save the complaint with the logged-in user's email
            complaint = form.save(commit=False)
            complaint.email = request.user.email
            complaint.save()
            return redirect('index')  # Redirect to a success page
    else:
        form = ComplaintSubmissionForm()

    return render(request, 'app/register_complaint.html', {'form': form})


@login_required
def list_complaints(request):
    if request.user.is_staff and hasattr(request.user, 'assigned_department'):  # Staff view
        complaints = Complaint.objects.filter(department__in=request.user.assigned_department.all())
    elif request.user.is_staff:  # Admin view
        complaints = Complaint.objects.all()
    else:  # Regular user view
        complaints = Complaint.objects.filter(email=request.user.email)
    return render(request, 'app/list_complaints.html', {'complaints': complaints})

# Check if a user is an admin
def is_admin(user):
    return user.is_staff

# Check if a user is HOD
def is_hod(user):
    return hasattr(user, 'department')

@user_passes_test(is_admin)  # Ensure only admins can access
def manage_complaint(request, pk):
    complaint = get_object_or_404(Complaint, pk=pk)
    if request.method == 'POST':
        form = ComplaintManagementForm(request.POST, instance=complaint)
        if form.is_valid():
            form.save()
            return redirect('list_complaints')  # Redirect to complaint list
    else:
        form = ComplaintManagementForm(instance=complaint)

    return render(request, 'admin/manage_complaint.html', {'form': form, 'complaint': complaint})


@user_passes_test(is_admin)
def manage_department(request):
    """
    View to assign or update HODs for departments.
    """
    departments = Department.objects.all()
    if request.method == 'POST':
        department_id = request.POST.get('department_id')
        hod_id = request.POST.get('hod_id')
        department = get_object_or_404(Department, id=department_id)
        department.hod_id = hod_id
        department.save()
        return redirect('manage_department')

    hods = User.objects.filter(is_staff=False)
    return render(request, 'admin/manage_department.html', {
        'departments': departments,
        'hods': hods,
    })
