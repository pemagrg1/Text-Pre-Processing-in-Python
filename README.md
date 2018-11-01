# Text-Pre-Processing-Text-in-Python
So are you planning to do research in the text field but not sure about how to start? <br>
Well, why not start with pre-processing of text as it is very important while doing research in text field and its easy! while cleaning the text helps you get quality output by removing all irrelevant text and getting the forms of the words etc. <br>
In this article, we will be covering:<br>
1. Converting text to lowercase
2. Contraction
3. Sentence tokenize
4. Word tokenize
5. Spell Check
6. Lemmatize
7. Stemming
8. Remove Tags
9. Remove numbers
10. Remove punctuation
11. Remove stopwords


<br>Let's START! <br>
Pre-requisites:<br>
install Python<br>
install NLTK<br>
pip install autocorrect<br>
<br><br>Done with the installations? okay! let's start coding! <br>
#### Convert text to lower case:<br>
Converting text to lower case as in, converting "Hello" to "hello" or "HELLO" to "hello".<br>

#### Contraction<br>
Contraction helps to expand the word form like "ain't": "am not". Contractions file has been created in my github which we will be importing to use it.

#### sentence tokenize
Tokenize sentences if the there are more than 1 sentence i.e breaking the sentences to list of sentence.

#### word tokenize
Tokenize words to get the tokens of the text i.e breaking the sentences into list of words.

#### Spell Check
correct the incorrect spelled words like "wrld" to "world"

#### Lemmatize
lemmatize the text so as to get its root form eg: functions,funtionality as function
#### Stemming
stemming is the process of reducing inflected (or sometimes derived) words to their word stem, base or root form
#### Remove Tags
Removing html tags from the text like "<head><body>" using regex.

#### Remove Numbers
Removing numbers from the text like "1,2,3,4,5…" We usually remove numbers when we do text clustering or getting keyphrases as we numbers doesn't give much importance to get the main words. To remove numbers, you can use: .isnumeric() else .isdigit()
#### Remove punctuation
Removing punctuation from the text like ".?!" and also the symbols like "@#$" .
#### Stop words removal
Remove irrelevant words using nltk stop words like "is,the,a" etc from the sentences as they don't carry any information.
#### PS:
You can get all the above code from: GITHUB
Once you are done with Pre-processing, you can then move to NER, clustering, word count, sentiment analysis, etc.
All the best with your research!
