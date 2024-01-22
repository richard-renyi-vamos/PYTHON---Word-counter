CHAT GPT CONVERSATION:

User
create a python script that counts words in a document and shows them as a barchart
ChatGPT
Certainly! To achieve this, you can use Python's libraries like matplotlib for plotting and collections to count the words. Here's a basic example:

First, make sure you have the required libraries installed. You can install them using pip:

bash
Copy code
pip install matplotlib
Here's a Python script that counts words in a document and displays them as a bar chart:

python
Copy code
import matplotlib.pyplot as plt
from collections import Counter
import re

def count_words(file_path):
    with open(file_path, 'r') as file:
        text = file.read().lower()  # Read the file content and convert to lowercase
        words = re.findall(r'\b\w+\b', text)  # Extract words using regex
        word_counts = Counter(words)  # Count occurrences of each word
        return word_counts

def plot_bar_chart(word_counts, top_n=10):
    top_words = dict(word_counts.most_common(top_n))  # Get the top n words and their counts

    plt.figure(figsize=(10, 6))
    plt.bar(top_words.keys(), top_words.values(), color='skyblue')
    plt.xlabel('Words')
    plt.ylabel('Frequency')
    plt.title(f'Top {top_n} Most Common Words')
    plt.xticks(rotation=45)  # Rotate x-axis labels for better readability
    plt.tight_layout()
    plt.show()

# Provide the path to your document here
file_path = 'path/to/your/document.txt'

word_counts = count_words(file_path)
plot_bar_chart(word_counts)
Replace 'path/to/your/document.txt' with the actual path to your document. This script reads the content of the document, counts the words, and displays the top N most common words (default is 10) in a bar chart using matplotlib.

This code snippet will create a bar chart displaying the top words and their frequency in your document. Adjust the top_n parameter in the plot_bar_chart function to display more or fewer words in the chart.
