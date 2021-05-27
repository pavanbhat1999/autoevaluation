from sklearn.naive_bayes import GaussianNB
import pandas as pd
import numpy as np
import pickle

df = pd.read_csv('static/finaldataset.csv')  #TODO improve this datasets
xf = df[['keyword', 'grammar', 'qst']]


pickle_in = open('static/nav_test.pickle', 'rb')
clf = pickle.load(pickle_in)

#TODO:  Improve Machine Learning Algorithm


def predict(k, g, q):
    predicted = clf.predict([[k, g, q]])
    accuracy = clf.predict_proba([[k, g, q]])
    #print("class[1-9] : " + str(predicted))
    return predicted


