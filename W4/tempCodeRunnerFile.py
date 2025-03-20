

    tfidf_vectorizer = TfidfVectorizer(stop_words=stopwords)
    tfidf_matrix=tfidf_vectorizer.fit_transform(document_texts)
    t_feature_names = tfidf_vectorizer.get_feature_names_out()
    tfidf_feature_names=t_feature_names