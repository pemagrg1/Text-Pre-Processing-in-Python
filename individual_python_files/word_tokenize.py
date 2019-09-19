# coding: utf-8
import nltk
from nltk import word_tokenize

def word_tokenize(text):
    """
    take string input and return list of words.
    use nltk.word_tokenize() to split the words.
    """
    word_list=[]
    for sentences in nltk.sent_tokenize(text):
        for words in nltk.word_tokenize(sentences):
            word_list.append(words)
    return word_list
    
def main():
    text = """Harry Potter is the most miserable, lonely boy you can imagine. He's shunned by his relatives, the Dursley's, that have raised him since he was an infant. He's forced to live in the cupboard under the stairs, forced to wear his cousin Dudley's hand-me-down clothes, and forced to go to his neighbour's house when the rest of the family is doing something fun. Yes, he's just about as miserable as you can get."""
    print (word_tokenize(text))

if __name__ == '__main__':
    main()
