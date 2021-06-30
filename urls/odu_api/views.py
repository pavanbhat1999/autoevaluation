from django.shortcuts import render,redirect
from django.http import HttpResponse
from django import forms
import pyrebase
from urls.odu_api import configurations
from urls.odu_api.givVal import eval,givVal
import urls.odu_api.cosine_similarity as keywordVal
import urls.odu_api.configurations as configurations
import urls.odu_api.nav_test
from fuzzywuzzy import fuzz




firebsevar = pyrebase.initialize_app(config=configurations.config)
db = firebsevar.database()


class AnswerForm(forms.Form):
    first  = forms.CharField(max_length = 500)
    second = forms.CharField(max_length = 500)
    third  = forms.CharField(max_length = 500)
    email  = forms.CharField(max_length = 50)

def get_answers(request):
    if request.method == "POST":
    
        first  = request.POST['first']
        second = request.POST['second']
        third  = request.POST['third']

        email = request.POST['emailID']
        ans = {"a1": first, "a2": second, "a3": third, "email": email}

        result = db.child("/answers1").push(ans)
        return render(request,"app_teacher.html")


    return render(request,"first.html")

def get_results(request):
    if request.method == "POST":
        eval()

    return render(request,"result.html")

def show_results(request):
    if request.method == "POST":
        email=request.POST['name']
        all_answers = db.child("answers").get()
        for each_users_answers in all_answers.each():
            if email==each_users_answers.val()['email']:
                print("email found")
                marks1=str(each_users_answers.val()['result1'])
                marks2=str(each_users_answers.val()['result2'])
                marks3=str(each_users_answers.val()['result3'])
                    
    return render(request,"out.html",{'email':email,'marks1':marks1,'marks2':marks2,'marks3':marks3})