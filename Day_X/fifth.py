# coding=gbk
#分成5组存在一个大列表里面，90-100 80-90 70-80 60-70 59-0
#初始条件
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
#提供最后存放的学生的列表
coq_student_list = [
    [],# 0
    [],# 1
    [],# 2
    [],# 3
    [] # 4
]

#编辑取第二个值的函数的参考对象(一定要是可迭代对象（一对多）)
def GetStudent_Sorce(inlist):
    return inlist[1]

def GetStudent_Name(inlist):
    return inlist[0]

def Putinto_Coqlist(level,gain):
    coq_student_list[level].append(gain)

#第一步，排序
student_list.sort(key=GetStudent_Sorce,reverse=True)

#分开对应的list
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

