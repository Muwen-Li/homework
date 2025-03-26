import jieba
import re
from sklearn.manifold import TSNE
from gensim.models import Word2Vec
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties
import numpy as np
from collections import defaultdict

class TextAnalyzer:
    def __init__(self,textfile_path,modelfile_path=None,vector_size=100,window_size=10,stopwords_path=r'C:\Users\Lenovo\Desktop\python\homework\W2\cn_stopwords.txt'):
        self.textfile_path=textfile_path#待分析文本
        self.modelfile_path=modelfile_path#预训练模型文件
        self.vector_size=vector_size#向量长度
        self.window_size=window_size#窗口大小
        with open(stopwords_path, 'r', encoding='utf-8') as f:
            self.stopwords = set([line.strip() for line in f])
    def _pre_process(self):
        text_contents = []
        with open(self.textfile_path,'r',encoding='utf-8') as f:
            next(f)#跳过第一行
            for line in f:
                line=line.strip()
            # 跳过空行
                if not line:
                    continue    

                # 按制表符分割字段
                parts = line.split('\t')
                if len(parts) < 2:  # 确保至少有text字段
                    continue
                
                text_content = parts[1]  # 第二个字段是text
                text_contents.append(text_content)            
            
        process_weibos=[]
        punctuation = set([
            '，', '。', '！', '？', '、', '；', '：', '「', '」', '『', '』',
            '（', '）', '〔', '〕', '【', '】', '—', '…', '–', '．', '《', '》'
        ])
        for content in set(text_contents):
            # 清理URL
            cleaned = re.sub(r'http[s]?://\S+', '', content)
            # 清理@提及
            cleaned = re.sub(r'@[\w\-]+', '', cleaned)
            # 清理话题标签但保留文字
            cleaned = re.sub(r'#([^#]+)#', r'\1', cleaned)
            # 清理表情符号如[爱你]
            cleaned = re.sub(r'\[[^\]]+\]', '', cleaned)
            # 清理"我在:"等位置标记
            cleaned = re.sub(r'我(在这里|在):', '', cleaned)
            # 清理特殊符号和多余空格
            cleaned = re.sub(r'[^\w\u4e00-\u9fff]+', ' ', cleaned)
            cleaned = cleaned.strip()            
            if not cleaned:
                continue
        
            words=jieba.lcut(cleaned)
            filtered_words=[word for word in words if word not in punctuation and word not in self.stopwords and len(word)>1]

            if filtered_words:
                process_weibos.append(filtered_words)
        
        return process_weibos
    
    def print_process_weibos(self):
        return (self._pre_process())
    
    def _get_word2vec_model(self):
        sentence=self._pre_process()
        model=Word2Vec(sentence,vector_size=self.vector_size,window=self.window_size,min_count=1)
        model.save("word2vec.model")
        return model 
    
    def get_similar_words(self,word,topn):
        model=Word2Vec.load('word2vec.model')
        similar_words=model.wv.most_similar(word,topn=topn)
        return similar_words

similar_words=TextAnalyzer(r"C:\Users\Lenovo\Desktop\weibo.txt").get_similar_words('花朵',10)
print(similar_words)