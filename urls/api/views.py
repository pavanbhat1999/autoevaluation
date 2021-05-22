from django.shortcuts import render
from django.http import HttpResponse
from django import forms
from backend.api.preprocessing import preprocessing_input
from backend.api.predict import predict

import sys
import numpy
numpy.set_printoptions(threshold=sys.maxsize)
class AnswerForm(forms.Form):
   answer = forms.CharField(max_length = 100)
   


def input(request):
    if request.method == "POST":

        answer = AnswerForm(request.POST)
        if answer.is_valid():
            answer = answer.cleaned_data['answer']

        # processing of answer    
        pre_answer= preprocessing_input(answer)
        print(pre_answer)

        #################Use this answer vector and directly predict################



        marks = predict(pre_answer)















        ################################################################################



        return HttpResponse(pre_answer)
        
    return render(request,"form.html")


    
