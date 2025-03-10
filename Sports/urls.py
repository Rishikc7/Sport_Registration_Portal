"""Sports URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.conf.urls import url, include
from home import views as home_views
from information import views
from my_app.views import Login

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^$', include('home.urls')),
    url(r'information/', include('information.urls'), name='information'),
    url(r'login/', Login, name='login'),
    path('', include('django.contrib.auth.urls')),
    url(r'my_app/', include('my_app.urls')),
]
