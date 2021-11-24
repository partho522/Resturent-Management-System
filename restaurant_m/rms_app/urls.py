
from django.urls import path
from . import views


urlpatterns = [
    path("login/",views.login_v,name = "login"), 
    path("home/", views.home, name = "home" ),
    path("add_emp/", views.add_emp, name = "add_emp" ),
    path("display_emp/", views.display_emp, name = "display_emp" ),
    path("del_emp/",views.del_emp, name = "del_emp"),
    path("add_bill/",views.add_bill, name = "add_bill"),
    path("display_bill/",views.display_bill, name = "display_bill"),
    path("",views.home,name = "home"),
    path("logout/",views.logout_v, name = "logout")
]