import pickle
import pandas as pd
from module4_3_1 import document_shopID_time
from module4_3_2 import doc_word_freq
from module4_3_3 import lda_topic_analysis

df=pd.read_csv('C:\\Users\\Lenovo\\Desktop\\week4.csv')
with open(r'C:\Users\Lenovo\Desktop\python\homework\W2\cn_stopwords.txt', 'r', encoding='utf-8') as file:
    stopwords = set([line.strip() for line in file])
stopwords = list(stopwords)

documents=document_shopID_time(df,518986, 'year')
count_matrix, count_vectorizer,feature_names = doc_word_freq(518986, 'year', stopwords)
doc_topic_distribution = lda_topic_analysis(518986, 'year', stopwords, n_topics=5)

with open('lda_model.pkl', 'wb') as f:
    pickle.dump(doc_topic_distribution, f)  # 保存 LDA 模型的文档-主题分布

with open('count_matrix.pkl', 'wb') as f:
    pickle.dump(count_matrix, f)  # 保存词频矩阵

with open('feature_names.pkl', 'wb') as f:
    pickle.dump(feature_names, f)  # 保存特征名称

with open("count_vectorizer.pkl","wb") as f:
    pickle.dump(count_vectorizer,f)

with open('documents.pkl','wb') as f:
    pickle.dump(documents,f)