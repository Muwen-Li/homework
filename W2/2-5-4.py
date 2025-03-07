import jieba
from collections import Counter
from wordcloud import WordCloud
import matplotlib.pyplot as plt

with open(r"C:\Users\Lenovo\Desktop\week2.txt",'r',encoding='utf-8') as file:
    lines=file.readlines()
words_list = [list(jieba.cut(line.strip())) for line in lines]
with open(r'C:\Users\Lenovo\Desktop\python\homework\W2\cn_stopwords.txt', 'r', encoding='utf-8') as file:
    stopwords = set([line.strip() for line in file])
filterd_words=[word for line in words_list for word in line if word not in stopwords and word.strip()!=' ']
bigrams=[(filterd_words[i],filterd_words[i+1]) for i in range(len(filterd_words)-1)]
#元素为元组的列表。

bigrams_count=Counter(bigrams)
for bigram,times in bigrams_count.most_common(10):
    print(f'{bigram}:{times}')

#转化成符合词云生成的格式。词频字典：键由元组转为一个字符串。
#字典推导式。键：' '.join(bigram)。将原本的元组元素用空格链接
bigram_freq = { ' '.join(bigram): freq for bigram, freq in bigrams_count.items() }

wordcloud = WordCloud(font_path='C:\\Windows\\Fonts\\simfang.ttf', width=800, height=400, background_color='white').generate_from_frequencies(bigram_freq)
plt.figure(figsize=(10, 5))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')
plt.show()

