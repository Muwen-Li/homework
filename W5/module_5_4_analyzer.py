import jieba
import re
from sklearn.manifold import TSNE
from gensim.models import Word2Vec
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties
import numpy as np
from gensim.models import KeyedVectors

class TextAnalyzer:
    def __init__(self,textfile_path,modelfile_path=None,vector_size=300,window_size=5,stopwords_path=r'C:\Users\Lenovo\Desktop\python\homework\W2\cn_stopwords.txt'):
        self.textfile_path=textfile_path#待分析文本
        self.modelfile_path=modelfile_path#预训练模型文件
        self.vector_size=vector_size#向量长度
        self.window_size=window_size#窗口大小
        self.model=None
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
        pretrained_path = r"C:\Users\Lenovo\Desktop\cc.zh.300.vec"  # 预训练模型路径
        pretrained_vectors = KeyedVectors.load_word2vec_format(pretrained_path, binary=False,unicode_errors="ignore")
        model=Word2Vec(vector_size=300,window=self.window_size,min_count=1,sg=1,epochs=20,workers=4)
        model.build_vocab(sentence)
        model.wv.vectors_lockf = np.ones(len(model.wv.key_to_index), dtype=np.float32)
        model.wv.intersect_word2vec_format(pretrained_path,lockf=1.0,binary=False,encoding='utf-8')       
        # 继续训练（微调）
        model.train(sentence,total_examples=model.corpus_count,epochs=model.epochs)
        model.save("word2vec.model")
        self.model=model
        return model 
    
    def get_similar_words(self,word,topn):
        model=self.model
        similar_words=model.wv.most_similar(word,topn=topn)
        return similar_words
    
    def expand_emotion_lexicon(self,original_lexion_path):
        emotions=['anger','disgust','fear','sadness','joy']
        original_lexicon={}
        for emotion in emotions:
            path=f'{"C:\\Users\\Lenovo\\Desktop\\emotion_lexicon (1)\\emotion_lexicon"}/{emotion}.txt'
            with open(path,'r',encoding='utf-8') as f:
                words=f.read().splitlines()
            for word in words:
                if word not in original_lexicon:
                    original_lexicon[word] = emotion
        
        expanded_lexicon=original_lexicon.copy()
        model=self.model
        for word in original_lexicon:
            if word in model.wv.key_to_index:
                similar_words=model.wv.most_similar(word,topn=5)
                for similar_word in similar_words:
                    if similar_word not in expanded_lexicon:
                        expanded_lexicon[similar_word]=original_lexicon[word]
        
        return expanded_lexicon

    
    def vis_word_tsne(self,target_word,topn=10):
        model=self.model
        most_similar=model.wv.most_similar(target_word,topn)
        least_similar = model.wv.most_similar(negative=target_word, topn=10)
        # 将最相关和最不相关的词汇向量合并为一个数组
        vectors = np.array([model.wv[word] for word, similarity in most_similar + least_similar])
        print(vectors.shape)
        words = [word for word, similarity in most_similar + least_similar]
        tsne=TSNE(n_components=2,perplexity=15)
        vectors_tsne=tsne.fit_transform(vectors)
    # 可视化降维后的词向量
        fig,ax=plt.subplots()
        ax.set_title(target_word,fontproperties='SimHei')
        ax.scatter(vectors_tsne[:10,0],vectors_tsne[:10,1],color='blue',label='most_simi')
        ax.scatter(vectors_tsne[10:,0],vectors_tsne[10:,1],color='red',label='least_simi')
        ax.legend()

        for i,word in enumerate(words):
            ax.annotate(word,(vectors_tsne[i,0],vectors_tsne[i,1]),fontproperties='SimHei')

        plt.show()


analyzer = TextAnalyzer(textfile_path=r"c:\Users\Lenovo\Desktop\weibo.txt",stopwords_path=r"C:\Users\Lenovo\Desktop\python\homework\W2\cn_stopwords.txt")
model = analyzer._get_word2vec_model() 
analyzer.vis_word_tsne('花朵')


