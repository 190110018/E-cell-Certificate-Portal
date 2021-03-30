from django.urls import path
from . import views 

urlpatterns = [
    path('login/', views.loginPage, name="login"),
    path('logout/', views.logoutUser, name="logout"),
    path('dd_certi/<filename>/',views.dd_certi,name="dd-certi"),
    path('view_certi/',views.view_certi,name="view-certi"),
]

