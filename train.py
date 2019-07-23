# Daniel Holmes
# 2019/07/22
# train.py
# train, score and save a model

import joblib
import os
from sklearn.ensemble import AdaBoostClassifier
from data.get import pipeline
from data.COMBINATIONS import rankenstein as features
from models.score import confusion_matrix_df, percent_scores

# Get the Data
X_train, X_test, y_train, y_test = pipeline(features, 'score', 30000, .25)

# Train the model
model = AdaBoostClassifier(algorithm='SAMME.R', learning_rate=0.1, n_estimators=250)
model.fit(X_train, y_train)

# Score predictions
y_pred = model.predict(X_test)

print(percent_scores(y_test, y_pred))
print(confusion_matrix_df(y_test, y_pred, model.classes_))

# Save the model
if input('Save model [y/n]? ').lower() == 'y':
    name = input('Name: ')
    joblib.dump(model, os.path.join('models', name) + '.joblib')




