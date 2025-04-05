from django.shortcuts import render,redirect,get_object_or_404
from .models import Course,User
from .decorators import role_required
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required
@role_required('faculty')
def course_view(request):
    if request.method == 'POST':
        course_name = request.POST.get('course_name')
        course_code = request.POST.get('course_code')
        offered_by_id = request.POST.get('offered_by')

        if course_name and course_code and offered_by_id:
            offered_by = User.objects.get(id=offered_by_id)
            Course.objects.create(course_name=course_name, course_code=course_code, offered_by=offered_by)
            return redirect('course')

    courses = Course.objects.all()
    faculty_users = User.objects.filter(role='faculty')
    return render(request, 'course.html', {'courses': courses, 'faculty_users': faculty_users})

@role_required('faculty')
def delete_course(request, course_id):
    course = get_object_or_404(Course, id=course_id)
    course.delete()
    return redirect('course')