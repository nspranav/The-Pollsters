#%%
import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from scipy import sparse
from os.path import expanduser
#%%
stop_words = [word.strip() for word in open('stop_words.txt').readlines()]

with open('dems.txt', 'r') as file:
    dem_text = [line.strip('\n') for line in file]

with open('gop.txt', 'r') as file:
    gop_text = [line.strip('\n') for line in file]

vectorizer = CountVectorizer(input=dem_text + gop_text,
                             stop_words=stop_words,
                             max_features=1200)
dem_bow = vectorizer.fit_transform(dem_text)
gop_bow = vectorizer.fit_transform(gop_text)

#%%
(dem_bow.shape, gop_bow.shape)
#%%
x = sparse.vstack((dem_bow, gop_bow))
ones = np.ones(200)
zeros = np.zeros(200)
y = np.hstack((ones, zeros))

#%%
from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.25, random_state=42)

#%%
from sklearn.naive_bayes import BernoulliNB
naive_bayes = BernoulliNB()
model = naive_bayes.fit(x_train, y_train)

#%%
y_predictions = model.predict(x_test)
#%%
y_predictions, y_test

#%%
from sklearn.metrics import accuracy_score
accuracy_score(y_test, y_predictions)

#%%
