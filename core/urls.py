from django.contrib.auth import views as auth_views
from django.urls import path
from django.views.generic.base import TemplateView

from . import views
from .forms import LoginForm

app_name = "core"

urlpatterns = [
    path('', views.index, name='index'),
    path('contact/', views.contact, name = 'contact'),
    path('about/', views.about, name = 'about'),
    path('signup/', views.signup, name='signup'),
    path('login/', auth_views.LoginView.as_view(template_name = 'core/login.html', authentication_form = LoginForm), name= 'login'),
    # path('logout/', views.logout_view, name= 'logout'),
    path('logout/', auth_views.LogoutView.as_view(), name= 'logout'), #template_name = "core/logout.html"
]