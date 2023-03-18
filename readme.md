In this script, we start by opening the text file using open() with the 'r' (read) mode. We then read the file contents into a variable called text.

Next, we use the word_tokenize() function from the NLTK library to tokenize the text into words.

We then filter out words shorter than 4 letters and convert all the words to lowercase.

We count the frequency of each word using the Counter() function from the built-in collections module.

We then use the most_common() method of the Counter object to find the 10 most common words and their frequencies.
Also We pass the start=1 argument to start the line numbers at 1 instead of the default of 0. We then use an f-string to format the output with the line number, word, and count for each item in the list.

Finally, we print the results to the console.

Make sure to replace 'example.txt' with the path to your own text file. If you haven't already installed the NLTK library, you can do so by running pip install nltk in your terminal or command prompt. You'll also need to download the necessary NLTK data by running nltk.download('punkt') at least once before running the script.

Also I added two new options in GUI version: "Minimum word length" and "Number of most common words", which can be set in the GUI interface. The default values for these options are set to 3 and 10, respectively.

When the "Analyze Text" button is clicked, the script reads the text file specified in the file path field and analyzes it using the minimum word length and number of most common words specified in the GUI. The results are displayed in the output text field.