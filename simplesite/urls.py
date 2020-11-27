from django.contrib import admin
from django.urls import path, include
from . import views
from users import views as user_views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', include('mainapp.urls')),
    path('addemp/', include('mainapp.urls')),

    path('register/', user_views.register, name='register'), ## Register 
    path('profile/', user_views.profile, name='profile'), ## Profile 
    
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'), ## Log in (class based views)
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'), ## Log out (class based views)
]
