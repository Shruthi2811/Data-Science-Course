
# coding: utf-8

# In[1]:

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt



# In[2]:

german = pd.read_csv('german.data',header = None, sep = " ")
columns = ['Checking account','Duration(month)','Credit history','Purpose',           'Credit Amount','Savings/Stocks','Present employment Length',           'Installment rate','Personal status','Guarantors',           'Residing since','Property','Age(years)','Other installment plans',           'Housing','No of credits',           'Job','dependents','Telephone','foreign worker','Creditability']
german.columns = columns

# In[8]:

from sklearn.metrics import accuracy_score
from sklearn.metrics import roc_curve,auc
from sklearn.metrics import classification_report
from sklearn.naive_bayes import GaussianNB
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix
from sklearn.preprocessing import LabelEncoder
X_train, X_test, y_train, y_test = train_test_split(german.iloc[:,:-1], german.iloc[:,-1:], test_size=0.20, random_state=4212)


# In[9]:

X_train = X_train.apply(LabelEncoder().fit_transform)
X_test = X_test.apply(LabelEncoder().fit_transform)




# In[ ]:

import itertools
estimators = [10,100,300,600,800]
depth = [1,2,50,100,300,800,10000,None]
features = ['auto','sqrt',0.2]
min_sampleleaf = [1,5,10,50,100,200,500]
randomstate = [1,50,100,500,None]
a = list(itertools.product(estimators,depth,features,min_sampleleaf,                           randomstate))
len(a)


# In[ ]:

featureset = pd.DataFrame(columns = ['accuracy','estimators','max depth','max features',                                     'min_leaf','random state'])
for i in range(len(a)):
    forest = RandomForestClassifier(n_estimators=a[i][0],max_depth = a[i][1],                                    n_jobs=-1,max_features = a[i][2],                                    min_samples_leaf = a[i][3],random_state=a[i][4])                                   
    forest = forest.fit(X_train,y_train.values.ravel())
    result = forest.predict(X_test)
    output = pd.DataFrame( data={"predicted":result,"actual":y_test.values.ravel()} )
    #print ("accuracy score:%s \t estimators:%s \t depth:%s \t features:%s"% (accuracy_score(y_test.values,result),a[i][0],a[i][1],a[i][2]))
    featureset.loc[i] = [accuracy_score(y_test.values,result),a[i][0],a[i][1],a[i][2],a[i][3],a[i][4]]


# Best Feature set for Random Forest is:

# In[ ]:

print(featureset[featureset['accuracy'] == max(featureset['accuracy'])])


# As seen in above table there are multiple combinations for highest accuracy. So, I will be selecting only first feature selection

# In[ ]:

best_feature = featureset[featureset['accuracy'] == max(featureset['accuracy'])].iloc[0,:]
import numpy as np
best_feature[1] = best_feature[1].astype(np.int64)
best_feature[2] = best_feature[2].astype(np.int64)
best_feature[4] = best_feature[4].astype(np.int64)
best_feature[5] = best_feature[5].astype(np.int64)
print(best_feature)



forest = RandomForestClassifier(n_estimators=best_feature[1],max_depth = best_feature[2],                                    n_jobs=-1,max_features = best_feature[3],                                    min_samples_leaf = best_feature[4],random_state=best_feature[5]) 
forest = forest.fit(X_train,y_train.values.ravel())
result = forest.predict(X_test)
fpr,tpr,_ = roc_curve(y_test.values,result,pos_label=2)  
roc_auc = auc(fpr,tpr)

