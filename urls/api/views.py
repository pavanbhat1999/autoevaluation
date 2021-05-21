from django.shortcuts import render
from django.http import HttpResponse
from django import forms
from backend.api.preprocess import process_input
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
        #########TODO#########################################################################################
        pre_answer= process_input(answer)
        print(pre_answer)
        marks = predict(pre_answer)






        return HttpResponse(pre_answer)
        
    return render(request,"form.html")

def predict(request):
    ################Composite Algorithm prediction###################

    
    #just return prediction marks
    prediction = "Marks predicted is  5"
    
    return prediction,
    
