from Preprocess import Preprocess

text = "pema is coding this part. who are you? Pema 123 <with>"
pr = Preprocess()


"""
INDIVIDUAL TESTING
"""
lower_text = pr.to_lower(text)
sentence_tokens = pr.sentence_tokenize(lower_text)
for each_sent in sentence_tokens:
    lemmatizzed_sent = pr.lemmatize(each_sent)
    clean_text = pr.remove_numbers(lemmatizzed_sent)
    clean_text = pr.remove_punct(clean_text)
    clean_text = pr.remove_Tags(clean_text)
    clean_text = pr.remove_stopwords(clean_text)
    word_tokens = pr.word_tokenize(clean_text)
    print(word_tokens)


"""
You can call the preprocess function directly
"""
print()
print (pr.preprocess(text))