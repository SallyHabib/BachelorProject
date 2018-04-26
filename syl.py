import numpy as np
import nltk
import glob
import os
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.cluster import KMeans
from scipy.cluster.vq import whiten
import csv
import string
from nltk.corpus import stopwords
from sklearn.feature_extraction import text
from nltk.stem.porter import PorterStemmer
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import TweetTokenizer
from nltk import pos_tag
from nltk.corpus import wordnet


# import sys  
# reload(sys)  # Reload does the trick!
# sys.setdefaultencoding('utf-8')
# print(sys.getdefaultencoding())
# stop_words = text.ENGLISH_STOP_WORDS.union(["xD","xd","XD"])
# words = [word.lower() for word in words if
#             not word in set(stopwords.words('english')) and not word.isdigit()]
# stop_words.append('.')
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
    lemmatiser = WordNetLemmatizer()
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
    words2 = [word for word in words if
            not word in exclude]
    words_tag = dict(pos_tag(words))
    words = [word.lower() for word in words2 if
            not word in nltk.corpus.stopwords.words('english') and not word.isdigit()]
    # print(words)
    words = [lima(word, words) for word in words]
    # print(words)
    words = ' '.join(words)
    # print(words)
    return words

stopwords = stopwords.words('english')
stopwords.append('.')
# stopwords.union('sally')
# operators = set(('sally'))
# stop = set(nltk.corpus.stopwords.words('english')) + operators
# print(stopwords)
sentence_tokenizer = nltk.data.load('tokenizers/punkt/english.pickle')
word_tokenizer = nltk.tokenize.RegexpTokenizer(r'\w+')
chapters=[]
with open('user_posts_1641812829207516.csv') as File:
    tfidfReader = csv.reader(File)
    for row in tfidfReader:
        chapters.append(clean(row[0]).encode('utf-8'))
num_chapters = len(chapters)
fvs_lexical = np.zeros((len(chapters), 3), np.float64)
fvs_punct = np.zeros((len(chapters), 3), np.float64)
i=1
    
for e, ch_text in enumerate(chapters):
    ch_text = unicode(ch_text, errors='ignore')

    # note: the nltk.word_tokenize includes punctuation
    # print(ch_text)
    if(ch_text):
        # ch_text.encode('utf-8')
        tokens = nltk.word_tokenize(ch_text.lower())
        words = word_tokenizer.tokenize(ch_text.lower())
        words=[word for word in words if
         not word in stopwords]
        sentences = sentence_tokenizer.tokenize(ch_text)
        if(words):
            vocab = set(words)
            # print(i)
            words_per_sentence = np.array([len(word_tokenizer.tokenize(s))
                                        for s in sentences])
            # print('w',words_per_sentence)
            # average number of words per sentence
            fvs_lexical[e, 0] = words_per_sentence.mean()
            # sentence length variation
            fvs_lexical[e, 1] = words_per_sentence.std()
            # Lexical diversity
            fvs_lexical[e, 2] = len(vocab) / float(len(words))
        
            # Commas per sentence
            fvs_punct[e, 0] = tokens.count(',') / float(len(sentences))
            # Semicolons per sentence
            fvs_punct[e, 1] = tokens.count(';') / float(len(sentences))
            # Colons per sentence
            fvs_punct[e, 2] = tokens.count(':') / float(len(sentences))
    i+=1
 
# apply whitening to decorrelate the features
# Before running k-means, it is beneficial to rescale each feature dimension of the observation set with whitening.
#  Each feature is divided by its standard deviation across all observations to give it unit variance.
print(fvs_lexical)
fvs_lexical = whiten(fvs_lexical)
fvs_punct = whiten(fvs_punct)