import os
import io
import re
import matplotlib.pyplot as plt
import numpy as np
from nltk.corpus import stopwords

truthful_pos = 'Dataset/positive_polarity/truthful_from_TripAdvisor/'
truthful_neg = 'Dataset/negative_polarity/truthful_from_Web/'

deceptive_pos = 'Dataset/positive_polarity/deceptive_from_MTurk/'
deceptive_neg = 'Dataset/negative_polarity/deceptive_from_MTurk/'

truthful_reviews_link = []
Y = []
unique = []
stop_words = set(stopwords.words('english'))

for fold in os.listdir(truthful_pos):
    foldLink = os.path.join(truthful_pos, fold)
    if os.path.isdir(foldLink):
        for f in os.listdir(foldLink):
            fileLink = os.path.join(foldLink, f)
            truthful_reviews_link.append(fileLink)
           
for fold in os.listdir(truthful_neg):
    foldLink = os.path.join(truthful_neg, fold)
    if os.path.isdir(foldLink):
        for f in os.listdir(foldLink):
            fileLink = os.path.join(foldLink, f)
            truthful_reviews_link.append(fileLink)
            
deceptive_reviews_link = []

for fold in os.listdir(deceptive_pos):
    foldLink = os.path.join(deceptive_pos, fold)
    if os.path.isdir(foldLink):
        for f in os.listdir(foldLink):
            fileLink = os.path.join(foldLink, f)
            deceptive_reviews_link.append(fileLink)
            
for fold in os.listdir(deceptive_neg):
    foldLink = os.path.join(deceptive_neg, fold)
    if os.path.isdir(foldLink):
        for f in os.listdir(foldLink):
            fileLink = os.path.join(foldLink, f)
            deceptive_reviews_link.append(fileLink)
                    
print('Number of truthfuls reviews ', len(truthful_reviews_link))
print('Number of deceptives reviews ', len(deceptive_reviews_link))

def clean_str(string):
    """
    Tokenization/string cleaning for all datasets except for SST.
    Original taken from https://github.com/yoonkim/CNN_sentence/blob/master/process_data.py
    """
    string = re.sub(r"[^A-Za-z0-9(),!?\'\`]", " ", string)
    string = re.sub(r"\'s", " \'s", string)
    string = re.sub(r"\'ve", " \'ve", string)
    string = re.sub(r"n\'t", " n\'t", string)
    string = re.sub(r"\'re", " \'re", string)
    string = re.sub(r"\'d", " \'d", string)
    string = re.sub(r"\'ll", " \'ll", string)
    string = re.sub(r",", " , ", string)
    string = re.sub(r"!", " ! ", string)
    string = re.sub(r"\(", " \( ", string)
    string = re.sub(r"\)", " \) ", string)
    string = re.sub(r"\?", " \? ", string)
    string = re.sub(r"\s{2,}", " ", string)
    return string.strip().lower()

def handleFile(filePath):
    with open(filePath, "r") as f:
        lines=f.readlines()
        words = ''
        for line in lines:
            cleanedLine = clean_str(line)
            cleanedLine = cleanedLine.strip()
            cleanedLine = cleanedLine.lower()
            words+=cleanedLine+" "
    return "\""+words.strip()+"\""


allFilesLinks = truthful_reviews_link + deceptive_reviews_link
vocabulary = []
numWords = []
text = 'Review,Label\n'
for fileLink in truthful_reviews_link:
    words = handleFile(fileLink)
    text+=words+",1\n"
   

for fileLink in deceptive_reviews_link:
    words = handleFile(fileLink)
    text+=words+",0\n"

f = open("dataset.csv", "w")
f.write(text)
f.close()




















