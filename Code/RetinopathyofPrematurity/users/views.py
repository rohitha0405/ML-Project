from django.shortcuts import render, HttpResponse
from .forms import UserRegistrationForm
from .models import UserRegistrationModel
from django.contrib import messages
from Maternity.models import RetinopathyofPrematureModel
from .models import UserLinearResultModel,UserGA2MResultModel
from django_pandas.io import read_frame

# Create your views here.
def UserRegisterActions(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            print('Data is Valid')
            form.save()
            messages.success(request, 'You have been successfully registered')
            form = UserRegistrationForm()
            return render(request, 'UserRegistrations.html', {'form': form})
        else:
            messages.success(request, 'Email or Mobile Already Existed')
            print("Invalid form")
    else:
        form = UserRegistrationForm()
    return render(request, 'UserRegistrations.html', {'form': form})


def UserLoginCheck(request):
    if request.method == "POST":
        loginid = request.POST.get('loginname')
        pswd = request.POST.get('pswd')
        print("Login ID = ", loginid, ' Password = ', pswd)
        try:
            check = UserRegistrationModel.objects.get(loginid=loginid, password=pswd)
            status = check.status
            print('Status is = ', status)
            if status == "activated":
                request.session['id'] = check.id
                request.session['loggeduser'] = check.name
                request.session['loginid'] = loginid
                request.session['email'] = check.email
                print("User id At", check.id, status)
                return render(request, 'users/UserHome.html', {})
            else:
                messages.success(request, 'Your Account Not at activated')
                return render(request, 'UserLogin.html')
        except Exception as e:
            print('Exception is ', str(e))
            pass
        messages.success(request, 'Invalid Login id and password')
    return render(request, 'UserLogin.html', {})


def UserHome(request):
    return render(request, 'users/UserHome.html', {})

def UserViewData(request):
    data = RetinopathyofPrematureModel.objects.all()
    return render(request, 'users/UserViewAllData.html', {'data': data})

def UserLinearModel(request):
    data = RetinopathyofPrematureModel.objects.all()
    df = read_frame(data)
    print(df.head())
    # import statsmodels.api as sm
    # x = df['gestationalweek','mechanicalventilation']
    # y = df['gender']
    # exog, endog = sm.add_constant(x), y
    # mod = sm.GLM(endog, exog, family=sm.families.Poisson(link=sm.families.links.log))
    # res = mod.fit()
    from sklearn.model_selection import train_test_split
    from sklearn.linear_model import LogisticRegression
    from sklearn.metrics import accuracy_score,precision_score, recall_score
    X = df.iloc[:, 1:10].values
    y = df.iloc[:, 3].values
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=1 / 3, random_state=0)

    model = LogisticRegression()
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    accuracy = accuracy_score(y_pred,y_test)
    precesion = precision_score(y_pred, y_test, pos_label = 'positive', average = 'micro')
    recall = recall_score(y_test, y_pred, pos_label = 'positive',  average = 'micro')
    print("Precesion = ", precesion)
    from .ChiSquaretest import TestChiSquare
    obj = TestChiSquare()
    chitest = obj.findTestResult(df)
    print("Chisquare Test ",chitest)
    loginid =request.session['loginid']
    UserLinearResultModel.objects.create(name=loginid,accuracy=accuracy, precesion=precesion,recall=recall,chitest=chitest)
    return render(request, "users/LinearResult.html",{'accuracy':accuracy,'precesion':precesion,'recall':recall, 'chitest':chitest})


def Userga2m(request):
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
    print("Scale =",scale," Devince = ",deviance, " pearsonc = ",pearson_chi2," llf = ",llf)
    UserGA2MResultModel.objects.create(name=loginid, scale=scale, deviance=deviance, pearson_chi2=pearson_chi2,llf=llf)
    return render(request, "users/LinearGa2mResult.html",{'scale':scale,'deviance':deviance,'pearson_chi2':pearson_chi2, 'llf':llf})