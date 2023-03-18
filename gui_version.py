import tkinter as tk
from tkinter import filedialog
import collections


class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.master.title("Text Analyzer")
        self.grid()
        self.create_widgets()

    def create_widgets(self):
        self.file_label = tk.Label(self, text="Select a text file:")
        self.file_label.grid(row=0, column=0)

        self.file_path_var = tk.StringVar()
        self.file_path_entry = tk.Entry(self, textvariable=self.file_path_var, width=50)
        self.file_path_entry.grid(row=0, column=1)

        self.browse_button = tk.Button(self, text="Browse", command=self.browse_file)
        self.browse_button.grid(row=0, column=2)

        self.len_label = tk.Label(self, text="Minimum word length:")
        self.len_label.grid(row=1, column=0)

        self.len_var = tk.StringVar()
        self.len_var.set("3")
        self.len_entry = tk.Entry(self, textvariable=self.len_var, width=10)
        self.len_entry.grid(row=1, column=1)

        self.count_label = tk.Label(self, text="Number of most common words:")
        self.count_label.grid(row=2, column=0)

        self.count_var = tk.StringVar()
        self.count_var.set("10")
        self.count_entry = tk.Entry(self, textvariable=self.count_var, width=10)
        self.count_entry.grid(row=2, column=1)

        self.analyze_button = tk.Button(self, text="Analyze Text", command=self.analyze_text)
        self.analyze_button.grid(row=3, column=0, columnspan=3)

        self.output_text = tk.Text(self, height=10, width=50)
        self.output_text.grid(row=4, column=0, columnspan=3)

    def browse_file(self):
        file_path = filedialog.askopenfilename()
        if file_path:
            self.file_path_var.set(file_path)

    def analyze_text(self):
        file_path = self.file_path_var.get()
        min_len = int(self.len_var.get())
        num_words = int(self.count_var.get())

        word_counts = collections.Counter()

        with open(file_path, 'r', encoding="utf8", errors='ignore') as f:
            for line_num, line in enumerate(f, start=1):
                for word in line.split():
                    if len(word) >= min_len:
                        word_counts[word] += 1

        self.output_text.delete('1.0', tk.END)

        for idx, (word, count) in enumerate(word_counts.most_common(num_words), start=1):
            self.output_text.insert(tk.END, f"{idx}. {word} = {count}\n")


root = tk.Tk()
app = Application(master=root)
app.mainloop()
