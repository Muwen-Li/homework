import pandas as pd
from sklearn.decomposition import LatentDirichletAllocation
import matplotlib.pyplot as plt
from module4_3_1 import document_shopID_time
from module4_3_2 import doc_word_freq

def lda_topic_analysis(shopID, time_unit, stopwords, n_topics=5):
    df = pd.read_csv('C:\\Users\\Lenovo\\Desktop\\week4.csv')
    count_matrix, count_vectorizer,feature_names= doc_word_freq(shopID, time_unit, stopwords)
    
    
    lda = LatentDirichletAllocation(n_components=n_topics, random_state=42, learning_method='online')
    lda.fit(count_matrix)

    # 查看每个主题的关键词
    topic_word_distribution = lda.components_
    feature_names = count_vectorizer.get_feature_names_out()
    n_top_words = 10
    for topic_idx, topic in enumerate(topic_word_distribution):
        print(f"Topic {topic_idx}:")
        top_words_idx = topic.argsort()[-n_top_words:][::-1]
        top_words = [feature_names[i] for i in top_words_idx]
        print(" ".join(top_words))

    # 查看文档的主题分布
    doc_topic_distribution = lda.transform(count_matrix)
    for doc_idx, topic_dist in enumerate(doc_topic_distribution):
        print(f"Document {doc_idx}:")
        for topic_idx, prob in enumerate(topic_dist):
            print(f"  Topic {topic_idx}: {prob:.4f}")

    # 可视化文档的主题分布
    plt.figure(figsize=(10, 6))
    for topic_idx in range(n_topics):
        plt.plot(doc_topic_distribution[:, topic_idx], label=f"Topic {topic_idx}")
    plt.xlabel("Document Index")
    plt.ylabel("Topic Probability")
    plt.title("Document-Topic Distribution")
    plt.legend()
    plt.show()

    return doc_topic_distribution


