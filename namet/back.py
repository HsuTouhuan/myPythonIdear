#coding: utf8



import pickle
import random
import re

answ={'0':'你们注定是天生一对你们有着共同的爱好，性格也非常相投，品味一致。如此的默契，让身边的朋友都非常羡慕。但是没办法，谁让你们连姓名的笔画都是一样的呢！','1':'一见钟情，两情相悦你们在见到彼此第一眼的时候就被对方深深的吸引了，都爱上了对方，你们发誓要永远的在一起。她崇拜他，她也令他十分着迷，你们像磁铁一样相互吸引.','2':'执子之手，与子携老你们就是传说中的夫妻相，怎么看怎么般配。','3':'欢喜冤家，分分合合前世的你们是冤家，今生在一起是爱人，你们的感情分分合合，不过你们最后还是会在一起恩爱到老的。','4':'风雨之后，亮丽彩虹你们都受过感情的伤害，都是感性的人，这样的你们更容易靠近，你们会相互治愈，慢慢的爱情也就圆满了。','5':'日久生情，顺理成章朝九晚五的生活让你们发生了办公室恋情，你们互相了解，产生好感，在一起是顺理成章的事情，在偷看一眼你们都会觉得很幸福。'}



def ifname(name):
	mp=name
	mp2=[]
	for j in mp:
		mp2.append(j)
	if mp2.count(u'+')!=1:
		return u'请输入"姓名1+姓名2"'
	mp2.remove(u'+')
	mpk=''.join(mp2)
	patten2=re.compile(ur'[^\u4e00-\u9fa5]',re.S)
	content2=re.findall(patten2,mpk)
	if content2:
		return u'请输入正确的姓名'
	return name

f=open('./namedict.data')
nameDict=pickle.load(f)
f.close()
mp=u'金那+韩梅梅'

mpc=ifname(mp)

mp2=[]
print mp
for j in mp:
	mp2.append(j)
print mp2


if nameDict.get(mp2[-1]) and nameDict.get(mp2[1]):
	pass
	
elif not nameDict.get(mp2[-1]):
	nameDict[mp2[-1]]=random.randint(1234,9999)
elif not nameDict.get(mp2[1]):
	nameDict[mp2[1]]=random.randint(1111,9999)
	
f2=open('./namedict.data','w')
pickle.dump(nameDict,f2)
f2.close()

a1=nameDict.get(mp2[-1])
a2=nameDict.get(mp2[1])
#num=(nameDict.get(mp2[-1])+nameDict.get(mp2[1]))
print answ[str((int(a1)+int(a2))%6)]

