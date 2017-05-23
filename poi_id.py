#!/usr/bin/python

import sys
import pickle
sys.path.append("../tools/")

from feature_format import featureFormat, targetFeatureSplit
from tester import dump_classifier_and_data

### Task 1: Select what features you'll use.
### features_list is a list of strings, each of which is a feature name.
### The first feature must be "poi".
features_list = ['poi',
                 'salary',
                 #'deferral_payments',
                 #'total_payments',
                 #'loan_advances',
                 'bonus',
                 #'restricted_stock_deferred',
                 #'deferred_income',
                 #'total_stock_value',
                 #'expenses',
                 #'exercised_stock_options',
                 #'other',
                 #'long_term_incentive',
                 #'restricted_stock',
                 #'director_fees',
                 #'expenses_to_salary',
                 #'stock_value_to_salary',
                 'bonus_proportion',
                 # Now add in the email features
                 #'to_messages',
                 #'email_address',
                 #'from_poi_to_this_person',
                 #'from_messages',
                 #'from_this_person_to_poi',
                 'shared_receipt_with_poi',
                 'email_to_poi_proportion',
                 ]
        
### Load the dictionary containing the dataset
with open("final_project_dataset.pkl", "r") as data_file:
    data_dict = pickle.load(data_file)

### Task 2: Remove outliers

## Remove the first and major outlier identified in lesson 7
data_dict.pop("TOTAL")

## Remove the other non-employee outlier based on the insider pay pdf
data_dict.pop("THE TRAVEL AGENCY IN THE PARK")

### Task 3: Create new feature(s)

# Employee expenses to salary ratio
for employee, features in data_dict.iteritems():
    if features['expenses'] == "NaN" or features['salary'] == "NaN":
        features['expenses_to_salary'] = "NaN"
    else:
        features['expenses_to_salary'] = float(features['expenses']) / float(features['salary'])
        
# Employee total stock value to salary ratio        
for employee, features in data_dict.iteritems():
    if features['total_stock_value'] == "NaN" or features['salary'] == "NaN":
        features['stock_value_to_salary'] = "NaN"
    else:
        features['stock_value_to_salary'] = float(features['total_stock_value']) / float(features['salary'])        

# Bonus as a proportion of salary        
for employee, features in data_dict.iteritems():
        if features['bonus'] == "NaN" or features['salary'] == "NaN":
                features['bonus_proportion'] = "NaN"
        else:
                features['bonus_proportion'] = float(features['bonus']) / float(features['salary'])

# email_to_poi_proportion
for employee, features in data_dict.iteritems():
        if features['from_this_person_to_poi'] == "NaN" or features['from_messages'] == "NaN":
                features['email_to_poi_proportion'] = "NaN"
        else:
                features['email_to_poi_proportion'] = float(features['from_this_person_to_poi']) / float(features['from_messages'])

### Store to my_dataset for easy export below.
my_dataset = data_dict

### Extract features and labels from dataset for local testing
data = featureFormat(my_dataset, features_list, sort_keys = True)
labels, features = targetFeatureSplit(data)

### Task 4: Try a varity of classifiers
### Please name your classifier clf for easy export below.
### Note that if you want to do PCA or other multi-stage operations,
### you'll need to use Pipelines. For more info:
### http://scikit-learn.org/stable/modules/pipeline.html

# Provided to give you a starting point. Try a variety of classifiers.
from sklearn.naive_bayes import GaussianNB
from sklearn.preprocessing import MinMaxScaler
from sklearn.feature_selection import SelectKBest
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.pipeline import Pipeline

# Setting out the steps for my pipeline

scaler = MinMaxScaler()
select = SelectKBest()
nvb = GaussianNB()
dect = DecisionTreeClassifier()
knn = KNeighborsClassifier()

steps = [
        #('min_max_scaler', scaler),
        ('feature_selection', select),
        #('nvb', nvb),
        ('dect', dect),
        #('knn', knn)
        ]

# Setting up the pipeline
pipeline = Pipeline(steps)
parameters = dict(
                  feature_selection__k=[5],
                  dect__criterion=['gini'],
                  #detc__splitter=['random'],
                  #dect__max_leaf_nodes = [None],
                  dect__max_depth=[2],
                  dect__min_samples_split=[2],
                  #dect__min_samples_leaf=[1],
                  #dect__min_weight_fraction_leaf=[0],
                  dect__class_weight=['balanced'],
                  dect__presort=[True],
                  dect__random_state=[42]
                  #knn__algorithm=['auto'],              
                  #knn__n_neighbors=[5],
                  #knn__leaf_size=[1, 10, 30, 60]
                  #knn__p=[1]
                  #knn_metric_params=[None]
                  #knn__weights['uniform']
                  )

### Task 5: Tune your classifier to achieve better than .3 precision and recall 
### using our testing script. Check the tester.py script in the final project
### folder for details on the evaluation method, especially the test_classifier
### function. Because of the small size of the dataset, the script uses
### stratified shuffle split cross validation. For more info: 
### http://scikit-learn.org/stable/modules/generated/sklearn.cross_validation.StratifiedShuffleSplit.html

from sklearn.cross_validation import train_test_split, StratifiedShuffleSplit
from sklearn.grid_search import GridSearchCV
from sklearn.metrics import classification_report

# Create training sets and test sets
features_train, features_test, labels_train, labels_test = \
    train_test_split(features, labels, test_size=0.3, random_state=42)


# Cross-validation ahead of grid search
sss = StratifiedShuffleSplit(
    labels_train,
    n_iter = 20,
    test_size = 0.5,
    random_state = 0
    )

# Use grid search to Create, fit, and make predictions

gs = GridSearchCV(pipeline,
                      param_grid=parameters,
                      scoring="f1",
                      cv=sss,
                      error_score=0)
gs.fit(features_train, labels_train)
labels_predictions = gs.predict(features_test)


# Pick the classifier with the best tuned parameters
clf = gs.best_estimator_
print "\n", "Best parameters to use are: ", gs.best_params_, "\n"

# Checking features selected and their importances

features_selected=[features_list[i+1] for i in clf.named_steps['feature_selection'].get_support(indices=True)]
scores = clf.named_steps['feature_selection'].scores_
importances = clf.named_steps['dect'].feature_importances_
import numpy as np
indices = np.argsort(importances)[::-1]
print 'The ', len(features_selected), " features selected and their importances:"
scores = clf.named_steps['feature_selection'].scores_
importances = clf.named_steps['dect'].feature_importances_
import numpy as np
indices = np.argsort(importances)[::-1]
print 'The ', len(features_selected), " features selected and their importances:"
for i in range(len(features_selected)):
    print "feature no. {}: {} ({}) ({})".format(i+1,features_selected[indices[i]],importances[indices[i]], scores[indices[i]])

    
# Print classification report to get precision and recall
#report = classification_report(labels_test, labels_predictions)
#print(report)

### Task 6: Dump your classifier, dataset, and features_list so anyone can
### check your results. You do not need to change anything below, but make sure
### that the version of poi_id.py that you submit can be run on its own and
### generates the necessary .pkl files for validating your results.

dump_classifier_and_data(clf, my_dataset, features_list)