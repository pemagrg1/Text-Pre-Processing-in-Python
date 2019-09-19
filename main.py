from Preprocess import Preprocess

pr = Preprocess()
t = pr.to_lower("pema is coding this part. who are you? 123 <with>")
print (pr.lemmatize(t))