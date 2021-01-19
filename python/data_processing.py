import re
from nltk.stem import WordNetLemmatizer

stemmer = WordNetLemmatizer()

def preprocess_code(code):
        # Remove all the special characters
        code = re.sub(r'\W', ' ', str(code))

        # remove all single characters
        code = re.sub(r'\s+[a-zA-Z]\s+', ' ', code)

        # Remove single characters from the start
        code = re.sub(r'\^[a-zA-Z]\s+', ' ', code)

        # Substituting multiple spaces with single space
        code = re.sub(r'\s+', ' ', code, flags=re.I)

        # Removing prefixed 'b'
        code = re.sub(r'^b\s+', '', code)

        # Converting to Lowercase
        code = code.lower()

        # Lemmatization
        tokens = code.split()
        tokens = [stemmer.lemmatize(word) for word in tokens]
        tokens = [word for word in tokens if word not in en_stop]
        tokens = [word for word in tokens if len(word) > 3]

        preprocessed_text = ' '.join(tokens)

        return preprocessed_text