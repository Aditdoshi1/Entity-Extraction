import re
import spacy
from spacy import displacy
from collections import Counter
import en_core_web_sm
import nltk
from nltk.tokenize import word_tokenize
from nltk.tag import pos_tag
from nltk.chunk import conlltags2tree, tree2conlltags
from pprint import pprint
from pathlib import Path
import xlwt 
from xlwt import Workbook 

##for filename in Path('').glob('**/*.txt'):
##    a = filename
nlp = en_core_web_sm.load()
with open('005.txt', 'r') as file:
    doc1 = file.read().replace('\n', '\n')

input = doc1
doc = nlp(doc1)
a=[(X.text, X.label_) for X in doc.ents]
output='{0}\n'.format(a)

phon = re.findall(r'\+?\[?\d\d*\s?[\d\d]?[?\d?\d?.?\d]?.\d{3}?\d?.?\d?.?\d{4}', doc1)
print('phone numbers')
for phone2 in phon:
    print(phone2)

print('Email')
emails = re.findall(r'[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z]+', doc1)
for email in emails:
    print(email)

domains = re.findall(r'[\w-]+\.+[\w-]+\.+[com|edu|net|co]+', doc1)
print('domain')
for domain in domains:
    print(domain)

addr=re.findall(r'\d\d\d?\d?\s?\w?\.?\-?([\w\,\s]+\d\d\d\d\d)|\s([a-zA-Z\,\s\-]+\d\d\d\-\d\d\d\d)|\s(\d\d[a-zA-Z\,\s]+\d\d)|\d\d\d\d?\s?([\w\,\-\s]+\d\d\d\d\d)', doc1)
print('addr=')
for address in addr:
    print(address)

a=[(X.text, X.label_) for X in doc.ents]
output='{0}\n'.format(a)
print('ORGANISATION')
org = re.compile(r"[(]+'+[a-zA-Z0-9.-]+'+, +'ORG'[)]") 
org1 = org.finditer(output)
for match3 in org1:
    print(match3)
print('Person=')
persons = re.findall(r"[a-zA-Z0-9.-]*\s*[a-zA-Z0-9.-]+'+, +'PERSON'", output)
['\n' if x=="PERSON" else x for x in persons]

for person1 in persons:
    print(person1)
    
### Workbook is created 
##wb = Workbook() 
##  
### add_sheet is used to create sheet. 
##sheet1 = wb.add_sheet('Sheet 1') 
##  
##sheet1.write(1, 0, 'a')
##wb.save('xlwt example.xls') 


file.close()

