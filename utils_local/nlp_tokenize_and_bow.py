from nltk.util import ngrams
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer, WordNetLemmatizer
from nltk.tag import pos_tag
from collections import Counter
import re

nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
nltk.download('stopwords')
nltk.download('wordnet')


# Function to expand contractions

def _expand_contractions(text):
    contractions_dict = {
        "ain't": "are not", "aren't": "are not", "can't": "cannot", "can't've": "cannot have", "'cause": "because",
        "could've": "could have", "couldn't": "could not", "couldn't've": "could not have", "didn't": "did not",
        "doesn't": "does not", "don't": "do not", "hadn't": "had not", "hadn't've": "had not have",
        "hasn't": "has not", "haven't": "have not", "he'd": "he would", "he'd've": "he would have",
        "he'll": "he will", "he'll've": "he will have", "he's": "he is", "how'd": "how did", "how'd'y": "how do you",
        "how'll": "how will", "how's": "how is", "I'd": "I would", "I'd've": "I would have", "I'll": "I will",
        "I'll've": "I will have", "I'm": "I am", "I've": "I have", "isn't": "is not", "it'd": "it would",
        "it'd've": "it would have", "it'll": "it will", "it'll've": "it will have", "it's": "it is",
        "let's": "let us", "ma'am": "madam", "mayn't": "may not", "might've": "might have", "mightn't": "might not",
        "mightn't've": "might not have", "must've": "must have", "mustn't": "must not", "mustn't've": "must not have",
        "needn't": "need not", "needn't've": "need not have", "o'clock": "of the clock", "oughtn't": "ought not",
        "oughtn't've": "ought not have", "shan't": "shall not", "sha'n't": "shall not", "shan't've": "shall not have",
        "she'd": "she would", "she'd've": "she would have", "she'll": "she will", "she'll've": "she will have",
        "she's": "she is", "should've": "should have", "shouldn't": "should not", "shouldn't've": "should not have",
        "so've": "so have", "so's": "so is", "that'd": "that had", "that'd've": "that would have", "that's": "that is",
        "there'd": "there would", "there'd've": "there would have", "there's": "there is", "they'd": "they would",
        "they'd've": "they would have", "they'll": "they will", "they'll've": "they will have", "they're": "they are",
        "they've": "they have", "to've": "to have", "wasn't": "was not", "we'd": "we would", "we'd've": "we would have",
        "we'll": "we will", "we'll've": "we will have", "we're": "we are", "we've": "we have", "weren't": "were not",
        "what'll": "what will", "what'll've": "what will have", "what're": "what are", "what's": "what is",
        "what've": "what have", "when's": "when is", "when've": "when have", "where'd": "where did",
        "where's": "where is", "where've": "where have", "who'll": "who will", "who'll've": "who will have",
        "who's": "who is", "who've": "who have", "why's": "why is", "why've": "why have", "will've": "will have",
        "won't": "will not", "won't've": "will not have", "would've": "would have", "wouldn't": "would not",
        "wouldn't've": "would not have", "y'all": "you all", "y'all'd": "you all would", "y'all'd've": "you all would have",
        "y'all're": "you all are", "y'all've": "you all have", "you'd": "you would", "you'd've": "you would have",
        "you'll": "you will", "you'll've": "you will have", "you're": "you are", "you've": "you have"
    }

    contractions_re = re.compile('(%s)' % '|'.join(contractions_dict.keys()))

    def replace(match):
        return contractions_dict[match.group(0)]

    return contractions_re.sub(replace, text)


# Step 1: Remove proper nouns
# def _remove_proper_nouns(text):
#     tagged = pos_tag(word_tokenize(text))
#     return ' '.join([word for word, tag in tagged if tag != 'NNP' and tag != 'NNPS'])


# Step 2: Normalization
def _normalize(text):
    text = text.lower()
    text = _expand_contractions(text)
    text = re.sub(r'[^a-zA-Z\s]', '', text)
    return text


# Step 3: Stemming and Lemmatization
def _stem_and_lemmatize(tokens):
    porter = PorterStemmer()
    wnl = WordNetLemmatizer()
    return [wnl.lemmatize(porter.stem(token)) for token in tokens]


# Step 4: Tokenization
def _tokenize(text):
    return word_tokenize(text)


# Step 5: Removing stop words
def _remove_stopwords(tokens):
    stop_words = set(stopwords.words('english'))
    return [token for token in tokens if token not in stop_words]


# Step 6: Bag-of-words representation
def _bag_of_words(tokens, n=1):
    if n == 1:
        return Counter(tokens)
    else:
        n_grams = _get_ngrams(tokens, n)
        return Counter(n_grams)

# New function to generate n-grams
def _get_ngrams(tokens, n):
    return list(ngrams(tokens, n))

def clean_from_txt_to_bow(txt, n=1):
    # cleaned_txt = _remove_proper_nouns(txt)
    cleaned_txt = _normalize(txt)
    tokens = _tokenize(cleaned_txt)
    tokens = _stem_and_lemmatize(tokens)
    tokens = _remove_stopwords(tokens)
    bow = _bag_of_words(tokens, n)
    return bow


if __name__ == "__main__":
    txt = """
            I met a traveller from an antique land
            Who said: Two vast and trunkless legs of stone
            Stand in the desert. Near them on the sand,
            Half sunk, a shatter'd visage lies, whose frown
            And wrinkled lip and sneer of cold command
            Tell that its sculptor well those passions read
            Which yet survive, stamp'd on these lifeless things,
            The hand that mock'd them and the heart that fed;
            And on the pedestal these words appear:
            "My name is Ozymandias, king of kings;
            Look on my works, ye Mighty, and despair!"
            Nothing beside remains: round the decay
            Of that colossal wreck, boundless and bare,
            The lone and level sands stretch far away.
            """
    # Perform the cleaning steps
    bow = clean_from_txt_to_bow(txt, n =3)

    # Your article text
    print('Result is', bow)