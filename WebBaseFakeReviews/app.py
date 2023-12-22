import re
from flask import Flask, request, flash, url_for, redirect, render_template, session
from Model import Model
from LoadModels import LoadModels
from string import punctuation
from nltk.corpus import stopwords
import nltk
from nltk.stem import WordNetLemmatizer
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

app = Flask(__name__)
  
  
app.secret_key = 'python world'
lm = LoadModels()
model = Model()
lm.loadModel(model)

sid = SentimentIntensityAnalyzer()
stop_words = set(stopwords.words('english'))
lemmatizer = WordNetLemmatizer()

def cleanPost(doc):
    tokens = doc.split()
    table = str.maketrans('', '', punctuation)
    tokens = [w.translate(table) for w in tokens]
    tokens = [word for word in tokens if word.isalpha()]
    tokens = [w for w in tokens if not w in stop_words]
    tokens = [word for word in tokens if len(word) > 1]
    tokens = [lemmatizer.lemmatize(token) for token in tokens]
    tokens = ' '.join(tokens)
    return tokens

def getResult(predict):
    result = ''
    if predict == 0:
        result = 'FAKE'
    else:
        result = "TRUTHFULL"
    return result

def reviewSentiment(review):
    sentiment_dict = sid.polarity_scores(review)
    negative = sentiment_dict['neg']
    positive = sentiment_dict['pos']
    neutral = sentiment_dict['neu']
    compound = sentiment_dict['compound']
    result = ''
    if compound >= 0.05 :
       result = 'Positive' 
    elif compound <= - 0.05 :
       result = 'Negative' 
    else:
       result = 'Neutral'
    return result   

@app.route('/ReviewAction', methods =['GET', 'POST'])
def ReviewAction():
   if request.method == 'POST':
        if not request.form['t1'] or not request.form['t2']:
           output = 'Please enter review in the fields'
        else:
           msg = request.form['t1']
           algorithm = request.form['t2']
           review = msg.lower()
           review = review.strip().lower()
           review = cleanPost(review)
           testReview = model.getTFIDF().transform([review]).toarray()
           output = '<table border=1 align=center>'
           output+='<tr><th>Algorithm Name</th></th><th>Review Sentiment</th><th>Review Result</th><th>Review</th></tr>'
           color = '<font size="" color="black">'    
           if algorithm == 'EM-SVM':
              predict = model.getSVM().predict(testReview)
              result = getResult(predict)
              sentiment = reviewSentiment(review)
              output+='<tr><td>'+color+"EM-SVM"+'</td><td>'+color+sentiment+'</td><td>'+color+result+'</td><td>'+color+msg+'</td></tr>'
           if algorithm == 'EM-NB':
              predict = model.getEMNaiveBayes().predict(testReview)
              result = getResult(predict)
              sentiment = reviewSentiment(review)
              output+='<tr><td>'+color+"EM-Naive Bayes"+'</td><td>'+color+sentiment+'</td><td>'+color+result+'</td><td>'+color+msg+'</td></tr>'
           if algorithm == 'Naive Bayes':
              predict = model.getNaiveBayes().predict(testReview)
              result = getResult(predict)
              sentiment = reviewSentiment(review)
              output+='<tr><td>'+color+"Naive Bayes"+'</td><td>'+color+sentiment+'</td><td>'+color+result+'</td><td>'+color+msg+'</td></tr>'
           if algorithm == 'SVM':
              predict = model.getSVM().predict(testReview)
              result = getResult(predict)
              sentiment = reviewSentiment(review)
              output+='<tr><td>'+color+"SVM"+'</td><td>'+color+sentiment+'</td><td>'+color+result+'</td><td>'+color+msg+'</td></tr>'
        print(output)   
        return render_template("ViewResult.html", msg = output)   
                  
  

@app.route("/index")
def index():
    return render_template("index.html")
    

if __name__ == "__main__":
    app.run(host ="localhost", port = int("5000"))
