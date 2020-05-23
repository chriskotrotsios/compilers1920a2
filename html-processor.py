import re

#Δημιουργία της συνάρτησης για την μετατροπή των &gt; &amp; &lt; &nbsp; entities

def func1(m):
  if (m.group(0)=='&lt;'):
    return '<'
  elif (m.group(0)=='&amp;'):
    return '&'
  elif (m.group(0)=='&gt;'):
    return '>'
  else:
    return ' '	

#Κανονικές εκφράσεις  
  
rexp1 = re.compile('<title>(.+?)</title>')	                                 #Ερώτημα 1ο, εξαγωγή τίτλου
rexp2 = re.compile('<!--.*?-->',re.DOTALL)                                   #Ερώτημα 2ο, απαλοιφή σχόλιων
rexp3 = re.compile(r'<(script|style).*?>.*?</(script|style)>',re.DOTALL)     #Ερώτημα 3ο, απαλοιφή script και style
rexp4 = re.compile(r'<a.+?href="(.*?)".*?>(.*?)</a>',re.DOTALL)              #Ερώτημα 4ο, εξαγωγή συνδέσμων
rexp6 = re.compile(r'&(amp|gt|lt|nbsp);')                                    #Εξαγωγή των &gt; &amp; &lt; &nbsp; entities
rexp7 = re.compile(r'\s+')                                                   #Ερώτημα 7ο, εξαγωγή των whitespaces 
rexp5tags1 = re.compile(r'<.+?>|</.+?>',re.DOTALL)                           #Ερώτημα 5ο, εξαγωγή tags με < > </> μορφή
rexp5tags2 = re.compile(r'<.+?/>',re.DOTALL)                                 #Ερώτημα 5ο, εξαγωγή tags με </> self closing μορφή


with open('testpage.txt','r') as fp:           #Άνοιγμα αρχείου

  text = fp.read()       

  m = rexp1.search(text)
  
  print(m.group(1))	#Εκτύπωση τίτλου

  text = rexp2.sub(' ',text)    # Απαλοιφή σχολίων
  text = rexp3.sub(' ',text)    # Απαλοιφή script και style

  for m in rexp4.finditer(text):
    print('{} {}'.format(m.group(1),m.group(2)))    #Εκτύπωση των links

  text = rexp5tags1.sub(' ',text)  #Απαλοιφή <> </> tags
  text = rexp5tags2.sub(' ',text)  #Απαλοιφή </> self closing tags
  text = rexp6.sub(func1,text)     #Αλλαγή των &gt; &amp; &lt; &nbsp; entities
  text = rexp7.sub(' ',text)       #Αλλαγή πολλαπλών κενών σε ένα κενό

  print(text)
