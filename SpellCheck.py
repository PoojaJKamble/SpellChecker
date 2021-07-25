from textblob import TextBlob   #spellcheck module

a='compter'   #wrong word
print("Wrong Spelling : " +str(a))

b = TextBlob(a)
print("Correct Spelling : " +str(b.correct()))
