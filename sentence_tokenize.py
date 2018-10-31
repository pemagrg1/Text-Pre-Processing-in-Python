# coding: utf-8
import nltk
from nltk import word_tokenize

def sentence_tokenize(text):
    """
    take string input and return list of sentences.
    use nltk.sent_tokenize() to split the sentences.
    """
    sent_list=[]
    for w in nltk.sent_tokenize(text):
        sent_list.append(w)
    return sent_list
    
def main():
    text = """Harry Potter is the most miserable, lonely boy you can imagine. He's shunned by his relatives, the Dursley's, that have raised him since he was an infant. He's forced to live in the cupboard under the stairs, forced to wear his cousin Dudley's hand-me-down clothes, and forced to go to his neighbour's house when the rest of the family is doing something fun. Yes, he's just about as miserable as you can get."""
    print (sentence_tokenize(text))

if __name__ == '__main__':
    main()
