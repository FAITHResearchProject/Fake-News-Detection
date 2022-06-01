import pickle
import pandas as pd
from nltk.stem.porter import PorterStemmer
import re
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import CountVectorizer

port_stem = PorterStemmer()

with open('trained_model', 'rb') as file:
    model_import = pickle.load(file)


with open('Vectorizer', 'rb') as file:
    CV_data = pickle.load(file)


def stemming(content):
    stemmed = re.sub('[^a-zA-Z]',' ', content)
    stemmed = stemmed.lower()
    stemmed = stemmed.split()
    stemmed = [port_stem.stem(word) for word in stemmed if not word in stopwords.words('english')]
    stemmed = ' '.join(stemmed)
    return stemmed


def output_label(n):
    if n == 0:
        return "This news is unreliable."
    elif n == 1:
        return "This news is reliable."


def manual_testing(news):
    testing_news = {"text":[news]}
    new_def_test = pd.DataFrame(testing_news)
    new_def_test["text"] = new_def_test["text"].apply(stemming) 
    new_x_test = new_def_test["text"]
    new_xv_test = CV_data.transform(new_x_test)
    pred_LR = model_import.predict(new_xv_test)
    
    return print((output_label(pred_LR[0])))

news = str(input())
manual_testing(news)