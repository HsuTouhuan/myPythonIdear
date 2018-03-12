
#coding:utf-8

import pickle
import random
import itchat
import re
# import全部消息类型
from itchat.content import *

ask=u'缘份配，性格配，门户配，星座配……现在最流行姓名配！恋爱向导，带你航向爱情海，不必媒人，不用八字，只要在一笔一划间，就能轻松配对！只要姓名配，不怕情敌追，从此不必伤脑筋琢磨，就能轻松找到你心目中完美的婚恋情人，谈一场像日剧般浪漫又完美的恋爱！(如果没有及时测试结果那一定是人太多啦，请再次发送！)'

answ={'0':u'你们注定是天生一对你们有着共同的爱好，性格也非常相投，品味一致。如此的默契，让身边的朋友都非常羡慕。但是没办法，就是这个样子啊！','1':u'一见钟情，两情相悦你们在见到彼此第一眼的时候就被对方深深的吸引了，都爱上了对方，你们发誓要永远的在一起。她崇拜他，她也令他十分着迷，你们像磁铁一样相互吸引.','2':u'执子之手，与子携老你们就是传说中的夫妻相，怎么看怎么般配。','3':u'欢喜冤家，分分合合前世的你们是冤家，今生在一起是爱人，你们的感情分分合合，不过你们最后还是会在一起恩爱到老的。','4':u'风雨之后，亮丽彩虹你们都受过感情的伤害，都是感性的人，这样的你们更容易靠近，你们会相互治愈，慢慢的爱情也就圆满了。','5':u'日久生情，顺理成章朝九晚五的生活让你们发生了办公室恋情，你们互相了解，产生好感，在一起是顺理成章的事情，在偷看一眼你们都会觉得很幸福。'}


f=open('./namedict.data')
nameDict=pickle.load(f)
f.close()


def ifname(name):
	mp=name
	mp2=[]
	for j in mp:
		mp2.append(j)
	if mp2.count(u'+')!=1:
		return '1'
	mp2.remove(u'+')
	mpk=''.join(mp2)
	patten2=re.compile(ur'[^\u4e00-\u9fa5]',re.S)
	content2=re.findall(patten2,mpk)
	if content2:
		return '2'
	return name
def answe(mp1):
	
	
	mp=ifname(mp1)
	
	if mp=='2':
		return u'请输入正确的姓名'
	if mp=='1':
		return u'请输入"姓名1+姓名2"'
		
	
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

	return  answ[str((int(a1)+int(a2))%6)]
#num=(nameDict.get(mp2[-1])+nameDict.get(mp2[1]))
# 处理文本类消息
# 包括文本、位置、名片、通知、分享
@itchat.msg_register([TEXT, MAP, CARD, NOTE, SHARING])
def text_reply(msg):
    # 微信里，每个用户和群聊，都使用很长的ID来区分
    # msg['FromUserName']就是发送者的ID
    # 将消息的类型和文本内容返回给发送者
   
    itchat.send(answe(msg['Text']), toUserName='filehelper')
    itchat.send( answe(msg['Text']), msg['FromUserName'])
    

@itchat.msg_register('Friends')
def add_friend(msg):
	itchat.add_friend(**msg['Text'])
	itchat.get_contract()
	itchat.send_msg(msg['RecommendInfo']['UserName'], 'Nice to meet you!')    
    
    
   

itchat.auto_login(enableCmdQR=False,hotReload=True)



itchat.send('Hello', toUserName='filehelper')
#'@de38485fc836cccba36e545e2450de5e525e5e3707665d039b0ee6c34ec35f55'
itchat.run()
