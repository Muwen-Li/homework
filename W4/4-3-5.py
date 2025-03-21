import matplotlib.pyplot as plt
from sklearn.decomposition import LatentDirichletAllocation
from sklearn.feature_extraction.text import CountVectorizer
import pickle
from module4_3_2 import doc_word_freq

with open('count_vectorizer.pkl', 'rb') as f:
    vectorizer = pickle.load(f)
with open('count_matrix.pkl', 'rb') as f:
    doc_term_matrix = pickle.load(f)


num_topics_range=range(2,11)
perplexities=[]

for num_topics in num_topics_range:
    lda=LatentDirichletAllocation(n_components=num_topics,random_state=0)
    lda.fit(doc_term_matrix)
    perplexity=lda.perplexity(doc_term_matrix)
    perplexities.append(perplexity)

plt.plot(num_topics_range,perplexities,marker='o')
plt.xlabel('Number of Topics')
plt.ylabel('Perplexity')
plt.title('Perplexity & Number of Topics')
plt.show()

optimal_num_topics=num_topics_range[perplexities.index(min(perplexities))]
print(f"Optimal number of topics:{optimal_num_topics}")

