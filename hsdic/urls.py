from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('check_code/', views.check_code, name='check_code'),
    path('signup/', views.signup, name='signup'),
    path('signup_user/', views.signup_user, name='signup_user'),
    path('signup/check_username/', views.check_username, name='check_username'),
    # path('check_username/', views.check_username, name='check_username'),
]
