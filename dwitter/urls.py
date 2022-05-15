from django.contrib.auth import views as auth_views
from django.urls import path, include

from dwitter.views import dashboard, get_profile_list, get_profile

app_name = 'dwitter'

urlpatterns = [
    path('', dashboard, name='dashboard'),
    path('profile_list/', get_profile_list, name='profile_list'),
    path('profile/<int:pk>', get_profile, name='profile'),
    path('accounts/', include('django.contrib.auth.urls')),

    # Password reset

    path(
        'password_reset/done/',
        auth_views.PasswordResetDoneView.as_view(),
        name='password_reset_done',
    ),
]