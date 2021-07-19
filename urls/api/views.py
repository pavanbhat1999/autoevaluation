from django.shortcuts import render,redirect
from django.http import HttpResponse
from django import forms
from backend.api.preprocessing import preprocessing,preprocessing_features
from backend.api.predict import execute

import sys
import numpy
import time
numpy.set_printoptions(threshold=sys.maxsize)
class AnswerForm(forms.Form):
   answer = forms.CharField()
   
marks = -1
# Input Page
def input(request):
    if request.method == "POST":

        answer = AnswerForm(request.POST)
        if answer.is_valid():
            answer = answer.cleaned_data['answer']

        # processing of answer   using features and BOW both 
        preprocessed_answer= preprocessing(answer,isTest=True)
        # preprocessed answer only using features
        # preprocessed_answer = preprocessing_features(answer,isTest=True)
        feature_vector = preprocessing_features(answer,isTest=True)

        #print(preprocessed_answer)

        #################Use this answer vector and directly predict################



        for i in range(5):
            time.sleep(1)

            pass
        global marks
        temp = marks
        if marks == -1:
            temp = execute(feature_vector)
        else:
            marks = -1
        # marks = request.session.get('marks',execute(feature_vector))
        # if 'marks' in request.session:
            # del request.session['marks']















        ################################################################################



        return render(request,"Result.html",{'vectoranswer':preprocessed_answer,'prediction':temp,'feature_vector':feature_vector})
    return render(request,"form.html")

##  Result Page    
def results(request):
    return render(request,"Result.html")
def analysis(request):
    return render(request,"analysis.html")
def marks_enter(request):
    if request.method == "POST":
        # request.session['marks'] = request.POST['marks']
        # print(request.session.get('marks'))
        global marks
        marks = request.POST['marks']
    return render(request,'marks.html')