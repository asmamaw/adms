# -*- coding: utf-8 -*-
"""
Created on Tue Nov 30 19:35:10 2021

@author: hp
"""

from __future__ import division
import nltk
from gensim.models import Word2Vec
from nltk.tokenize import word_tokenize
import multiprocessing
from sklearn.decomposition import PCA
from matplotlib import pyplot
from nltk.stem import RegexpStemmer
import string
string.punctuation

import nltk, re, pprint
def remove_numbers(text):
    """
    take string input and return a clean text without numbers.
    Use regex to discard the numbers.
    """
    output = ''.join(c for c in text if not c.isdigit())
    return output

def remove_punctuation(text):
    no_punct=[words for words in text if words not in string.punctuation]
    words_wo_punct=''.join(no_punct)
    return words_wo_punct
def to_lower(self,text):
     """
     :param text:
     :return:
         Converted text to lower case as in, converting "Hello" to "hello" or "HELLO" to "hello".
     """
     return text.lower()

def stem(word):
    regexp = r'^(.*?)(a|achuu|achuuf|adha|adhe|adhu|ama|amaa|aman|amne|amoo|amta|amtan|amte|amti|amtuu|amuuf|ani|e|eera|I|uu|uuf|neerra|aaf|aas|aat|aatu|uuttan|uutti|aa|naan|u|eet|eeti|ees|is|uufan|uufi|uufii|adhuu|adhee|amani|amanii|ame|amni|amu|amtu|amtani|amuu|amuudhaa|amuudhaaf|amuun|ullee|aatii|umsa|iisa|iinsa|wwan|lee|n|tiin|dhaa|dhaan|dhaaf|tii|an|i|een|ni|eeyyiiii|iin|iifi|iis|iif|iinis|iifuu|iifis|uma|umaa|umaanuu|umaaf|umaanis|umatti|umattuu|umattis|umaratti|umarattis|itti|ittis|ittuu|irraa|irraahuu|irraahis|irraan|irraanuu|irraanis|irratti|irrattis|irrattuu|illee|iinillee|umallee|umaafillee|umaanillee|ittillee|umattillee|irraahillee|irrattillee|irraanillee|oota|tu|dha|rra|tumoo|rratti|oota|oolii|oolee|tti|rraa|ummaa|ooma|ittii|icha|na|ne|nu|atini|achise|achisa|achisan|achiste|achisna|achistan|aniiru|anna|anne|annu|ata|atani|ate|atine|atte|attu|attan|atu|da|di|dani|de|du|eenya|nna|nnu|dhe|dhu|chisiise|chisiisa|hisisa|chisiisan|chisiste|chisisna|chisistan|chiise|chiisan|chiisna|chiistan|chiisne|iinsa|iisa|noo|ita|iti|itani|ite|itu|ina|inu|ine|ise|isa|isan|iste|isna|ifte|ifna|isise|isisa|isisan|isiste|isisna|isista|isistan|la|lu|le|lani|ra|ru|re|oofte|oofti|oofna|ooftan|oofta|ja|ju|je|jani)?$'
    stem, suffix = re.findall(regexp, word)[0]
   # return (" ").join(stem)
    return stem
raw = """Labsii Walii-gala Mirgoota Namummaa
Murtoo Wal-ga'ii Walii-gala kan Dhaabbata Waldaa Mootummootaatiin qabxii 217 A (iii) jalatti Mudde baatii 10 bara 1948 itti Akka Murteeffamee Ragga'ee Labsametti.
SEENSA
Ulfinni fi wal-qixxummaan ilmoo namaa kan uummattoota hundaa akka ifatti kabajamu gochuun bu'ura bilisummaa haqaa fi nageenya addunyaa waan ta'eef;
Mirga namummaa irra ijjechuun yookaan tuffachuun yeroo hunda jeequmsa badiisa fidu uumee uummata kan dheekamsiisu waan ta'eef akkasumas addunyaa haaraa kan uummanni ishee wal-qixxummaadhaan bilisummaa yaadaa fi amantii argatanii yaaddoo fi dhaba irraa birmaduu ta'anii gammachuudhaan akka jiraatan gochuun hawwii fi fedha uummattoota addunyaa waan ta'eef;
Uummanni bulchiisa rooroo fi cunqursaa ofirra kuffisuuf humnaan akka hinfayyadamnetti yoo barbaachise mirgooti namummaa seeraan akka eegamu gochuun barbaachisaa waan ta'eef;
Biyyoota gidduutti walitti-dhufeenyi michumaa fi wal-jaalalaa akka dagaagu gochuun barbaachisaa waan ta'eef;
Miseens."""

f=open("stop.txt")
my_stopwords=f.read()
f.close()
def remove_mystopwords(sentence):
    tokens = word_tokenize(sentence)
    tokens_filtered= [word for word in tokens if not word in my_stopwords]
    return (" ").join(tokens_filtered)
ff = open("Afaan_OromoText.txt")
text = ff.read()
print(text[:100])
ttext = remove_numbers(text)
punc = remove_punctuation(ttext)
#tokens = nltk.word_tokenize(punc)
filtered_text = remove_mystopwords(punc)
#punc = remove_punctuation(filtered_text)
print(filtered_text[:1000])
#punc = remove_punctuation(filtered_text)
#tokens = nltk.word_tokenize(punc)
# Removing Stop Words
#tokenss = remove_mystopwords(text)
#t = [stem(t) for t in tokenss]
#print(tokenss[:100])
#[stem(t) for t in tokenss]
#print(t[:100])
tokens = nltk.word_tokenize(filtered_text)
t = [stem(t) for t in tokens]

#[stem(t) for t in tokens]
print(t[:200])
