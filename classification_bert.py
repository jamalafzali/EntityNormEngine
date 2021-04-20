import pickle
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import SGDClassifier
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
from bert_embedding import *

######################
# Data preprocessing #
######################

# Load data
df = pd.read_csv('./TextClassData.csv')
df = df.sample(frac=1).reset_index(drop=True) # Shuffle
df = df.applymap(lambda s:s.upper() if type(s) == str else s) # Convert everything to upper

# Clean labels
labels_dict = {"Label": {'COMPANY': 0, 'ADDRESS': 1, 'LOCATION': 2, 'SERIAL': 3, 'GOOD': 4}}
df = df.replace(labels_dict)

# Get reverse mapping
my_map = {'COMPANY': 0, 'ADDRESS': 1, 'LOCATION': 2, 'SERIAL': 3, 'GOOD': 4}
val_to_label = dict(map(reversed, my_map.items()))


# Split into training and test sets
X = df.Text
y = df.Label
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3)

#####################################
# Converting data to BERT embedding #
#####################################
X_train = list(map(get_embedding, X_train))
X_test = list(map(get_embedding, X_test))

# Cleaning up data
for i in range(len(X_train)):
    X_train[i] = X_train[i].numpy()
for i in range(len(X_test)):
    X_test[i] = X_test[i].numpy()

my_tags = ['ADDRESS', 'COMPANY', 'LOCATION', 'SERIAL', 'GOOD']

############
# Training #
############
sgd = SGDClassifier(loss='hinge', penalty='l2',alpha=1e-3, random_state=42, max_iter=5, tol=None)
sgd.fit(X_train, y_train)

############
# Evaluate #
############
y_pred = sgd.predict(X_test)

print('accuracy %s' % accuracy_score(y_pred, y_test))
print(classification_report(y_test, y_pred,target_names=my_tags))

inputs = ["Plastic Bottle", "M&S Limited", "Dining Table", "4 Watermill Way, Feltham, TW13 5NG", "Marks and Spencers LTD", "Slough SE12 3XY", "United Kingdom", "LSG4455-rew-fd78fffd", "NVIDIA Ireland", "Imperial College London", "Hardwood Table", "Chair", "Asia", "Japan", "123453454"]
for sample_input in inputs:
    embed = get_embedding(sample_input.upper()).numpy()
    pred = val_to_label[sgd.predict([embed])[0]]
    print('{:<8} => {:<15}'.format(pred, sample_input))

##############
# Save model #
##############
filename = 'entity_classifier.pickle'
pickle.dump(sgd, open(filename, 'wb'))