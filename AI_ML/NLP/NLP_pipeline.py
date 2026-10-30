import re
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

# Download required resources (run once)
import nltk

nltk.download('punkt')
nltk.download('punkt_tab')
nltk.download('stopwords')

text = "Hello!!!   I LOVE AI, and it is AMAZING!!! 😍 #MachineLearning"

# 1. Lowercase
text = text.lower()

# 2. Remove punctuation
text = re.sub(r'[^\w\s]', '', text)

# 3. Remove extra spaces
text = " ".join(text.split())

# 4. Tokenize
tokens = word_tokenize(text)

# 5. Remove stopwords
stop_words = set(stopwords.words("english"))
tokens = [word for word in tokens if word not in stop_words]

print("Cleaned Text:", text)
print("Tokens:", tokens)