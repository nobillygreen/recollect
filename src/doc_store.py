import json
from glob import glob

import numpy as np
import sklearn
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer


class DocStore:
    def __init__(self):
        self.documents = []
        self.tfidf_vectorizer = None
        self.bow_vectorizer = None
        self.vectors = np.array([])
        self.vocabulary = []
        self.weights = np.array([])

    def load_documents(self, documents_path: str):
        """
        Loads all json documents stored under documents_path, creates a TFIDF vectorizor, and vectorizes
        all the documents into a 
        If called for a second time, then this overwrites the original model and vectorized docs.
        Call this again when documents need to be reloaded.
        """

        # Load in the documents
        self.documents = []
        for file_name in glob('./documents/*.json'):
            with open(file_name, 'r') as f:
                doc = json.load(f)
                self.documents.append(doc['body'])

        # Create the TFIDF vectorizor
        self.tfidf_vectorizer = TfidfVectorizer().fit(self.documents)

        # Save the vocab
        self.vocabulary = self.tfidf_vectorizer.get_feature_names()

        # Create the BOW vectors of the docs
        new_vectors = self.tfidf_vectorizer.transform(self.documents)
        self.vectors = np.asarray(new_vectors.toarray())

    def search(self, query):
        # get the vectorized version of the query
        vector = self.tfidf_vectorizer.transform([query]).toarray()
        vector = np.transpose(vector)
        scores = np.dot(self.vectors, vector)

        results = list(zip(self.documents, scores.tolist()))
        results.sort(key=lambda x: x[1], reverse=True)
        return results
