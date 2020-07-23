# -*- coding: utf-8 -*-
from ZipFile import ZipFile as z
import os
import datetime as t
info="""
===============!!!======!!=================|
|NAME:ZipBrute.                            |
|AUTHOR:AGBOOLA OLAMIDIPUPO.               |
|EMAIL:dipoagboola2019@gmail.com.          |
|FACEBOOK:Olamidipupo favor.               |
|GITHUB:olamidipupo-favor.                 |
|WEBSITE:http://dipogeek.000webhostapp.com.| 
|©Agboola Olamidipupo 2020.                |
|DISCLAIMER:USE AT YOUR OWN RISK.          |
|NOTE:TO USE ON A NON ANDROID, ADD AN INV- |
|ERTED COMMA TO THE SECOND LINE AFTER THIS | 
|LINE.                                     |
=============!!===!!!======================|"""
print(info)
st=t.datetime.now()
os.chdir('/storage/emulated/0/sl4a/scripts')
dir = str(raw_input('\n\n DIR?  => '))
file = str(raw_input('\n\n WORDLIST? =>'))
zip = str(raw_input('\n\n ZIP? => '))
zi = z(zip)
keywords = []
if (os.getcwd() == dir or dir == ""):
    files = open(file, 'rb')
    for i in files:
         f = i.replace('\n','')
         keywords.append(f)
    print("=>TESTING [+]" + str(len(keywords)))
else:
   os.chdir(dir)
   files = open(file, 'rb')
   for i in files:
       f=i.replace('\n','')
       keywords.append(f)
p=len(keywords)
tested=0
for i in keywords :
    tested+=1
    try:
        j=zi.extractall(pwd=i)
    except :
        continue 
    else:
        print(str(((tested/p)*100)) + "%")
        l=t.datetime.now()
        print ("password for '" +zip + "' Cracked => " + str(i).decode().title() + "  After {0} hours. ".format(l-st))
        exit(0)
print("=>[-]PASSWORD NOT FOUND KINDLY TRY ANOTHER WORDLIST")
