# coding: utf-8
from string import punctuation


def remove_punct(text):
    """
    take string input and clean string without punctuations.
    use regex to remove the punctuations.
    """
    return ''.join(c for c in text if c not in punctuation)
    
def main():
    text = "Hello! how are you doing?"
    print (remove_punct(text))

if __name__ == '__main__':
    main()
    
