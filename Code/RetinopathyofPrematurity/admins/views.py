from django.shortcuts import render
from django.contrib import messages
from users.models import UserRegistrationModel,UserLinearResultModel,UserGA2MResultModel

# Create your views here.

# Create your views here.
def AdminLoginCheck(request):
    if request.method == 'POST':
        usrid = request.POST.get('loginid')
        pswd = request.POST.get('pswd')
        print("User ID is = ", usrid)
        if usrid == 'admin' and pswd == 'admin':
            return render(request, 'admins/AdminHome.html')
        elif usrid == 'Admin' and pswd == 'Admin':
            return render(request, 'admins/AdminHome.html')
        else:
            messages.success(request, 'Please Check Your Login Details')
    return render(request, 'AdminLogin.html', {})


def AdminHome(request):
    return render(request, 'admins/AdminHome.html')


def ViewAllUsers(request):
    data = UserRegistrationModel.objects.all()
    return render(request, 'admins/ViewallUsers.html', {'data': data})


def AdminActivaUsers(request):
    if request.method == 'GET':
        id = request.GET.get('uid')
        status = 'activated'
        print("PID = ", id, status)
        UserRegistrationModel.objects.filter(id=id).update(status=status)
        data = UserRegistrationModel.objects.all()
        return render(request, 'admins/ViewallUsers.html', {'data': data})

def AdminLinearResults(request):
    data = UserLinearResultModel.objects.all()
    return render(request, 'admins/adminLinearResults.html',{'data':data})

def AdminGA2Results(request):
    data = UserGA2MResultModel.objects.all()
    return render(request, 'admins/AdminGa2mResults.html',{'data':data})
