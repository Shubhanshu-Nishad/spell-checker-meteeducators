from textblob import TextBlob 

print('SPELL CHECK \n Enter Your Text:-')
# You can input any text that you want to spell check.
text = input()
blob = TextBlob(text)
# You will get the correct text as output.
print('Correct Text:-')
print(str(blob.correct()))
