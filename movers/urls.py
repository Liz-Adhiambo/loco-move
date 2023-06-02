from django.urls import path, include
from .views import *


urlpatterns = [

path('user/login', user_login_view, name='clientlogin'),

]