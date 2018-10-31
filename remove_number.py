# coding: utf-8
import nltk
from nltk import word_tokenize

def remove_numbers(text):
    """
    take string input and return a clean text without numbers. 
    Use regex to discard the numbers.
    """
    output = ''.join(c for c in text if not c.isdigit())
    return output
    
def main():
    text = "There was 200 people standing right next to me at 2pm."
    print (remove_numbers(text))

if __name__ == '__main__':
    main()
    
