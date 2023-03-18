import nltk
nltk.download('punkt')
from nltk.tokenize import word_tokenize
from collections import Counter
import tkinter as tk
from tkinter import filedialog

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.master.title('Word Frequency Counter')
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        # Create the "Import File" button
        self.import_button = tk.Button(self, text='Import File', command=self.import_file)
        self.import_button.pack(side='left')

        # Create the "Start" button
        self.start_button = tk.Button(self, text='Start', command=self.start_analysis)
        self.start_button.pack(side='left')

        # Create the text box for displaying results
        self.results_box = tk.Text(self, width=60, height=20)
        self.results_box.pack(side='top', fill='both', expand=True)

    def import_file(self):
        # Use a file dialog to select a text file
        file_path = filedialog.askopenfilename()

        # Open the selected text file with UTF-8 encoding and read its contents
        with open(file_path, 'r', encoding='utf-8', errors='ignore') as txt_file:
            self.text = txt_file.read()

    def start_analysis(self):
        # Tokenize the text into words
        words = word_tokenize(self.text)

        # Filter out words shorter than 4 letters and convert to lowercase
        words = [word.lower() for word in words if len(word) >= 4]

        # Count the frequency of each word
        word_counts = Counter(words)

        # Find the 10 most common words and their frequencies
        most_common = word_counts.most_common(100)

        # Clear the results box
        self.results_box.delete('1.0', 'end')

        # Display the results in the results box
        self.results_box.insert('end', 'The 100 most common words starting from 4 letters are:\n\n')
        for i, (word, count) in enumerate(most_common, start=1):
            result = f'{i}. {word}: {count}\n'
            self.results_box.insert('end', result)


root = tk.Tk()
app = Application(master=root)
app.mainloop()
