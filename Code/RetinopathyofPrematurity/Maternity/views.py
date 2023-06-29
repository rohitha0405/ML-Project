from django.shortcuts import render
from django.contrib import messages
from .forms import RetinopathyofPrematureForm
from django_pandas.io import  read_frame
from .models import RetinopathyofPrematureModel
from users.models import UserGA2MResultModel
# Create your views here.
def MaternityLoginCheck(request):
    if request.method == 'POST':
        usrid = request.POST.get('loginname')
        pswd = request.POST.get('pswd')
        print("User ID is = ", usrid)
        if usrid == 'Maternity' and pswd == 'Maternity':
            return render(request, 'maternity/MaternityHome.html')
        elif usrid == 'maternity' and pswd == 'maternity':
            return render(request, 'maternity/MaternityHome.html')
        else:
            messages.success(request, 'Please Check Your Login Details')
    return render(request, 'MaternityLogin.html', {})


def MaternityHome(request):
    return render(request, 'maternity/MaternityHome.html')

def MaternityAddDataForm(request):
    form = RetinopathyofPrematureForm()
    return render(request, 'maternity/AddMaternityNewbaby.html',{'form':form})


def MaternityAddDataAction(request):
    if request.method == 'POST':
        form = RetinopathyofPrematureForm(request.POST)
        if form.is_valid():
            print('Data is Valid')
            form.save()
            messages.success(request, 'Data Stored Create one More')
            form = RetinopathyofPrematureForm()
            return render(request, 'maternity/AddMaternityNewbaby.html', {'form': form})
        else:
            messages.success(request, 'Invalid Entry')
            print("Invalid form")
    else:
        form = RetinopathyofPrematureForm()
    return render(request, 'maternity/AddMaternityNewbaby.html', {'form': form})


def MaternityGa2m(request):
    data = RetinopathyofPrematureModel.objects.all()
    df = read_frame(data)
    X = df.iloc[:, 1].values.astype(int)
    y = df.iloc[:, 3].values.astype(int)
    # Poisson regression code
    import statsmodels.api as sm
    exog, endog = sm.add_constant(X), y
    mod = sm.GLM(endog, exog,
                 family=sm.families.Poisson(link=sm.families.links.log))
    res = mod.fit()
    print(res.params)
    scale = res.scale
    deviance = res.deviance
    pearson_chi2 = res.pearson_chi2
    llf = res.llf
    loginid = request.session['loginid']
    print("Scale =", scale, " Devince = ", deviance, " pearsonc = ", pearson_chi2, " llf = ", llf)

    return render(request, "maternity/MaternityGa2mResult.html",
                  {'scale': scale, 'deviance': deviance, 'pearson_chi2': pearson_chi2, 'llf': llf})

def MaternityViewGA2mResults(request):
    data = UserGA2MResultModel.objects.all()
    return render(request,'maternity/ViewGa2mResults.html',{'data':data})
