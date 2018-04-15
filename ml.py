from sklearn.feature_extraction.text import TfidfVectorizer
import numpy
import scipy
import csv
#corpus = ["This is very strange",
#          "This is very nice"]
corpus = []
with open('user_likes_1641812829207516') as File:
    tfidfReader = csv.reader(File)
    for row in tfidfReader:
        #print("l")
        corpus.append((row[0]))

vectorizer = TfidfVectorizer(min_df=1)
vectorizer.stop_words='english'
X = vectorizer.fit_transform(corpus)
idf = vectorizer.idf_
print(X)
print(vectorizer.vocabulary_)
#print dict(zip(vectorizer.get_feature_names(), idf))

# list of text documents
text = ["The quick brown fox jumped over the lazy dog.",
		"The dog.",
		"The fox"]
# create the transform  
vectorizer = TfidfVectorizer()
# tokenize and build vocab
vectorizer.fit(text)
# summarize
# print(vectorizer.vocabulary_)
# print(vectorizer.idf_)
# encode document
vector = vectorizer.transform([text[0]])
# summarize encoded vector
# print(vector.shape)
# print(vector.toarray())