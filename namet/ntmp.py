#!/usr/bin/python
# -*- coding: UTF-8 -*-

import os
import re
import pickle

	
lisst={}			
f=open('./namecode.py','r')
fr=f.readlines()	
for fk in fr:
	patten1=re.compile(ur'[0-9]{4}',re.S)

	patten2=re.compile(ur'[\u4000-\u9fa5]',re.S)
	content2=re.findall(patten2,fk.decode('utf8'))
	content1=re.findall(patten1,fk.decode('utf8'))	
	#lisst[content2[0]]=content1[0]
	#print lisst
	if content2 :
		
		for k in content1:
		#	lisst[k]=content1[1]
			
			pass
		for j in content2:
			pass
		lisst[j]=k
	
lisst[u'\u5229']=8776

lisst[u'\u5fd7']=8768

print lisst[u'\u5fd7']
f.close()
f2=open('./namedict.data','w')
pickle.dump(lisst,f2)
f2.close()





