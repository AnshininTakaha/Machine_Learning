
# coding=gbk
import random
import string

#��ȡ��Ӧ���ַ���
alphabet = string.ascii_uppercase
number = string.digits
Car_numstore = []
Choose_time = 3
#��ϳ�Ϊһ���б�
msglist = list(alphabet + number)

#�ַ���msglist
for x in msglist:
    x = str(x)
# print(msglist)

#��ȡ���5��Ԫ����ɳ��ƺ�
for i in range(20):

    CarFrontlist = random.choice(alphabet)
    Carbacklist = random.sample(msglist,5)
    CarF = "".join(CarFrontlist)
    CarB = "".join(Carbacklist)

    #��ӵ��б�����ȥ
    CarfullNumber = f"��{CarF}.{CarB}"
    Car_numstore.append(CarfullNumber)
    print(CarfullNumber)
    i+=1

while Choose_time:
    choose = input("����������Ҫѡ��ĺ��룺 ").strip() #ȥ������Ŀո�
    if choose in Car_numstore:
        print('ѡ��ɹ�')
        exit('ף�����')
    else:
        print("������ĳ��������⣬����������")
        Choose_time-=1

