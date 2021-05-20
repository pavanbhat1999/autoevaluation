from django.shortcuts import render
from django.http import HttpResponse
from django import forms
from backend.api.preprocess import preprocess
class AnswerForm(forms.Form):
   answer = forms.CharField(max_length = 100)
   


def input(request):
    if request.method == "POST":

        answer = AnswerForm(request.POST)
        if answer.is_valid():
            answer = answer.cleaned_data['answer']
        #########TODO#########################################################################################
        pre_answer= preprocess(answer)
        
        marks = predict(pre_answer)






        return HttpResponse(marks)
        
    return render(request,"form.html")

def predict(request):
    ################Composite Algorithm prediction###################

    # include preprocessing in composite algorithm part itself
    #just return prediction marks
    prediction = request
    
    return prediction
    
