from nltk import word_tokenize
from nltk.corpus import stopwords


stop_words = set(stopwords.words('english'))


def remove_stopwords(sentence):
    #removes all the stop words like "is,the,a, etc."
    clean_sent =[]
    for w in word_tokenize(sentence):
        if not w in stop_words:
            clean_sent.append(w)
    return " ".join(clean_sent)
#     return ' '.join([w for w in word_tokenize(sentence) if not w in stop_words]) #5 lines of code can be written in one line

text = """Harry Potter is the most miserable, lonely boy you can imagine. He’s shunned by his relatives, the Dursley’s, that have raised him since he was an infant. He’s forced to live in the cupboard under the stairs, forced to wear his cousin Dudley’s hand-me-down clothes, and forced to go to his neighbour’s house when the rest of the family is doing something fun. Yes, he’s just about as miserable as you can get."""
remove_stopwords(text)

"""
OUTPUT:
'Harry Potter miserable , lonely boy imagine . He ’ shunned relatives , Dursley ’ , raised since infant . He ’ forced live cupboard stairs , forced wear cousin Dudley ’ hand-me-down clothes , forced go neighbour ’ house rest family something fun . Yes , ’ miserable get .'
"""
