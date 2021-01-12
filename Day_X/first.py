
# coding=gbk
import random
import string

#获取对应的字符串
alphabet = string.ascii_uppercase
number = string.digits
Car_numstore = []
Choose_time = 3
#组合成为一个列表
msglist = list(alphabet + number)

#字符化msglist
for x in msglist:
    x = str(x)
# print(msglist)

#获取随机5个元素组成车牌号
for i in range(20):

    CarFrontlist = random.choice(alphabet)
    Carbacklist = random.sample(msglist,5)
    CarF = "".join(CarFrontlist)
    CarB = "".join(Carbacklist)

    #添加到列表里面去
    CarfullNumber = f"京{CarF}.{CarB}"
    Car_numstore.append(CarfullNumber)
    print(CarfullNumber)
    i+=1

while Choose_time:
    choose = input("请输入你想要选择的号码： ").strip() #去掉多余的空格
    if choose in Car_numstore:
        print('选择成功')
        exit('祝你好运')
    else:
        print("你输入的车牌有问题，请重新输入")
        Choose_time-=1

