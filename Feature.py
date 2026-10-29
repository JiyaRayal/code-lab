from sklearn.feature_extraction.text import CountVectorizer
documents = [
    "Hello!!!   I LOVE AI, and it is AMAZING!!! 😍 #MachineLearning",
    "Natural Language Processing (NLP) is a fascinating field of AI.",
    "Tokenization, stemming, and lemmatization are essential steps in text preprocessing."
]
vectorizer = CountVectorizer()
X = vectorizer.fit_transform(documents)

print("Feature Names:", vectorizer.get_feature_names_out())
print("Document-Term Matrix:\n", X.toarray())
print("Shape of Document-Term Matrix:", X.shape)
print("Number of Features:", len(vectorizer.get_feature_names_out()))
print("Vocabulary:", vectorizer.vocabulary_)