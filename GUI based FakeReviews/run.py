from Model import Model
from LoadModels import LoadModels
from string import punctuation
from nltk.corpus import stopwords
import nltk
from nltk.stem import WordNetLemmatizer
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer


lm = LoadModels()
model = Model()
lm.loadModel(model)

#msg = "place was nice and food was good recomend this hotel for anyone who is looking for a nice vacation"
msg = "place was nice and food was good but only limited opening hours , the lobby is very nice location is decent"

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

review = msg.lower()
review = review.strip().lower()
review = cleanPost(review)
testReview = model.getTFIDF().transform([review]).toarray()
predict = model.getSVM().predict(testReview)
print(review+' CLASSIFIED AS '+getResult(predict))
predict = model.getSVM().predict(testReview)
print(review+' CLASSIFIED AS '+getResult(predict))
predict = model.getEMNaiveBayes().predict(testReview)
print(review+' CLASSIFIED AS '+getResult(predict))
predict = model.getNaiveBayes().predict(testReview)
print(review+' CLASSIFIED AS '+getResult(predict))

