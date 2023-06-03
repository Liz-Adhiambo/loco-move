from django.urls import path, include
from .views import *


urlpatterns = [

path('user/login', user_login_view, name='clientlogin'),
path('driver/signup', driver_signup_view, name='driver_signup_view'),

]