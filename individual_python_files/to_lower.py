# coding: utf-8
import nltk
from nltk import word_tokenize

def to_lower(text):
    """
    Converting text to lower case as in, converting "Hello" to "hello" or "HELLO" to "hello".
    """
    return ' '.join([w.lower() for w in word_tokenize(text)])


def main():
    text = """Harry Potter is the most miserable, lonely boy you can imagine. He’s shunned by his relatives, the Dursley’s, that have raised him since he was an infant. He’s forced to live in the cupboard under the stairs, forced to wear his cousin Dudley’s hand-me-down clothes, and forced to go to his neighbour’s house when the rest of the family is doing something fun. Yes, he’s just about as miserable as you can get."""
    lower_text = to_lower(text)
    print (lower_text)

if __name__ == '__main__':
    main()
    
