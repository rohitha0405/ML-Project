"""RetinopathyofPrematurity URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from RetinopathyofPrematurity import views as mainView
from users import views as usr
from admins import views as admins
from Maternity import views as rop

urlpatterns = [
    path('admin/', admin.site.urls),
    path("",mainView.index, name="index"),
    path("index/", mainView.index, name="index"),
    path("logout/", mainView.logout, name="logout"),
    path("UserLogin/", mainView.UserLogin, name="UserLogin"),
    path("AdminLogin/", mainView.AdminLogin, name="AdminLogin"),
    path("UserRegister/", mainView.UserRegister, name="UserRegister"),
    path("MaternityLogin/", mainView.MaternityLogin, name="MaternityLogin"),

    ### User Side Views
    path("UserRegisterActions/", usr.UserRegisterActions, name="UserRegisterActions"),
    path("UserLoginCheck/", usr.UserLoginCheck, name="UserLoginCheck"),
    path("UserHome/", usr.UserHome, name="UserHome"),
    path("UserViewData/", usr.UserViewData, name="UserViewData"),
    path("UserLinearModel/", usr.UserLinearModel, name="UserLinearModel"),
    path("Userga2m/", usr.Userga2m, name="Userga2m"),

    #### Admin Side views
    path("AdminLoginCheck/", admins.AdminLoginCheck, name="AdminLoginCheck"),
    path("AdminHome/", admins.AdminHome, name="AdminHome"),
    path("ViewAllUsers/", admins.ViewAllUsers, name="ViewAllUsers"),
    path("AdminActivaUsers/", admins.AdminActivaUsers, name="AdminActivaUsers"),
    path("AdminLinearResults/", admins.AdminLinearResults, name="AdminLinearResults"),
    path("AdminGA2Results/", admins.AdminGA2Results, name="AdminGA2Results"),

    #Maternity URLS
    path("MaternityLoginCheck/", rop.MaternityLoginCheck, name="MaternityLoginCheck"),
    path("MaternityHome/", rop.MaternityHome, name="MaternityHome"),
    path("MaternityAddDataForm/", rop.MaternityAddDataForm, name='MaternityAddDataForm'),
    path("MaternityAddDataAction/", rop.MaternityAddDataAction, name="MaternityAddDataAction"),
    path("MaternityGa2m/", rop.MaternityGa2m, name="MaternityGa2m"),
    path("MaternityViewGA2mResults/", rop.MaternityViewGA2mResults, name="MaternityViewGA2mResults"),



]
