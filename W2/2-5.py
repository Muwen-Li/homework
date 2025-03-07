import jieba
import collections
from collections import Counter
with open(r"C:\Users\Lenovo\Desktop\week2.txt",'r',encoding='utf-8') as file:
    text=file.read()
word_list=jieba.cut(text)
wordlist=list(word_list)
tfreq=Counter(wordlist)
common_words=sorted(tfreq.items(),key=lambda x:x[1],reverse=True)
for i in range(10):
    print(common_words[i][0])