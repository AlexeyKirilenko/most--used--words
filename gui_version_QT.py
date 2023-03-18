# >pip install pyqt5     before run


import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog, QTextEdit, QPushButton

from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QTextEdit
from collections import Counter


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        # Create GUI elements
        self.title = QLabel("Word Count Tool", self)
        self.title.move(50, 10)

        self.file_label = QLabel("File path:", self)
        self.file_label.move(50, 50)

        self.file_input = QLineEdit(self)
        self.file_input.move(110, 50)

        self.len_label = QLabel("Minimum word length:", self)
        self.len_label.move(50, 80)

        self.len_input = QLineEdit(self)
        self.len_input.move(160, 80)

        self.count_label = QLabel("Number of most common words to display:", self)
        self.count_label.move(50, 110)

        self.count_input = QLineEdit(self)
        self.count_input.move(295, 110)

        self.result_label = QLabel("Word counts:", self)
        self.result_label.move(50, 150)

        self.result_display = QTextEdit(self)
        self.result_display.setReadOnly(True)
        self.result_display.setGeometry(50, 180, 400, 250)

        self.import_button = QPushButton("Import file", self)
        self.import_button.setGeometry(50, 450, 100, 30)
        self.import_button.clicked.connect(self.import_file)

        self.start_button = QPushButton("Start", self)
        self.start_button.setGeometry(175, 450, 100, 30)
        self.start_button.clicked.connect(self.start_analysis)

        self.clear_button = QPushButton("Clear", self)
        self.clear_button.setGeometry(300, 450, 100, 30)
        self.clear_button.clicked.connect(self.clear_results)

        # Set window properties
        self.setGeometry(300, 300, 500, 500)
        self.setWindowTitle("Word Count Tool")
        self.show()

    def import_file(self):
        filepath, _ = QFileDialog.getOpenFileName(self, "Select text file", "", "Text Files (*.txt)")
        self.file_input.setText(filepath)

    def start_analysis(self):
        filepath = self.file_input.text()
        min_len = int(self.len_input.text())
        num_words = int(self.count_input.text())

        # Read in file and count words
        try:
            with open(filepath, encoding='utf-8', errors='ignore') as file:
                words = file.read().split()
                counts = Counter(word.lower() for word in words if len(word) >= min_len)
                most_common = counts.most_common(num_words)
        except FileNotFoundError:
            self.result_display.setText("Error: File not found.")
            return
        except Exception as e:
            self.result_display.setText(f"Error: {e}")
            return

        # Format word counts for display
        result_str = ""
        for i, word_count in enumerate(most_common):
            result_str += f"{i+1}. {word_count[0]} = {word_count[1]}\n"

        # Display word counts
        self.result_display.setText(result_str)

    def clear_results(self):
        self.file_input.setText("")
        self.len_input.setText("")
        self.count_input.setText("")
        self.result_display.setText("")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())

