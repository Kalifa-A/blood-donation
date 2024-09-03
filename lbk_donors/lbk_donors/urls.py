"""
URL configuration for lbk_donors project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path
from blood import views
from django.urls import path, include
from django.contrib.auth import views as auth_views
from blood.forms import MyPasswordResetForm

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home,name="Home"),
    path('insert/',views.insert,name="insert"),
    path('need/',views.need,name='Need'),
    path('login/',views.login,name='Login'),
    path('login/updateData/<int:id>/',views.updatedata,name='updateData'),
    path('update/',views.update,name="update"),
    path('search/',views.search,name='Search'),
]


