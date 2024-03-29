"""
URL configuration for core project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from . import views
from django.views.generic.base import RedirectView
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path("seguridad/", include("Seguridad.urls")),
    path('', views.inicio, name='home'),
    path('login/', views.login_view, name='login'),  # <-- Agrega esta línea
    path('accounts/', include('allauth.urls')),
    path('accounts/profile/', views.profile_view, name='profile_view'),
    path('accounts/profile/', RedirectView.as_view(url='/'), name='redirect_to_home'),
    #path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
    path('social-auth/', include('social_django.urls', namespace='social')),  # Añade esto

]
