import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import SGDClassifier
from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
from sklearn.feature_extraction.text import TfidfTransformer

df = pd.read_csv('./TextClassData.csv')
df = df.sample(frac=1).reset_index(drop=True) # Shuffle
df = df.applymap(lambda s:s.upper() if type(s) == str else s) # Convert everything to upper


labels_dict = {"Label": {'COMPANY': 0, 'ADDRESS': 1, 'LOCATION': 2, 'SERIAL': 3, 'GOOD': 4}}
df = df.replace(labels_dict)

my_map = {'COMPANY': 0, 'ADDRESS': 1, 'LOCATION': 2, 'SERIAL': 3, 'GOOD': 4}
val_to_label = dict(map(reversed, my_map.items()))

X = df.Text
y = df.Label

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3)

my_tags = ['ADDRESS', 'COMPANY', 'LOCATION', 'SERIAL', 'GOOD']

sgd = Pipeline([('vect', CountVectorizer()),
                ('tfidf', TfidfTransformer()),
                ('clf', SGDClassifier(loss='hinge', penalty='l2',alpha=1e-3, random_state=42, max_iter=5, tol=None)),
               ])
sgd.fit(X_train, y_train)

def classify(sample_input):
    pred = val_to_label[sgd.predict([sample_input])[0]]
    print("Predicted label for", sample_input, "is:", pred)
    return pred.lower()

# y_pred = sgd.predict(X_test)

# print('accuracy %s' % accuracy_score(y_pred, y_test))
# print(classification_report(y_test, y_pred,target_names=my_tags))

# inputs = ["Plastic Bottle", "Dining Table", "4 Watermill Way, Feltham, TW13 5NG", "Marks and Spencers LTD", "Slough SE12 3XY", "United Kingdom", "LSG4455-rew-fd78fffd"]
# for sample_input in inputs:
#     pred = val_to_label[sgd.predict([sample_input])[0]]
#     print('{:<8} => {:<15}'.format(pred, sample_input))

# from sklearn.naive_bayes import MultinomialNB
# from sklearn.pipeline import Pipeline
# from sklearn.feature_extraction.text import TfidfTransformer

# nb = Pipeline([('vect', CountVectorizer()),
#                ('tfidf', TfidfTransformer()),
#                ('clf', MultinomialNB()),
#               ])
# nb.fit(X_train, y_train)

# from sklearn.metrics import classification_report
# y_pred = nb.predict(X_test)

# print('accuracy %s' % accuracy_score(y_pred, y_test))
# print(classification_report(y_test, y_pred,target_names=my_tags))

# from sklearn.ensemble import RandomForestClassifier
# from sklearn.pipeline import Pipeline
# from sklearn.feature_extraction.text import TfidfTransformer

# rfc = Pipeline([('vect', CountVectorizer()),
#                ('tfidf', TfidfTransformer()),
#                ('clf', RandomForestClassifier()),
#               ])
# rfc.fit(X_train, y_train)

# from sklearn.metrics import classification_report
# y_pred = rfc.predict(X_test)

# print('accuracy %s' % accuracy_score(y_pred, y_test))
# print(classification_report(y_test, y_pred,target_names=my_tags))

# from sklearn.svm import SVC
# from sklearn.pipeline import Pipeline
# from sklearn.feature_extraction.text import TfidfTransformer

# svc = Pipeline([('vect', CountVectorizer()),
#                ('tfidf', TfidfTransformer()),
#                ('clf', SVC()),
#               ])
# svc.fit(X_train, y_train)

# from sklearn.metrics import classification_report
# y_pred = svc.predict(X_test)

# print('accuracy %s' % accuracy_score(y_pred, y_test))
# print(classification_report(y_test, y_pred,target_names=my_tags))

# from sklearn.ensemble import GradientBoostingClassifier
# from sklearn.pipeline import Pipeline
# from sklearn.feature_extraction.text import TfidfTransformer

# gbc = Pipeline([('vect', CountVectorizer()),
#                ('tfidf', TfidfTransformer()),
#                ('clf', GradientBoostingClassifier(learning_rate=0.1, n_estimators=400)),
#               ])
# gbc.fit(X_train, y_train)

# from sklearn.metrics import classification_report
# y_pred = gbc.predict(X_test)

# print('accuracy %s' % accuracy_score(y_pred, y_test))
# print(classification_report(y_test, y_pred,target_names=my_tags))

# from sklearn.ensemble import ExtraTreesClassifier
# from sklearn.pipeline import Pipeline
# from sklearn.feature_extraction.text import TfidfTransformer

# etc = Pipeline([('vect', CountVectorizer()),
#                ('tfidf', TfidfTransformer()),
#                ('clf', ExtraTreesClassifier(n_estimators=200)),
#               ])
# etc.fit(X_train, y_train)

# from sklearn.metrics import classification_report
# y_pred = etc.predict(X_test)

# print('accuracy %s' % accuracy_score(y_pred, y_test))
# print(classification_report(y_test, y_pred,target_names=my_tags))

# from sklearn.linear_model import LogisticRegression
# from sklearn.pipeline import Pipeline
# from sklearn.feature_extraction.text import TfidfTransformer

# logr = Pipeline([('vect', CountVectorizer()),
#                ('tfidf', TfidfTransformer()),
#                ('clf', LogisticRegression(n_jobs=1, C=1e5)),
#               ])
# logr.fit(X_train, y_train)

# from sklearn.metrics import classification_report
# y_pred = logr.predict(X_test)

# print('accuracy %s' % accuracy_score(y_pred, y_test))
# print(classification_report(y_test, y_pred,target_names=my_tags))