from textblob import TextBlob
from flask import Flask,render_template,request

app=Flask(__name__)
 

@app.route("/")
def sentiment():
	return render_template('AYUSHI2.html')


@app.route("/result",methods=["POST","GET"])
def fun():
    blob=TextBlob(request.form["sentiment_text"])
    a=float(blob.sentiment.polarity)
    if a>0:
        return render_template('AYUSHI3.html')
    elif a<0:
        return render_template('AYUSHI11.html')
    else:
        return render_template('AYUSHI6.html')

if __name__=="__main__":
	app.run(debug=True)