# Text classification (example using a simple Naive Bayes classifier)
from nltk.classify import NaiveBayesClassifier
import nltk

# training data (using a toy dataset for illustration purposes)
training_data = [
    ("It was a great movie.", "pos"),
    ("I hated the book.", "neg"),
    ("The book was okay.", "pos")
]

# extract features from the training data
def extract_features(text):
    features = {}
    for word in nltk.word_tokenize(text):
        features[word] = True
    return features

# create a list of feature sets and labels
feature_sets = [(extract_features(text), label) for (text, label) in training_data]

# train the classifier
classifier = NaiveBayesClassifier.train(feature_sets)

# test the classifier on a new example
test_text = "It is a great movie."
print("Sentiment:", classifier.classify(extract_features(test_text)))
