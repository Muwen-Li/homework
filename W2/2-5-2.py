import jieba
from collections import Counter
from wordcloud import WordCloud
import matplotlib.pyplot as plt

# 加载停用词表
def load_stopwords(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        stopwords = set([line.strip() for line in file])
    return stopwords

# 分词并统计词频
def word_frequency(text, stopwords):
    words = jieba.lcut(text)#精确模式下的分词结果
    filtered_words = [word for word in words if word not in stopwords and word.strip() != '']
    #列表推导式：将文本的分词用停词表过滤
    word_count = Counter(filtered_words)
    return word_count

with open(r"C:\Users\Lenovo\Desktop\week2.txt",'r',encoding='utf-8') as file:
    text=file.read()

# 加载停用词表
stopwords = load_stopwords(r'C:\Users\Lenovo\Desktop\python\homework\W2\cn_stopwords.txt')

# 进行词频分析
word_count = word_frequency(text, stopwords)#生成一个词典

# 输出词频排序结果
common_words=sorted(word_count.items(),key=lambda x:x[1],reverse=True)
for i in range(10):
    print(common_words[i][0])

#创建词云
fpath = 'C:\\Windows\\Fonts\\simfang.ttf'
wd = WordCloud(font_path=fpath)
wd.fit_words(word_count)
#wd.to_file('./wd.png')
plt.imshow(wd)
plt.axis('off')
plt.show()