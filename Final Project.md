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



#### Outlier Investigation


