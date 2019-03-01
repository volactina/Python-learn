'''
5. 从键盘输入整数n（1-9之间），对于1-100之间的整数删除包含n并且能被n整除的数，
例如如果n为6，则要删掉包含6的如6，16这样的数及是6的倍数的如12和18这样的数，
输出所有满足条件的数，要求每满10个数换行。

测试数据：

Enter the number: 6

屏幕输出：

1,2,3,4,5,7,8,9,10,11

13,14,15,17,19,20,21,22,23,25

27,28,29,31,32,33,34,35,37,38

39,40,41,43,44,45,47,49,50,51

52,53,55,57,58,59,70,71,73,74

75,77,79,80,81,82,83,85,87,88

89,91,92,93,94,95,97,98,99,100
'''

n=input("please input a number n to erase:")
cnt=0
print_str = ''
for i in range(1,101):
    if i%int(n)==0 or str(i).find(str(n))!=-1:
        continue
    cnt+=1
    print_str+=str(i)
    if(cnt==10):
        print('\n',print_str)
        cnt=0
        print_str = ''
    else:
        print_str+=','
if(len(print_str)>0):
    print(print_str)


# #-*-coding:utf-8-*-
# """
# @author: Dazhuang
# """
# n = int(input("Enter the number: "))
# count = 0
# new_str = ''
# print("The result string: ")
# for i in range(101):
#     s = str(i)
#     if i % n != 0 and s.find(str(n)) == -1:
#         new_str = new_str + s + ','
#         count += 1
#         if count % 10 == 0:
#             print(new_str[:-1])
#             new_str = ''
# if len(new_str) > 0:
#     print(new_str[:-1])