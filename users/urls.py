from django.urls import path

from . import views

urlpatterns = [
    path('register' , views.register , name = "register"),
    path('login' , views.login_view , name = "login" ),
    path('logout' , views.logout_view , name="logout"),
    path('user' , views.user , name = "user"),
    path('updtuser', views.update_user, name="updtuser"),
]