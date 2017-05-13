# Identify Fraud from Enron Email

#### By Simon Dickson

## 1. Summarize for us the goal of this project and how machine learning is useful in trying to accomplish it. As part of your answer, give some background on the dataset and how it can be used to answer the project question. Were there any outliers in the data when you got it, and how did you handle those?  [relevant rubric items: “data exploration”, “outlier investigation”]

At its height, Enron Corporation was one of the world's largest electricity, natural gas, communications and pulp and paper companies employing around 20,000 staff and reporting revenues of over $100 billion. This all collapse in the run up to the corporation declaring bankruptcy on December 2nd, 2001. The collapse was primarily instigated by institutionalised, systematic and creatively planned accounting fraud.

The goal of this project is to use the publicly available Enron financial and email datasets to identify individuals who may have committed fraud. During the project, these individuals will be known as persons of interest (POI's) who were "individuals who were indicted, reached a settlement, or plea deal with the government, or testified in exchange for prosecution immunity"

### Data Exploration

#### Allocation across classes (POI/Non-POI)

- Employees: There are 146 Enron employees within the public data sets. Out of these 146, 18 of them are POI's.

#### Number of features

- POI feature: There is one boolean feature to identify if an employee is a POI or not
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

Using list comprehension, I reviewed all 21 features within the dataset.

From the financial features (including the POI identifier) all features apart from the POI identifier had missing values present. The 3 features with the lowest population were loan_advances (2.74% population), director_fees (11.64% population) and restricted_stock_deferred (12.33% population) 

From the email features, all features have missing values present, but all features have above 58.90% population.

#### Outlier Investigation

Based on the work completed in previous lessons running to the completion of this project, we identified a spreadsheet quirk where a row labelled "TOTAL" was being included. I used data_dict.pop to remove this outlier. 

Upon reviewing the FindLaw insider pay pdf, there was also one additional row which for "THE TRAVEL AGENCY IN THE PARK" These were not payments to a specific individual but payments on an account of business-related travel. I have also excluded these payments again using data_dict.pop.

## 2. What features did you end up using in your POI identifier, and what selection process did you use to pick them? Did you have to do any scaling? Why or why not? As part of the assignment, you should attempt to engineer your own feature that does not come ready-made in the dataset -- explain what feature you tried to make, and the rationale behind it. (You do not necessarily have to use it in the final analysis, only engineer and test it.) In your feature selection step, if you used an algorithm like a decision tree, please also give the feature importances of the features that you use, and if you used an automated feature selection function like SelectKBest, please report the feature scores and reasons for your choice of parameter values.  [relevant rubric items: “create new features”, “properly scale features”, “intelligently select feature”]

#### Methodology for selection process

The methodology I adopted for feature selection was a univariate selection process using select k-best from sklean. I used the k-best selection within a pipeline that included grid search to select the best features to use. The goal of this selection process was to maximise precision as well as recall.

#### Features Selected in POI identifier

The 5 features I selected are sorted in order of importance below. The values following the feature names are the feature importance followed by the feature score:

- feature no. 1: bonus (0.716358632315) (0.00998239958969)
- feature no. 2: exercised_stock_options (0.283641367685) (7.03793279819)
- feature no. 3: shared_receipt_with_poi (0.0) (30.7287746334)
- feature no. 4: total_stock_value (0.0) (8.95913664769)
- feature no. 5: salary (0.0) (15.858730906)

#### Use of Scaling

The only algorithm that I used scaling for was the k-nearest neighbours algorithm. The logic behind using scaling was that we needed to measure the distances between our sample pairs which impacts the clustering when determining the nearest neighbours.

#### Features Engineered

I decided to engineer 2 features into the data sets primarily focused around the final aspects of the data. 

- expenses_to_salary: I decided to look at the ratio between the amount of expenses the employee claimed and their salary. I wanted to explore if there may have been anything peculiar going on with the expenses for employees receiving lower salaries
- stock_value_to_salary: In the same way as the expenses_to_salary ratio, I also decided to explore if there was any significance between the total stock value an employee had versus their salary

## 3. What algorithm did you end up using? What other one(s) did you try? How did model performance differ between algorithms?  [relevant rubric item: “pick an algorithm”]



## 4. What does it mean to tune the parameters of an algorithm, and what can happen if you don’t do this well?  How did you tune the parameters of your particular algorithm? (Some algorithms do not have parameters that you need to tune -- if this is the case for the one you picked, identify and briefly explain how you would have done it for the model that was not your final choice or a different model that does utilize parameter tuning, e.g. a decision tree classifier).  [relevant rubric item: “tune the algorithm”]

## 5. What is validation, and what’s a classic mistake you can make if you do it wrong? How did you validate your analysis?  [relevant rubric item: “validation strategy”]

## 6. Give at least 2 evaluation metrics and your average performance for each of them.  Explain an interpretation of your metrics that says something human-understandable about your algorithm’s performance. [relevant rubric item: “usage of evaluation metrics”]


