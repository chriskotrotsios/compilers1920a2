import re

def func1(m):
  if (m.group(0)=='&lt;'):
    return '<'
  elif (m.group(0)=='&amp;'):
    return '&'
  elif (m.group(0)=='&gt;'):
    return '>'
  else:
    return ' '	

rexp1 = re.compile('<title>(.+?)</title>')	
rexp2 = re.compile('<!--.*?-->',re.DOTALL)
rexp3 = re.compile(r'<(script|style).*?>.*?</(script|style)>',re.DOTALL)
rexp4 = re.compile(r'<a.+?href="(.*?)".*?>(.*?)</a>',re.DOTALL)
rexp5 = re.compile(r'&(amp|gt|lt|nbsp);')
rexp6 = re.compile(r'\s+')
rexptags1 = re.compile(r'<.+?>|</.+?>',re.DOTALL)
rexptags2 = re.compile(r'<.+?/>',re.DOTALL)


with open('testpage.txt','r') as fp:

  text = fp.read()

  m = rexp1.search(text)
  
  print(m.group(1))	

  text = rexp2.sub(' ',text)
  text = rexp3.sub(' ',text)

  for m in rexp4.finditer(text):
    print('{} {}'.format(m.group(1),m.group(2)))

  text = rexptags1.sub(' ',text)
  text = rexptags2.sub(' ',text)
  text = rexp5.sub(func1,text)
  text = rexp6.sub(' ',text)

  print(text)
