from textblob import TextBlob
 
 
def sentiment(polarity):
    if blob.sentiment.polarity < 0:
        print("Negative")
    elif blob.sentiment.polarity > 0:
        print("Positive")
    else:
        print("Neutral")
 
a=input("Enter any statement: ")

blob = TextBlob(a)
sentiment(blob.sentiment.polarity)
 
