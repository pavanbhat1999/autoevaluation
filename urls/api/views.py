from django.shortcuts import render,redirect
from django.http import HttpResponse
from django import forms
from backend.api.preprocessing import preprocessing
from backend.api.predict import predict

import sys
import numpy
numpy.set_printoptions(threshold=sys.maxsize)
class AnswerForm(forms.Form):
   answer = forms.CharField(max_length = 100)
   

# Input Page
def input(request):
    if request.method == "POST":

        answer = AnswerForm(request.POST)
        if answer.is_valid():
            answer = answer.cleaned_data['answer']

        # processing of answer    
        preprocessed_answer= preprocessing(answer,isTest=True)
        print(preprocessed_answer)

        #################Use this answer vector and directly predict################



        marks = predict(preprocessed_answer)















        ################################################################################



        return render(request,"Result.html",{'vectoranswer':preprocessed_answer,'prediction':marks})
    return render(request,"form.html")

##  Result Page    
# def results(request):
#     return render(request,"Result.html")

    
