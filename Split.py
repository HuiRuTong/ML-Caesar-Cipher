"""
This program splits long paragraphs of text into sentences
and then writes them line-by-line into a file so that each
sentence can later be encrypted.
"""
import nltk

def Split_para(path):
    text = open(path, 'r+', encoding="utf-8")  # Opens the text file for reading and writing

    content = text.read()
    sentences = nltk.tokenize.sent_tokenize(content)    # Splits the text into multiple sentences; from the nltk documentation: https://www.nltk.org/_modules/nltk/tokenize.html#sent_tokenize

    text.seek(0)    # Resets the pointer to the beginning of the file so truncate() can remove all content
    text.truncate()

    for s in sentences:
        text.write(f"{s}\n")

    text.close()