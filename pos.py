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


 # print(pos, [1])
# print word + ":", pos[word]
#return word
POS('teessuu')