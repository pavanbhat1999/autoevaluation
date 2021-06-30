from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User , auth
from django.contrib import messages
# Create your views here.
def home(request):
    return render(request,'Home.html')
def register(request):
    message=""
    if request.method == "POST":
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        print(password1)
        try:
            user = User.objects.create_user(username=username,password=password1,email=email)
            user.save()

            user = auth.authenticate(username=username,password=password1)
            auth.login(request,user)
        except:
            return HttpResponse("error in register Please register again possible username repeat")
    # return render(request,'form.html',{'message':message})
    return render(request,'test_select.html',{'message':message})
def login(request):
    message=""
    if request.method == "POST":
        username = request.POST['username'] 
        password = request.POST['password']
        user = auth.authenticate(username=username,password=password)
        print(user)
        if user is None:
           return HttpResponse("Error in login possible wrong usernmae")
        if user is not None:
            auth.login(request,user)
            print(username,password)
            return render(request,'test_select.html',{'message':message})
        else:
           return HttpResponse("Error in login")

    return render(request,'Home.html')
def logout(request):
    auth.logout(request)
    return redirect("home")
