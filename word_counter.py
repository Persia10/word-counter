from collections import Counter
import string

def clean_text(text):
    # Convert to lowercase
    text = text.lower()
    # Remove punctuation
    return text.translate(str.maketrans('', '', string.punctuation))

def count_words(filename):
    try:
        with open(filename, 'r') as file:
            text = file.read()
            cleaned = clean_text(text)
            words = cleaned.split()
            word_counts = Counter(words)
            return word_counts
    except FileNotFoundError:
        print("File not found. Please check the filename.")
        return {}

def print_top_words(word_counts, top_n=10):
    print(f"\nTop {top_n} most common words:\n")
    for word, count in word_counts.most_common(top_n):
        print(f"{word}: {count}")

if __name__ == "__main__":
    filename = input("Enter the name of the .txt file to analyze: ")
    word_counts = count_words(filename)
    if word_counts:
        print_top_words(word_counts)
