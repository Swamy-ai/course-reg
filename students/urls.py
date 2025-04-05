from django.urls import path
from .views import login_view,registration_view,logout_view,signup_view

urlpatterns = [
    path('login/', login_view, name='login'),
    path('registration/', registration_view, name='registration'),
    path('logout/', logout_view, name='logout'),
    path('signup/', signup_view, name='signup'),
]