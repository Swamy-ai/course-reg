from django.urls import path
from .views import course_view,delete_course

urlpatterns = [
    path('course/', course_view, name='course'),
    path('delete/<int:course_id>/', delete_course, name='delete_course')
]