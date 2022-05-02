from django.urls import path

from dwitter.views import dashboard, get_profile_list, get_profile

app_name = 'dwitter'

urlpatterns = [
    path('', dashboard, name='dashboard'),
    path('profile_list/', get_profile_list, name='profile_list'),
    path('profile/<int:pk>', get_profile, name='profile'),
]