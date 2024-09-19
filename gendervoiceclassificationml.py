import pandas as pd
train_df= pd.read_csv('gender-voice-train.csv')
test_df= pd.read_csv('gender-voice-test.csv')

print("The number of rows and columns in train dataframe", train_df.shape)
print("The number of rows and columns in test dataframe", test_df.shape)

#checking for null values
res_df1=train_df.isnull()
for i in res_df1:
  if i==True:
    print("The value is missing at: ",i)

res_df2=test_df.isnull()
for k in res_df2:
  if k==True:
    print("The value is missing at: ",k)

#counting the number of male and female labelled voices in the dataframe
train_df_label= train_df.iloc[:,0]
print("The count of 'female' and 'male' classes in the test dataframe: \n",train_df_label.value_counts())

test_df_label= test_df.iloc[:,0]
print("The count of 'male' and 'female' classes in the test dataframe: \n",test_df_label.value_counts())

#feature variables from the 'train_df' DataFrame.
x_train= train_df.iloc[:,1:]
#feature variables from the 'test_df' DataFrame.
x_test= test_df.iloc[:,1:]

#target variable from the 'train_df' DataFrame.
y_train= train_df.iloc[:,0]
#target variable from the 'test_df' DataFrame.
y_test= test_df.iloc[:,0]

#building a Random Forest Classifier model.
from sklearn.ensemble import RandomForestClassifier 
from sklearn.metrics import confusion_matrix as c_m 
from sklearn.metrics import classification_report as c_r
#predicting the target variables based on the feature variables of the test DataFrame.
rf_clf= RandomForestClassifier(n_jobs=-1, n_estimators=50)
rf_clf.fit(x_train, y_train)
rf_clf.score(x_train, y_train)
y_predicted = rf_clf.predict(x_test)
y_predicted = pd.Series(y_predicted)
print(y_predicted.head())
#printing the confusion matrix to see the number of TN, FN, TP and FP values.
print(c_m(y_test, y_predicted))
#printing the precision, recall and f1-score values for both the male and female classes.
print(c_r(y_test, y_predicted))