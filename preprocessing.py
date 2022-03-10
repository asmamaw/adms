
from __future__ import division
from nltk.stem import RegexpStemmer

import nltk, re, pprint

from nltk.corpus import stopwords
from nltk.stem import SnowballStemmer
from nltk.stem.porter import PorterStemmer
from nltk.stem import WordNetLemmatizer
from string import punctuation
from autocorrect import spell

snowball_stemmer = SnowballStemmer('english')
wordnet_lemmatizer = WordNetLemmatizer()

class Preprocess:
    def __int__(self):
        pass

    def autospell(self,text):
        """
        correct the spelling of the word.
        """
        spells = [spell(w) for w in (nltk.word_tokenize(text))]
        return " ".join(spells)

    def to_lower(self,text):
        """
        :param text:
        :return:
            Converted text to lower case as in, converting "Hello" to "hello" or "HELLO" to "hello".
        """
        return text.lower()

    def remove_numbers(self,text):
        """
        take string input and return a clean text without numbers.
        Use regex to discard the numbers.
        """
        output = ''.join(c for c in text if not c.isdigit())
        return output

    def remove_punct(self,text):
        """
        take string input and clean string without punctuations.
        use regex to remove the punctuations.
        """
        return ''.join(c for c in text if c not in punctuation)

    def remove_Tags(self,text):
        """
        take string input and clean string without tags.
        use regex to remove the html tags.
        """
        cleaned_text = re.sub('<[^<]+?>', '', text)
        return cleaned_text

    def sentence_tokenize(self,text):
        """
        take string input and return list of sentences.
        use nltk.sent_tokenize() to split the sentences.
        """
        sent_list = []
        for w in nltk.sent_tokenize(text):
            sent_list.append(w)
        return sent_list

    def word_tokenize(self,text):
        """
        :param text:
        :return: list of words
        """
        return [w for sent in nltk.sent_tokenize(text) for w in nltk.word_tokenize(sent)]

    def remove_stopwords(self,sentence):
        """
        removes all the stop words like "is,the,a, etc."
        """
        stop_words = stopwords.words('english')
        return ' '.join([w for w in nltk.word_tokenize(sentence) if not w in stop_words])


    def stem(self,word):
     regexp = r'^(.*?)(a|achuu|achuuf|adha|adhe|adhu|ama|amaa|aman|amne|amoo|amta|amtan|amte|amti|amtuu|amuuf|ani|e|eera|I|uu|uuf|neerra|aaf|aas|aat|aatu|uuttan|uutti|aa|naan|u|eet|eeti|ees|is|uufan|uufi|uufii|adhuu|adhee|amani|amanii|ame|amni|amu|amtu|amtani|amuu|amuudhaa|amuudhaaf|amuun|ullee|aatii|umsa|iisa|iinsa|wwan|lee|n|tiin|dhaa|dhaan|dhaaf|tii|an|i|een|ni|eeyyiiii|iin|iifi|iis|iif|iinis|iifuu|iifis|uma|umaa|umaanuu|umaaf|umaanis|umatti|umattuu|umattis|umaratti|umarattis|itti|ittis|ittuu|irraa|irraahuu|irraahis|irraan|irraanuu|irraanis|irratti|irrattis|irrattuu|illee|iinillee|umallee|umaafillee|umaanillee|ittillee|umattillee|irraahillee|irrattillee|irraanillee|oota|tu|dha|rra|tumoo|rratti|oota|oolii|oolee|tti|rraa|ummaa|ooma|ittii|icha|na|ne|nu|atini|achise|achisa|achisan|achiste|achisna|achistan|aniiru|anna|anne|annu|ata|atani|ate|atine|atte|attu|attan|atu|da|di|dani|de|du|eenya|nna|nnu|dhe|dhu|chisiise|chisiisa|hisisa|chisiisan|chisiste|chisisna|chisistan|chiise|chiisan|chiisna|chiistan|chiisne|iinsa|iisa|noo|ita|iti|itani|ite|itu|ina|inu|ine|ise|isa|isan|iste|isna|ifte|ifna|isise|isisa|isisan|isiste|isisna|isista|isistan|la|lu|le|lani|ra|ru|re|oofte|oofti|oofna|ooftan|oofta|ja|ju|je|jani)?$'
     stem, suffix = re.findall(regexp, word)[0]
     return stem

    def lemmatize(self,text):
        lemmatized_word = [wordnet_lemmatizer.lemmatize(word)for sent in nltk.sent_tokenize(text)for word in nltk.word_tokenize(sent)]
        return " ".join(lemmatized_word)


    def preprocess(self,text):
        lower_text = self.to_lower(text)
        sentence_tokens = self.sentence_tokenize(lower_text)
	   # tokens = sent_tokenize(text)
        word_list = []
        for each_sent in sentence_tokens:
            lemmatizzed_sent = self.lemmatize(each_sent)
            clean_text = self.remove_numbers(lemmatizzed_sent)
		    #clean_text = self.remove_numbers(each_sent)
            clean_text = self.remove_punct(clean_text)
            clean_text = self.remove_Tags(clean_text)
            clean_text = self.remove_stopwords(clean_text)
            word_tokens = self.word_tokenize(clean_text)
           # porter = PorterStemmer()
           # stemmed = [porter.stem(word) for word in word_tokens]
            stemmed = self.stem(word_tokens)
            for i in stemmed:
                word_list.append(i)
        return word_list
