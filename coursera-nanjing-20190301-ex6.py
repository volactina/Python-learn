'''
6. 请用随机函数产生500行1-100之间的随机整数存入文件random.txt中，
编程寻找这些整数的众数并输出，
众数即为一组数中出现最多的数。
'''

import random
import numpy as np
from scipy import stats

with open("random.txt",'w') as f:
    for i in range(500):
        f.writelines(str(random.randint(1,100))+"\n")
    f.close()

with open("random.txt",'r') as f:
    lst=f.readlines()
    for i in range(len(lst)):
        lst[i]=int(lst[i])
    print(stats.mode(lst))
    f.close()

# #-*-coding:utf-8-*-
# """
# @author: Dazhuang
# """
# import random
#
# with open('random.txt', 'w+') as fp:
#     for i in range(500):
#          fp.write(str(random.randint(1, 100)))
#          fp.write('\n')
#     fp.seek(0)
#     nums = fp.readlines()
# nums = [num.strip() for num in nums]
# setNums = set(nums)
# lst = [0] * 101
# for num in setNums:
#     c = nums.count(num)
#     lst[int(num)] = c
# for i in range(len(lst)):
#     if lst[i] == max(lst):
#         print(i)