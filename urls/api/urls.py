from django.urls import path

from urls.api import views

urlpatterns = [
    path('', views.input, name='input'),
   # path('results/', views.results,name="results"),
   path('analysis/',views.analysis,name='analysis'),
   path('marks_enter/',views.marks_enter,name="marks_enter"),
   
]