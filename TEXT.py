# pip install nltk
import nltk
nltk.download('all')
import string

# input text
text = ("Natural language processing is a field of artificial "
        "intelligence that deals with the interaction between computers and "
        "human (natural) language.")

# tokenize the text
tokens = nltk.word_tokenize(text)
print("Tokens:", tokens)
print()

# lowercase the tokens
lowercased_tokens = [token.lower() for token in tokens]
print("Lowercased tokens:", lowercased_tokens)
print()

# remove punctuation
filtered_tokens = [token for token in tokens if token not in string.punctuation]
print("Tokens without punctuation:", filtered_tokens)
print()

# get list of stopwords in English
stopwords = nltk.corpus.stopwords.words("english")

# remove stopwords
filtered_tokens = [token for token in tokens if token.lower() not in stopwords]
print("Tokens without stopwords:", filtered_tokens)
print()

# create stemmer object
stemmer = nltk.stem.PorterStemmer()

# stem each token
stemmed_tokens = [stemmer.stem(token) for token in tokens]
print("Stemmed tokens:", stemmed_tokens)
print()

# create lemmatizer object
lemmatizer = nltk.stem.WordNetLemmatizer()

# lemmatize each token
lemmatized_tokens = [lemmatizer.lemmatize(token) for token in tokens]
print("Lemmatized tokens:", lemmatized_tokens)
print()
