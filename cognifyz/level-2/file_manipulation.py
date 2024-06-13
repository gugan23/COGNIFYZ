import re
from collections import Counter

def count_words(file_path):
    try:
        with open(file_path, 'r') as file:
            text = file.read()
    except FileNotFoundError:
        print(f"The file at {file_path} was not found.")
        return
    
    
    words = re.findall(r'\b\w+\b', text.lower())
    
   
    word_counts = Counter(words)
    
    
    sorted_word_counts = sorted(word_counts.items())
    
    
    for word, count in sorted_word_counts:
        print(f"{word}: {count}")

if __name__ == "__main__":
   
    file_path = input("Please enter the path to the text file: ")
    count_words(file_path)
