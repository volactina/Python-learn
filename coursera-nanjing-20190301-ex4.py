'''
4. 有一个咖啡列表['32Latte', '_Americano30', '/34Cappuccino', 'Mocha35']，
列表中每一个元素都是由咖啡名称、价格和一些其他非字母字符组成，
编写一个函数clean_list()处理此咖啡列表，处理后列表中只含咖啡名称，
并将此列表返回。__main__模块中初始化咖啡列表，调用clean_list()函数获得处理后的咖啡列表，
并利用zip()函数给咖啡名称进行编号后输出，输出形式如下：

1 Latte

2 Americano

3 Cappuccino

4 Mocha
'''

def clean_list(lst):
    for i in range(len(lst)):
        after=''
        for ch in lst[i]:
            if ch.isalpha():
                after+=ch
        lst[i]=after
    return lst

if __name__=="__main__":
    lst=['32Latte', '_Americano30', '/34Cappuccino', 'Mocha35']
    lst=clean_list(lst)
    for k,v in zip(range(1,len(lst)+1),lst):
        print(k,v)


# # -*- coding: utf-8 -*-
# """
# List processing
#
# @author: Dazhuang
# """
# def clean_list(lst):
#     cleaned_list = []
#     for item in lst:
#         for c in item:
#             if c.isalpha() != True:
#                  item = item.replace(c, '')
#         cleaned_list.append(item)
#     return cleaned_list
#
# if __name__ == "__main__":
#     coffee_list = ['32Latte', '_Americano30', '/34Cappuccino', 'Mocha35']
#     cleaned_list = clean_list(coffee_list)
#     for k,v in zip(range(1, len(cleaned_list)+1), cleaned_list):
#         print(k, v)