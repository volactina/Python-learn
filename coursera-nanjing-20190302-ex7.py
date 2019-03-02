maxlen=0
maxword=''
with open('article.txt','r') as f:
    lst=f.read()
    lst=lst.split()
    for words in lst:
        words=words.strip()
        words = words.replace('!', '')
        words = words.replace('?', '')
        words = words.replace(',', '')
        words = words.replace('.', '')
        words = words.replace('...', '')
        if(len(words)>maxlen):
            maxlen=len(words)
            maxword=words
    f.close()

print(maxword,maxlen)

# #-*-coding:utf-8-*-
# """
# @author: Dazhuang
# """
# with open('article.txt') as fp:
#     data = fp.read()
# words = data.split()
# lst = []
# for word in words:
#     if word[-3:] == '...':
#         word = word[:-3]
#         lst.append(word)
#     if word[-1] in ',.?!':
#         word = word[:-1]
#         lst.append(word)
# result = sorted(lst, key = len, reverse = True)
# print(result[0])
# m = len(result[0])
# # 最长单词可能不止一个
# for word in result[1:]:
#     n = len(word)
#     if n == m:
#         print(word)
#     else:
#         break