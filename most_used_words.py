import nltk
nltk.download('punkt')
from nltk.tokenize import word_tokenize
from collections import Counter

# Open the text file with UTF-8 encoding and read its contents
with open('example.txt', 'r', encoding='utf-8', errors='ignore') as txt_file:
    text = txt_file.read()

# Tokenize the text into words
words = word_tokenize(text)

# Filter out words shorter than 3 letters and convert to lowercase
words = [word.lower() for word in words if len(word) >= 4]

word_counts = Counter(words)


most_common = word_counts.most_common(100)

# Print the results with line numbers
print('The 10 most common words starting from 3 letters are:')
for i, (word, count) in enumerate(most_common, start=1):
    print(f'{i}. {word}: {count}')
