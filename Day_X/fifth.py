# coding=gbk
#�ֳ�5�����һ�����б����棬90-100 80-90 70-80 60-70 59-0
#��ʼ����
student_list = [
    ["DDD",83],
    ["BB",95],
    ["AA",55],
    ["DD",85],
    ["EEE",61],
    ["CC",75],
    ["CCC",77],
    ["EE",65],
    ["AAA",51],
    ["BBB",92]
]
#�ṩ����ŵ�ѧ�����б�
coq_student_list = [
    [],# 0
    [],# 1
    [],# 2
    [],# 3
    [] # 4
]

#�༭ȡ�ڶ���ֵ�ĺ����Ĳο�����(һ��Ҫ�ǿɵ�������һ�Զࣩ)
def GetStudent_Sorce(inlist):
    return inlist[1]

def GetStudent_Name(inlist):
    return inlist[0]

def Putinto_Coqlist(level,gain):
    coq_student_list[level].append(gain)

#��һ��������
student_list.sort(key=GetStudent_Sorce,reverse=True)

#�ֿ���Ӧ��list
for student in student_list:
    if  GetStudent_Sorce(student) <= 100 and GetStudent_Sorce(student) >=90:
        Putinto_Coqlist(0,student)
    elif  GetStudent_Sorce(student) < 90 and GetStudent_Sorce(student) >=80:
        Putinto_Coqlist(1,student)
    elif GetStudent_Sorce(student) < 80 and GetStudent_Sorce(student) >= 70:
        Putinto_Coqlist(2,student)
    elif GetStudent_Sorce(student) < 70 and GetStudent_Sorce(student) >= 60:
        Putinto_Coqlist(3,student)
    else:
        Putinto_Coqlist(4,student)

print(coq_student_list)

