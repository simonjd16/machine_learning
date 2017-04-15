# Identify Fraud from Enron Email

#### By Simon Dickson

## 1. Summarize for us the goal of this project and how machine learning is useful in trying to accomplish it. As part of your answer, give some background on the dataset and how it can be used to answer the project question. Were there any outliers in the data when you got it, and how did you handle those?  [relevant rubric items: “data exploration”, “outlier investigation”]

At it's height, Enron Corporation was one of the worlds largest electircity, natural gas, communications and pulp and paper companies employing around 20,000 staff and reporting revenues of over $100 billion. This all collapese in the run up to the corporation declaring bankrupcy on December 2nd 2001. The collapse was primarily instigated by institutionalised, systematic and creatively planned accounting fraud.

The goal of this project is to use the publicly available Enron financial and email datasets to identify individuals who may of comnmited fraud. During the project, these individuals will be known as persons of interest (POI's) who by definition were "individuals who were indicted, reached a settlement, or plea deal with the government, or testified in exchange for prosecution immunity"

### Data Exploration

#### Allocation across classes (POI/Non-POI)

- Employees: There are 146 Enron employees within the public data sets. Out of these 146, 18 of them are POI's.

#### Number of features

- POI feature: There is one boolean feature to identify if a particular employee is a POI or not
  - poi
- Financial features: There are 14 features within the financial data set. The currency for all units are in USD
  - salary
  - deferral_payments
  - total_payments
  - load_advances
  - bonus
  - restricted_stock_deferred
  - deferred_income
  - total_stock_value
  - expenses
  - exercised_stock_options
  - other
  - long_term_incentive
  - restricted_stock
  - director_fees
  
- Email features: There are 6 features within the email data set.
  - to_messages
  - email_address
  - from_poi_to_this_person
  - from_messages
  - from_this_person_to_poi
  - shared_receipt_with_poi

#### Features with missing values

Using list comprehension I reviewed all 21 features within the dataset.

From the financial features (including the POI identifier) all features apart from the POI identifier had missing values present. The 3 features with the lowest population were loan_advances (2.74% population), director_fees (11.64% population) and restricted_stock_deferred (12.33% population) 

From the email features, all features have missing values present, but all features have above 58.90% population.

#### Outlier Investigation

Based on the work completed in previous lessons running to the completion of this project, we identified a speadsheet querk where a row labelled "TOTAL" was being included. I used data_dict.pop to remove this outlier. 

Upon reviewing the FindLaw insider pay pdf, there was also one additonal row which for "THE TRAVEL AGENCY IN THE PARK" These were not payments to a specific individual but payments on an account of business-related travel. I have also excluded these payments again using data_dict.pop.

## 2. What features did you end up using in your POI identifier, and what selection process did you use to pick them? Did you have to do any scaling? Why or why not? As part of the assignment, you should attempt to engineer your own feature that does not come ready-made in the dataset -- explain what feature you tried to make, and the rationale behind it. (You do not necessarily have to use it in the final analysis, only engineer and test it.) In your feature selection step, if you used an algorithm like a decision tree, please also give the feature importances of the features that you use, and if you used an automated feature selection function like SelectKBest, please report the feature scores and reasons for your choice of parameter values.  [relevant rubric items: “create new features”, “properly scale features”, “intelligently select feature”]

