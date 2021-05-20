from django.shortcuts import render
from django.http import HttpResponse
from django import forms

class AnswerForm(forms.Form):
   answer = forms.CharField(max_length = 100)
   


def input(request):
    if request.method == "POST":

        answer = AnswerForm(request.POST)
        if answer.is_valid():
            answer = answer.cleaned_data['answer']
        #########TODO#########################################################################################
        
        marks = predict(answer)






        return HttpResponse(marks)
        
    return render(request,"form.html")
def predict(request):
    ################Composite Algorithm prediction###################
    prediction = 0
    
    return prediction
    
