import tkinter as tk
from tkinter import scrolledtext, ttk
from collections import Counter

def count_words():
    text = article_text.get("1.0", tk.END).lower()
    words = text.split()
    word_counts = Counter(words)

    # Clearing the previous results in the table
    for i in tree.get_children():
        tree.delete(i)

    # Inserting new word counts into the table
    for word, count in word_counts.items():
        tree.insert('', 'end', values=(word, count))

def treeview_sort_column(col, reverse):
    l = [(tree.set(k, col), k) for k in tree.get_children('')]
    l.sort(reverse=reverse)

    # Rearranging items in sorted positions
    for index, (val, k) in enumerate(l):
        tree.move(k, '', index)

    # Reverse sort next time
    tree.heading(col, command=lambda: treeview_sort_column(col, not reverse))

# Set up the main window
root = tk.Tk()
root.title("Word Counter")

# Create a text box for the article
article_text = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=40, height=10)
article_text.pack(pady=10)

# Create a button to count words
count_button = tk.Button(root, text="Count Words", command=count_words)
count_button.pack()

# Create a Treeview widget for displaying the words and counts
tree = ttk.Treeview(root, columns=('Word', 'Count'), show='headings')
tree.heading('Word', text='Word', command=lambda: treeview_sort_column('Word', False))
tree.heading('Count', text='Count', command=lambda: treeview_sort_column('Count', False))
tree.column('Word', width=200)
tree.column('Count', width=100, anchor='center')
tree.pack(pady=10)

# Start the GUI loop
root.mainloop()
