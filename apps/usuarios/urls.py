from django.contrib.auth import views as auth_views
from django.urls import path, reverse_lazy, include
from . import views
from .forms import LoginForm

app_name = 'usuarios'
urlpatterns = [
    path(
        "login/",
        auth_views.LoginView.as_view(
            template_name = "usuarios/login.html",
            form_class = LoginForm
        ),
        name="login"
    ),

    path("logout/", auth_views.LogoutView.as_view(), name="logout"),
    path("register/", views.register, name="register"),
    path("<int:id>/", views.perfil, name="perfil"),
    path("edit/", views.edit_profile, name="edit_profile"),
    path(
        "password/",
        auth_views.PasswordChangeView.as_view(
            template_name = "usuarios/password.html",
            success_url = reverse_lazy("home")
        ),
        name="change_password"
    ),    

]