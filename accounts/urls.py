from django.urls import path
from accounts.views import login_view, logout_view, signup_view
from django.views.generic import TemplateView


urlpatterns = [
    path("signup/", signup_view, name="signup"),
    path("logout/", logout_view, name="logout"),
    path("login/", login_view, name="login"),
    path(
        "dinwarz/",
        TemplateView.as_view(template_name="accounts/dinwarz.html"),
        name="dinwarz",
    ),
]
