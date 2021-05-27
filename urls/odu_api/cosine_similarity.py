import re, math
from collections import Counter
import fuzzywuzzy.fuzz
import nltk
from nltk.corpus import wordnet
#import PyDictionary
from nltk.stem import WordNetLemmatizer,PorterStemmer

WORD = re.compile(r'\w+')


def get_cosine(vec1, vec2):
    numerator=0
    intersection = set(vec1.keys()) & set(vec2.keys())
    
 #>>>>>>>>>>>>>synonym checking
    
    
    #print(set(vec1.keys()) , set(vec2.keys()))
    for y1 in set(vec1.keys()):
        #print(y1)
        if y1 not in set(vec2.keys()):
            syn=wordnet.synsets(y1)
            #print(syn)
            if syn==None:
                print("none")
                continue
            #print(syn)
            
            mean =[]
            for i in range(len(syn)):
                mean.append(syn[i].lemmas()[0].name())
            #print("name=",mean)
            for j1 in mean:
                if j1 in set(vec2.keys()):
                    
                    #print("found",j1)
                    #print(set(vec2.keys()))
                    #print(y1,"=",j1)
                    #intersection.add(y1)
                    numerator= numerator+1
    
    
    
    #print("                                     ",intersection)
    #print(vec1[y1],vec2[y1])
    numerator = numerator+sum([vec1[x] * vec2[x] for x in intersection])
    #print(numerator)
    sum1 = sum([vec1[x] ** 2 for x in vec1.keys()])
    sum2 = sum([vec2[x] ** 2 for x in vec2.keys()])
    denominator = math.sqrt(sum1) * math.sqrt(sum2)

    if not denominator:
        return 0.0
    else:
        return float(numerator) / denominator


def text_to_vector(text):
    words = WORD.findall(text)
    return Counter(words)


def givKeywordsValue(text1, text2):
    vector1 = text_to_vector(text1)
    vector2 = text_to_vector(text2)
    cosine = round(get_cosine(vector1, vector2),2)*100
    #print(cosine)
    kval = 0
    if cosine > 90:
        kval = 1
    elif cosine > 80:
        kval = 2
    elif cosine > 60:
        kval = 3
    elif cosine > 40:
        kval = 4
    elif cosine > 20:
        kval = 5
    else:
        kval = 6
    return kval

