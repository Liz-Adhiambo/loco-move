from django.urls import path, include
from .views import *


urlpatterns = [

path('user/login', user_login_view, name='clientlogin'),
path('driver/signup', driver_signup_view, name='driver_signup_view'),
path('mover/signup', mover_signup_view, name='mover_signup_view'),
path('profiles/',profile_list),
path('profiles/<int:pk>/',profile_detail),
path('drivers/list',list_drivers),
path('movers/list',list_movers),
path('user/signup',user_signup_view),
path('vehicle/add',add_vehicle),
path('request/move',request_move),
path('schedule/move',schedule_move)

]