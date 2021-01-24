"""tutor URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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

from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
   
   path('<int:user_id>', views.index , name='index'),
   path('search', views.search , name='search'),
   path('', views.home , name='home'),
   path('loginPage', views.loginPage , name='loginPage'),
   path('login', views.login, name='login'),
   path('register', views.register, name='register'),
   path('sndRegister', views.sndRegister, name='sndRegister'),
   path('profile_one', views.profile_one, name='profile_one'),
   path('profile_two', views.profile_two, name='profile_two'),
   path('sendOtp', views.sendOtp, name='sendOtp'),
   path('send_otp', views.send_otp, name='send_otp'),
   path('create_profile_one', views.create_profile_one, name='create_profile_one'),
   path('create_profile_two', views.create_profile_two, name='create_profile_two'),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
