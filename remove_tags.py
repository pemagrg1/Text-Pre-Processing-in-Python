# coding: utf-8
import re
import nltk
from nltk import word_tokenize

def remove_Tags(text):
    """
    take string input and clean string without tags.
    use regex to remove the html tags.
    """
    cleaned_text = re.sub('<[^<]+?>','', text)
    return cleaned_text
    
def main():
    text = """<head><body>hello world!</body></head>"""
    print (remove_Tags(text))

if __name__ == '__main__':
    main()
    
