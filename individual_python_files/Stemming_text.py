# coding: utf-8
import nltk
from nltk.corpus import stopwords
from nltk.stem import SnowballStemmer

stopword = stopwords.words('english')
snowball_stemmer = SnowballStemmer('english')


def stemming(text):
    """
    take string input and stem the words.
    use snowball_stemmer to stem the string.
    """
    word_tokens = nltk.word_tokenize(text)
    stemmed_word = [snowball_stemmer.stem(word) for word in word_tokens]
    return " ".join(stemmed_word)
    
def main():
    text = "the functions of this fan is awesome"
    print (stemming(text))

if __name__ == '__main__':
    main()
    
