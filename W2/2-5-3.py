import jieba
import jieba.posseg as pseg #对文本进行分词和词性标注
from collections import Counter
from wordcloud import WordCloud
import matplotlib.pyplot as plt

with open(r"C:\Users\Lenovo\Desktop\week2.txt",'r',encoding='utf-8') as file:
    text=file.read()
with open(r'C:\Users\Lenovo\Desktop\python\homework\W2\cn_stopwords.txt', 'r', encoding='utf-8') as file:
    stopwords = set([line.strip() for line in file])   
words_type=pseg.lcut(text)
filtered_words_type=[(word, type) for word, type in words_type if word not in stopwords and word.strip() != '']

type_counter=Counter(type for word, type in filtered_words_type)#获得不同词性的词频而非单个词语的词频
for type,freq in type_counter.most_common(3):
    print(f"{type}: {freq}")

# 提取特定词性的词并生成词云
def generate_wordcloud(filtered_words_type, target_type):
    words = [word for word, type in filtered_words_type if type == target_type]
    text = ' '.join(words)
    wordcloud = WordCloud(font_path='C:\\Windows\\Fonts\\simfang.ttf', width=800, height=400, background_color='white').generate(text)
    plt.figure(figsize=(10, 5))
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis('off')
    plt.show()   

generate_wordcloud(filtered_words_type, 'v')