import re
import nltk

from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords


nltk.download('punkt')
nltk.download('punkt_tab')
nltk.download('stopwords')



def preprocess_text(text):

    text = text.lower()

    text = re.sub(r'[^a-zA-Z ]', ' ', text)

    tokens = word_tokenize(text)

    stop_words = set(stopwords.words('english'))

    filtered_tokens = [
        word for word in tokens
        if word not in stop_words
    ]

    return " ".join(filtered_tokens)