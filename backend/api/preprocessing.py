# importing required packages

import nltk
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from nltk.stem import WordNetLemmatizer
from nltk.corpus import wordnet
# import nltk
# nltk.download('all')
import re, collections
from collections import defaultdict
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression, Ridge, Lasso
from sklearn.svm import SVR
from sklearn import ensemble
from sklearn.model_selection import GridSearchCV
from sklearn.metrics import cohen_kappa_score
def sentence_to_wordlist(raw_sentence):
    
    clean_sentence = re.sub("[^a-zA-Z0-9]"," ", raw_sentence)
    tokens = nltk.word_tokenize(clean_sentence)
    
    return tokens
# tokenizing an essay into a list of word lists

def tokenize(essay):
    stripped_essay = essay.strip()
    
    tokenizer = nltk.data.load('tokenizers/punkt/english.pickle')
    raw_sentences = tokenizer.tokenize(stripped_essay)
    
    tokenized_sentences = []
    for raw_sentence in raw_sentences:
        if len(raw_sentence) > 0:
            tokenized_sentences.append(sentence_to_wordlist(raw_sentence))
    
    return tokenized_sentences
def avg_word_len(essay):
    
    clean_essay = re.sub(r'\W', ' ', essay)
    words = nltk.word_tokenize(clean_essay)
    
    return sum(len(word) for word in words) / len(words)
def word_count(essay):
    
    clean_essay = re.sub(r'\W', ' ', essay)
    words = nltk.word_tokenize(clean_essay)
    
    return len(words)
def char_count(essay):
    
    clean_essay = re.sub(r'\s', '', str(essay).lower())
    
    return len(clean_essay)
def sent_count(essay):
    
    sentences = nltk.sent_tokenize(essay)
    
    return len(sentences)
# calculating number of lemmas per essay

def count_lemmas(essay):
    
    tokenized_sentences = tokenize(essay)      
    
    lemmas = []
    wordnet_lemmatizer = WordNetLemmatizer()
    
    for sentence in tokenized_sentences:
        tagged_tokens = nltk.pos_tag(sentence) 
        
        for token_tuple in tagged_tokens:
        
            pos_tag = token_tuple[1]
        
            if pos_tag.startswith('N'): 
                pos = wordnet.NOUN
                lemmas.append(wordnet_lemmatizer.lemmatize(token_tuple[0], pos))
            elif pos_tag.startswith('J'):
                pos = wordnet.ADJ
                lemmas.append(wordnet_lemmatizer.lemmatize(token_tuple[0], pos))
            elif pos_tag.startswith('V'):
                pos = wordnet.VERB
                lemmas.append(wordnet_lemmatizer.lemmatize(token_tuple[0], pos))
            elif pos_tag.startswith('R'):
                pos = wordnet.ADV
                lemmas.append(wordnet_lemmatizer.lemmatize(token_tuple[0], pos))
            else:
                pos = wordnet.NOUN
                lemmas.append(wordnet_lemmatizer.lemmatize(token_tuple[0], pos))
    
    lemma_count = len(set(lemmas))
    
    return lemma_count
def count_spell_error(essay):
    
    clean_essay = re.sub(r'\W', ' ', str(essay).lower())
    clean_essay = re.sub(r'[0-9]', '', clean_essay)
    
    #big.txt: It is a concatenation of public domain book excerpts from Project Gutenberg 
    #         and lists of most frequent words from Wiktionary and the British National Corpus.
    #         It contains about a million words.
    data = open('big.txt').read()
    
    words_ = re.findall('[a-z]+', data.lower())
    
    word_dict = collections.defaultdict(lambda: 0)
                       
    for word in words_:
        word_dict[word] += 1
                       
    clean_essay = re.sub(r'\W', ' ', str(essay).lower())
    clean_essay = re.sub(r'[0-9]', '', clean_essay)
                        
    mispell_count = 0
    
    words = clean_essay.split()
                        
    for word in words:
        if not word in word_dict:
            mispell_count += 1
    
    return mispell_count
def count_pos(essay):
    
    tokenized_sentences = tokenize(essay)
    
    noun_count = 0
    adj_count = 0
    verb_count = 0
    adv_count = 0
    
    for sentence in tokenized_sentences:
        tagged_tokens = nltk.pos_tag(sentence)
        
        for token_tuple in tagged_tokens:
            pos_tag = token_tuple[1]
        
            if pos_tag.startswith('N'): 
                noun_count += 1
            elif pos_tag.startswith('J'):
                adj_count += 1
            elif pos_tag.startswith('V'):
                verb_count += 1
            elif pos_tag.startswith('R'):
                adv_count += 1
            
    return noun_count, adj_count, verb_count, adv_count
def extract_features(data):
    
    features = data.copy()
    
    features['char_count'] = features['essay'].apply(char_count)
    
    features['word_count'] = features['essay'].apply(word_count)
    
    features['sent_count'] = features['essay'].apply(sent_count)
    
    features['avg_word_len'] = features['essay'].apply(avg_word_len)
    
    features['lemma_count'] = features['essay'].apply(count_lemmas)
    
    #features['spell_err_count'] = features['essay'].apply(count_spell_error)
    
    features['noun_count'], features['adj_count'], features['verb_count'], features['adv_count'] = zip(*features['essay'].map(count_pos))
    
    return features


def get_count_vectors(essays):
    
    vectorizer = CountVectorizer(max_features = 10000, ngram_range=(1, 3), stop_words='english')
    
    count_vectors = vectorizer.fit_transform(essays)
    
    feature_names = vectorizer.get_feature_names()
    
    return feature_names, count_vectors
def fit_count_vectors(essays,answer):
    vectorizer = CountVectorizer(max_features = 10000, ngram_range=(1, 3), stop_words='english')
    count_vectors = vectorizer.fit_transform(essays)
    text_vector= vectorizer.transform([answer])
    text_vector = text_vector.toarray()
    return text_vector
# def preprocessing(answer=None,isTest=False):
#     dataframe = pd.read_csv('http://127.0.0.1:8000/static/essays.csv', encoding = 'latin-1')
#     # getting relevant columns

#     data = dataframe[['essay_set','essay','domain1_score']].copy()
#     if(isTest):
#         text_vector = fit_count_vectors(data[data['essay_set'] == 1]['essay'],answer)
#         return(text_vector)
#     else:
#         feature_names_cv, count_vectors = get_count_vectors(data[data['essay_set'] == 1]['essay'])

#         X_cv = count_vectors.toarray()

#         y_cv = data[data['essay_set'] == 1]['domain1_score']
#         X_train, X_test, y_train, y_test = train_test_split(X_cv, y_cv, test_size = 0.3)
#         return (X_train,X_test,y_train,y_test)

##### NEw Features extraction Part
def preprocessing(answer=None,isTest=False):
    dataframe = pd.read_csv('static/essays.csv', encoding = 'latin-1')
    data = dataframe[['essay_set','essay','domain1_score']].copy()
    
    if(isTest):
        
        new_data = [[1,answer]]
        new_data = pd.DataFrame(new_data,columns=['essay_set','essay'])
        print("Extracting Features of given answer.....")
        features_set_answer = extract_features(new_data)
        print("Feature Extraction Complete....")
        print(features_set_answer)
        text_vector = fit_count_vectors(data[data['essay_set'] == 1]['essay'],answer)
        text_vector = np.concatenate((features_set_answer.iloc[:, 2:].to_numpy(),text_vector), axis = 1)
        print("return it....")
        return(text_vector)
    else:
        print("calculating Vectors : ")
        feature_names_cv, count_vectors = get_count_vectors(data[data['essay_set'] == 1]['essay'])
    
        X_cv = count_vectors.toarray()  # X without features only BOW
        y_cv = data[data['essay_set'] == 1]['domain1_score']
        print(y_cv.shape)


        print("Extracting Features for test.....")
        features_set1 = extract_features(data[data['essay_set'] == 1])
        print("Feature Extraction Complete....")
        print(features_set1)





        print("Creation of X and y")
        X = np.concatenate((features_set1.iloc[:, 3:].to_numpy(), X_cv), axis = 1)
        y = features_set1['domain1_score'].to_numpy()

        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.3)
        print(X_train.shape,X_test.shape,y_train.shape,y_test.shape)

        return (X_train,X_test,y_train,y_test)








