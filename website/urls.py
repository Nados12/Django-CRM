from django.urls import path  
from . import views

urlpatterns = [
    path('', views.home , name='home'),
    # path('login/', views.login_user , name='login'), - - אם אני מעוניין לעשות עמוד לוגין נפרד
    path('logout/', views.logout_user , name='logout'),
    path('register/', views.register_user , name='register'),
    
   
]       
    