from nltk import ngrams
from ngram import NGram
sentence = 'this is a foo bar sentences and i want to ngramize it'
n = 2
sixgrams = ngrams(sentence.split(), n)
for grams in sixgrams:
    print grams

print NGram.compare('spa', 'spam')
