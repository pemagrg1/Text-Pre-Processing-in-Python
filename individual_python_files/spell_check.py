# coding: utf-8
import nltk
from autocorrect import spell
from nltk import word_tokenize

def autospell(text):
    """
    correct the spelling of the word.
    """
    spells = [spell(w) for w in (nltk.word_tokenize(text))]
    return " ".join(spells)


def main():
    text = "This is a wrld of hope"
    spell_text = autospell(text)
    print (spell_text)

if __name__ == '__main__':
    main()
    
