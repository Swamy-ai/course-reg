from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login,logout
from django.contrib import messages
from faculty.models import Course,User
from .models import Registration
from django.core.exceptions import ValidationError
from faculty.decorators import role_required
from django.contrib.auth.decorators import login_required

def login_view(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        print(user)
        if user is not None:
            print(user.role)
            login(request, user)

            if(user.role == "faculty"):
                return redirect('course')
            
            if(user.role == "student"):
                return redirect('registration')
        else:
            messages.error(request, "Invalid username or password.")

    return render(request, 'login.html')

@login_required
# @role_required('student')
def registration_view(request):
    registered_courses = Registration.objects.filter(student=request.user).select_related('course')
    all_courses = Course.objects.exclude(id__in=registered_courses.values_list('course_id', flat=True))

    if request.method == 'POST':
        course_id = request.POST.get('course_id')
        if course_id:
            try:
                course = Course.objects.get(id=course_id)
                registration = Registration(student=request.user, course=course)
                registration.save()
                return redirect('registration')
            except ValidationError as e:
                return render(request, 'registration.html', {
                    'error': str(e),
                    'registered_courses': registered_courses,
                    'available_courses': all_courses
                })

    return render(request, 'registration.html', {
        'registered_courses': registered_courses,
        'available_courses': all_courses
    })

def logout_view(request):
    logout(request)
    return redirect('login')

def signup_view(request):
    if request.method == "POST":
        username = request.POST['username']
        email = request.POST.get('email', '')
        role = request.POST['role']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if password1 != password2:
            return render(request,'signup.html',{'error':"Passwords do not match."})

        if User.objects.filter(username=username).exists():
            return render(request,'signup.html',{'error':"Username already exists."})

        user = User.objects.create_user(username=username, email=email, password=password1, role=role)
        return redirect('login')

    return render(request, 'signup.html')
