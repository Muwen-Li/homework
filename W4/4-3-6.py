import pandas as pd
import matplotlib.pyplot as plt
from sklearn.decomposition import LatentDirichletAllocation
import numpy as np
import pickle

with open('lda_model.pkl', 'rb') as f:
    doc_topic_distribution = pickle.load(f)
with open('count_matrix.pkl', 'rb') as f:
    count_matrix = pickle.load(f)
with open('feature_names.pkl', 'rb') as f:
    feature_names = pickle.load(f)
with open('count_vectorizer.pkl', 'rb') as f:
    count_vectorizer = pickle.load(f)
with open('documents.pkl', 'rb') as f:
    documents = pickle.load(f)

def convert_to_dataframe(documents):
    data = []
    for shopID, time_comments in documents.items():
        for time_unit, comment in time_comments.items():
            if isinstance(time_unit, tuple):  # 如果时间单位是元组（如 (year, month, day)）
                time_str = '-'.join(map(str, time_unit))
            else:  # 如果时间单位是单个值（如 year）
                data.append({'shopID': shopID,'time_unit': str(time_unit),'combined_comment': comment})
    df = pd.DataFrame(data)
    return df
   
documents_df=convert_to_dataframe(documents)  
print(documents_df.head(10))


# 将 doc_topic_distribution 添加到 DataFrame
documents_df['topic_distribution']=list(doc_topic_distribution)
documents_df['time_period'] = documents_df['time_unit']
topic_trends=documents_df.groupby('time_period')['topic_distribution'].apply(lambda x:np.mean(np.vstack(x),axis=0)).reset_index()
topic_trends=pd.DataFrame({'time_period': topic_trends['time_period'],**{f'topic_{i}': topic_trends['topic_distribution'].apply(lambda x: x[i]) for i in range(doc_topic_distribution.shape[1])}})
# 计算每个时间段内每个主题的平均权重
print(topic_trends.columns)
plt.figure(figsize=(12, 6))
for topic in range(doc_topic_distribution.shape[1]):
    column_name = f'topic_{topic}'
    plt.plot(topic_trends['time_period'], topic_trends[column_name], label=f'Topic {topic + 1}')
plt.xlabel('Time Period')
plt.ylabel('Topic Weight')
plt.title('Topic Trends Over Time')
plt.legend()
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

documents_df=convert_to_dataframe(documents)  
                                                                        
from sklearn.preprocessing import MinMaxScaler

# 归一化数据
scaler = MinMaxScaler()
normalized_weights = scaler.fit_transform(topic_trends[[f'topic_{i}' for i in range(doc_topic_distribution.shape[1])]])

# 创建新的 DataFrame
normalized_topic_trends = topic_trends.copy()
for topic in range(doc_topic_distribution.shape[1]):
    column_name = f'topic_{topic}'
    normalized_topic_trends[column_name] = normalized_weights[:, topic]

# 绘图
plt.figure(figsize=(12, 6))
for topic in range(doc_topic_distribution.shape[1]):
    column_name = f'topic_{topic}'
    plt.plot(
        normalized_topic_trends['time_period'], 
        normalized_topic_trends[column_name], 
        label=f'Topic {topic + 1}',
        alpha=0.7
    )
plt.xlabel('Time Period')
plt.ylabel('Normalized Topic Weight')
plt.title('Normalized Topic Trends Over Time')
plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()