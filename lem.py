from flask import Flask
from flask import request
import requests
import facebook
from pymongo import MongoClient
import json
import csv
import nltk
from nltk.corpus import wordnet
from nltk import pos_tag
from nltk import word_tokenize
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
from nltk.stem import  WordNetLemmatizer as wnl
from nltk.corpus import wordnet as wn
from nltk.tokenize import TweetTokenizer
import re
import string
import codecs
from sklearn.feature_extraction.text import TfidfVectorizer
import numpy
import scipy
import csv


def get_wordnet_pos(treebank_tag):

    if treebank_tag.startswith('J'):
        return wordnet.ADJ
    elif treebank_tag.startswith('V'):
        return wordnet.VERB
    elif treebank_tag.startswith('N'):
        return wordnet.NOUN
    elif treebank_tag.startswith('R'):
        return wordnet.ADV
    else:
        return  wordnet.NOUN


def lima(word, words):
    # print(word)
    lemmatiser = wnl()
    words_tag = dict(pos_tag(words))
    # print(wordnet.synsets(word))
    # print(get_wordnet_pos(words_tag.get(word)))
    # if word.isalpha() and wordnet.synsets(word):
    return  lemmatiser.lemmatize(word, get_wordnet_pos(words_tag.get(word)))
    # else:
    #     return word


def clean(words):
    # words = re.sub('[^a-zA-Z]', '', words.lower()).split()
    tknzr = TweetTokenizer()
    # tokenizer = RegexpTokenizer('\w+|\S+')
    # words=nltk.word_tokenize(words.lower())
    words = tknzr.tokenize(words)
    exclude = set(string.punctuation)
    words = [word for word in words if
            not word in exclude]
    words_tag = dict(pos_tag(words))
    words = [word.lower() for word in words if
            not word in set(stopwords.words('english')) and not word.isdigit()]
    #print(words)
    words = [lima(word, words) for word in words]
    #print(words)
    words = ' '.join(words)
    return words

    # 'groups.csv', 'w', newline=''
    #  lemmatiser.lemmatize(word, get_wordnet_pos(words_tag.get(word)))
    # words = re.sub('[^a-zA-Z]', 'pp', words.lower()).split()
corpus = []
with open('user_posts.csv') as File:
    spamreader = csv.reader(File)
    for row in spamreader:
        #print("l")
        corpus.append(clean(row[0]))
    #print(corpus)

vectorizer = TfidfVectorizer(min_df=3)
vectorizer.stop_words='english'
X = vectorizer.fit_transform(corpus)
idf = vectorizer.idf_
print(X)
print(vectorizer.vocabulary_)
#print dict(zip(vectorizer.get_feature_names(), idf))

