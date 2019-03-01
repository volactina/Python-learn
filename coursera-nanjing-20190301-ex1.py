'''
1. 使用以下语句存储一个字符串：

string = 'My moral standing is: 0.98765'

将其中的数字字符串转换成浮点数并输出。

（提示：可以使用find()方法和字符串切片或split()方法，
提取出字符串中冒号后面的部分，然后使用float函数，
将提取出来的字符串转换为浮点数）

'''

string = 'My moral standing is: 0.98765'
for str in string.split():
    try:
        if type(eval(str))==float:
            print(float(str))
    except:()

# 参考程序
# # -*- coding: utf-8 -*-
# """
# Substring taking
# @author: Dazhuang
# """
# string = 'My moral standing  is: 0.98765'
# moral_str = string.split(":")[1]
# result = float(moral_str)
# print(result)
