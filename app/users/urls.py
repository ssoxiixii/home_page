from django.contrib.auth import views as auth_views
from django.urls import path

urlpatterns = [
    path(
        'login/',
        auth_views.LoginView.as_view(
            template_name='auth/login.html',
            next_page='home_page',
        ),
        name='login',
    ),
    path(
        'logout/',
        auth_views.LogoutView.as_view(next_page='home_page'),
        name='logout',
    ),
]
