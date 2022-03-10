from __future__ import division
import bs4 as bs
import urllib.request
import re
import nltk
from gensim.models import Word2Vec
import multiprocessing
from sklearn.decomposition import PCA
from matplotlib import pyplot
import csv

def stem(word):
    regexp = r'^(.*?)(a|achuu|achuuf|adha|adhe|adhu|ama|amaa|aman|amne|amoo|amta|amtan|amte|amti|amtuu|amuuf|ani|e|eera|I|uu|uuf|neerra|aaf|aas|aat|aatu|uuttan|uutti|aa|naan|u|eet|eeti|ees|is|uufan|uufi|uufii|adhuu|adhee|amani|amanii|ame|amni|amu|amtu|amtani|amuu|amuudhaa|amuudhaaf|amuun|ullee|aatii|umsa|iisa|iinsa|wwan|lee|n|tiin|dhaa|dhaan|dhaaf|tii|an|i|een|ni|eeyyiiii|iin|iifi|iis|iif|iinis|iifuu|iifis|uma|umaa|umaanuu|umaaf|umaanis|umatti|umattuu|umattis|umaratti|umarattis|itti|ittis|ittuu|irraa|irraahuu|irraahis|irraan|irraanuu|irraanis|irratti|irrattis|irrattuu|illee|iinillee|umallee|umaafillee|umaanillee|ittillee|umattillee|irraahillee|irrattillee|irraanillee|oota|tu|dha|rra|tumoo|rratti|oota|oolii|oolee|tti|rraa|ummaa|ooma|ittii|icha|na|ne|nu|atini|achise|achisa|achisan|achiste|achisna|achistan|aniiru|anna|anne|annu|ata|atani|ate|atine|atte|attu|attan|atu|da|di|dani|de|du|eenya|nna|nnu|dhe|dhu|chisiise|chisiisa|hisisa|chisiisan|chisiste|chisisna|chisistan|chiise|chiisan|chiisna|chiistan|chiisne|iinsa|iisa|noo|ita|iti|itani|ite|itu|ina|inu|ine|ise|isa|isan|iste|isna|ifte|ifna|isise|isisa|isisan|isiste|isisna|isista|isistan|la|lu|le|lani|ra|ru|re|oofte|oofti|oofna|ooftan|oofta|ja|ju|je|jani)?$'
    stem, suffix = re.findall(regexp, word)[0]
   # return (" ").join(stem)
    return stem
def POS(word):
 for nsuffix in ['wwan', 'lee', 'n', 'tiin', 'dhaa', 'dhaan', 'dhaaf', 'tii', 'ota', 'oota', 'olee', 'olii', 'an', 'i', 'een', 'ni', 'a', 'eeyyii', 'ii', 'iin', 'iifi', 'iis', 'iif', 'iinis', 'iifuu', 'iifis', 'uma', 'umaa', 'umaanuu', 'umaaf',
'umaanis', 'umatti', 'umattuu', 'umattis', 'umaratti', 'umarattis', 'itti', 'ittis', 'ittuu', 'irraa', 
'irraahuu', 'irraahis', 'irraan', 'irraanuu', 'irraanis', 'irratti', 'irrattis', 'irrattuu', 'illee', 'iinillee',
'umallee', 'umaafillee', 'umaanillee', 'ittillee', 'umattillee', 'irraahillee', 'irrattillee', 
'irraanillee', 'tu', 'dhaan', 'dha', 'rra', 'dhaaf', 'tumoo', 'rratti', 'rraa', 'ummaa', 'ooma', 'ittii', 'icha' ]:
  if word.endswith(nsuffix):
      pos = 'Maqaa'
      break
      #print(word + ":", pos[word])
   #return word[:-len(suffix)]
 for vsuffix in ['na', 'ne', 'nu', 'atini', 'achise', 'achisa', 'achisan', 'achiste', 'achisna', 'achistan', 'aniiru', 'anna', 'anne', 'annu',
'ata', 'atani', 'ate', 'atine', 'atte', 'attu', 'attan', 'atu', 'da', 'di', 'dani', 'de', 'du', 'eenya', 'nna', 'nnu', 'dha', 'dhe', 'dhu', 'chisiise', 'chisiisa', 'chisisa', 'chisiisan', 'chisiste', 
'chisisna', 'chisistan', 'chiise', 'chiisan', 'chiisna', 'chiistan', 'chiisne', 'iinsa', 'iisa', 'noo', 'ita', 'iti', 'itani', 'ite','itu', 'ina', 'inu', 'ine', 'ise', 'isa', 'isan', 'iste', 'isna', 'ifte', 
'ifna', 'isise', 'isisa', 'isisan', 'isiste', 'isisna', 'isista', 'isistan', 'la', 'lu', 'le', 'lani', 'ra', 'ru', 're', 'oofte', 'oofti', 'oofna', 'ooftan', 'oofta', 'a','achuu',
'achuuf', 'adha', 'adhe', 'adhu', 'ama', 'amaa', 'aman', 'amne', 'amoo', 'amta', 'amtan', 'amte', 
'amti', 'amtuu', 'amuuf', 'ani', 'e', 'eera', 'I','uu', 'uuf', 'neerra', 'aaf', 'aas', 'aat', 'aatu', 'uuttan', 
'uutti', 'aa', 'naan', 'u', 'eet', 'eeti', 'ees', 'is', 'uufan', 'uufi', 'uufii', 'adhuu', 'adhee', 'amani', 
'amanii', 'ame', 'amni', 'amu', 'amtu', 'amtani', 'amuu', 'hin', 'amuudhaa', 'amuudhaaf', 'amuun', 
'ullee', 'aatii', 'umsa', 'iisa', 'iinsa']:
  if word.endswith(vsuffix):
    #pos = {word: 'v'}
    pos = 'Xumura'
    break
 print(word + ":", pos)
#scrapped_data = urllib.request.urlopen('https://www.bbc.com/afaanoromoo/oduu-59390553')
f = open("Afaan_OromoText.txt")

#article = scrapped_data .read()
article = f .read()

parsed_article = bs.BeautifulSoup(article,'lxml')

paragraphs = parsed_article.find_all('p')

article_text = ""

for p in paragraphs:
    article_text += p.text
    
    # Cleaing the text
processed_article = article_text.lower()
processed_article = re.sub('[^a-zA-Z]', ' ', processed_article )
processed_article = re.sub(r'\s+', ' ', processed_article)

# Preparing the dataset
all_sentences = nltk.sent_tokenize(processed_article)

all_words = [nltk.word_tokenize(sent) for sent in all_sentences]

# Removing Stop Words
f=open("stop.txt")
my_stopwords=f.read()
f.close()
for i in range(len(all_words)):
    all_words[i] = [w for w in all_words[i] if w not in my_stopwords]
    cores = multiprocessing.cpu_count() # Count the number of cores in a computer
    word2vec = Word2Vec(all_words, min_count=2,window=5,
                     vector_size=100,
                     sample=6e-5, 
                     alpha=0.03, 
                     min_alpha=0.0007, 
                     negative=20,
                     workers=cores-1)
    #w2v_model.build_vocab(all_words, progress_per=10000)
   
    print(word2vec)
    # summarize vocabulary
    words = list(word2vec.wv.index_to_key)
    vocabulary = word2vec.wv.index_to_key
print(vocabulary[:200])
#print(words)
#for i in range(len(all_words)):
 #vec = [word2vec.wv[v] for v in all_words[i]]
 #print(all_words[i] +":", vec[i])
v1 = word2vec.wv['gurguddaafi']
#print(word2vec)
# save model
word2vec.save('model.bin')
word = input('search word:')
search_terms = word.split()
#search_terms = search_terms+'\n'
#with open('Afaanoromosysnset.csv') as csv_file:
cs = open('Afaanoromosysnset.csv')
csv_read = csv.reader(cs, delimiter=',')
  
line_count = 0
	    
  
       

           # stemd = stem(search_terms)

for row in csv_read:
    
    if line_count == 0:
             print(f"\t{', '.join(row)}")
             line_count += 1
    

    if any([term in row[line_count] for term in search_terms]):
               print(row)
               
            
               break
              # print(row[line_count])
else:
    # load model
   new_model = Word2Vec.load('model.bin')

   sim_words = new_model.wv.most_similar(search_terms)
   POS(search_terms[0])
   print(sim_words)
#   word2vec.accuracy(new_model)
  # dissimlar_words = new_model.doesnt_match(search_terms.split())
   #print(dissimlar_words)
  
#sim_words = word2vec.wv.most_similar('gurguddaafi')
#print(sim_words)
"""X = word2vec.wv.index_to_key
pca = PCA(n_components=2)
result = pca.fit_transform(X)
# create a scatter plot of the projection
pyplot.scatter(result[:, 0], result[:, 1])
words = list(word2vec.wv.index_to_key)
for i, word in enumerate(words):
	pyplot.annotate(word, xy=(result[i, 0], result[i, 1]))
pyplot.show()
"""
