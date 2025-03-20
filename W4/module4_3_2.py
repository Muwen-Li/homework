import jieba
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer,TfidfVectorizer
from module4_3_1 import document_shopID_time

df=pd.read_csv('C:\\Users\\Lenovo\\Desktop\\week4.csv')
with open(r'C:\Users\Lenovo\Desktop\python\homework\W2\cn_stopwords.txt', 'r', encoding='utf-8') as file:
    stopwords = set([line.strip() for line in file])
stopwords = list(stopwords)

def doc_word_freq(shopID,time_unit,stopwords):
    documents=document_shopID_time(df,shopID,time_unit)
    document_texts = [time_docs for shop_docs in documents.values() for time_docs in shop_docs.values() ]
    document_texts = [" ".join(jieba.cut(text)) for text in document_texts]
    #{ID：{时间：评论}}
    count_vectorizer = CountVectorizer(stop_words=stopwords,min_df=2,max_features=10000)
    count_matrix=count_vectorizer.fit_transform(document_texts)
    feature_names = count_vectorizer.get_feature_names_out()
    count_feature_names=feature_names
    #使用 CountVectorizer 进行词频特征表示

    tfidf_vectorizer = TfidfVectorizer(stop_words=stopwords)
    tfidf_matrix=tfidf_vectorizer.fit_transform(document_texts)
    t_feature_names = tfidf_vectorizer.get_feature_names_out()
    tfidf_feature_names=t_feature_names
    # 使用 TfidfVectorizer 进行 TF-IDF 特征表示

    return count_matrix, count_vectorizer,feature_names


