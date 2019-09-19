# coding: utf-8
"""
import all the functions from all the python files

"""
from individual_python_files.contractions import contractions_dict
from individual_python_files.expanding_contractions import expand_contractions
from individual_python_files.spell_check import autospell
from individual_python_files.to_lower import to_lower
from individual_python_files.remove_number import remove_numbers
from individual_python_files.remove_punctuation import remove_punct
from individual_python_files.remove_tags import remove_Tags
from individual_python_files.lemmatizing import lemmatize
from individual_python_files.Stemming_text import stemming
from individual_python_files.remove_stop_words import remove_stopwords
from individual_python_files.word_tokenize import word_tokenize

def pre_process(text):
    """

    """
    text = expand_contractions(text, contractions_dict)
    text = autospell(text)
    text = to_lower(text)
    text = remove_numbers(text)
    text = remove_punct(text)
    text = remove_Tags(text)
    text = lemmatize(text)
    text = stemming(text)
    text = remove_stopwords(text)
    text = word_tokenize(text)
    return (text)


def main():
    text = """Similaly, once you'd beyond this surprising first step, you'd realise that Satanism isn't at all like what the movies have shown us. Whereas Harry Potter couldn't wait to put his muggle past behind him, Sabrina is having a more difficult time making up her mind. At one point, Sabrina and her friends even make a slight reference to Riverdale high school, perhaps teasing a future crossover. Kiernan Shipka is off to the Academy of Unseen Arts in Chilling Adventures of Sabrina. With minor adjustments The Chilling Adventures of Sabrina could be Netflix's new A Series of Unfortunate Events, but with Umbrella Academy in the offing, the streaming service's offbeat YA material seems to be cannibalising itself."""
    pre_process_text = pre_process(text)
    print(pre_process_text)
    print ("counting the word frequency")
    word_count = dict()

    for word in pre_process_text:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1

    for w in sorted(word_count, key=word_count.get, reverse=True):
        print (w, word_count[w])


if __name__ == '__main__':
    main()

