import string
import nltk

from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer


# Download required NLTK resources
nltk.download("punkt", quiet=True)
nltk.download("punkt_tab", quiet=True)
nltk.download("wordnet", quiet=True)
nltk.download("omw-1.4", quiet=True)


lemmatizer = WordNetLemmatizer()


def preprocess_text(text):
    text = text.lower()

    tokens = word_tokenize(text)

    tokens = [
        lemmatizer.lemmatize(word)
        for word in tokens
        if word not in string.punctuation
    ]

    return " ".join(tokens)