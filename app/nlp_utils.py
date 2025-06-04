from nltk.stem import WordNetLemmatizer



# Creating a lemmatizer instance
lemmatizer = WordNetLemmatizer()

# Defining a function to preprocess the input text
def preprocess_input(text: str) -> str:
    # Converting  text to lowercase and split it into words using basic whitespace 
    tokens = text.lower().split()
    # Applying lemmatization to each token
    lemmas = [lemmatizer.lemmatize(token) for token in tokens]

    # Rejoining  the lemmatized words into a single string
    return " ".join(lemmas)
