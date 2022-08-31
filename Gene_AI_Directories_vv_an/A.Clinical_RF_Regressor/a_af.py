#Importing Modules

#For Matrix Manipulation and Data Management
import pandas as pd
import numpy as np

#For Machine Learning and Feature Analysis
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.feature_selection import RFECV
from sklearn import preprocessing
from sklearn.feature_selection import SelectKBest
from sklearn.feature_selection import chi2
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from sklearn.metrics import f1_score,confusion_matrix

#For Data Visualization
import matplotlib.pyplot as plt
from matplotlib.pyplot import figure
import seaborn as sns

#Data Pre-Processing
atrial_df = pd.read_csv('AF_Data.csv')
atrial_df.fillna('Other',inplace=True)

atrial_df.head()
atrial_df.describe()

atrial_df.loc[atrial_df['Race'] == 'White ', 'Race'] = 'White'
atrial_df.loc[atrial_df['Race'] == 'Other', 'Race'] = 6
atrial_df.loc[atrial_df['Race'] == 'White', 'Race'] = 1
atrial_df.loc[atrial_df['Race'] == 'Black', 'Race'] = 2
atrial_df.loc[atrial_df['Race'] == 'Asian', 'Race'] = 19
atrial_df.loc[atrial_df['Race'] == 'Decline to Answer', 'Race'] = 7

atrial_df['Race'].unique()

atrial_df.loc[atrial_df['Gender'] == 'Other', 'Gender'] = 999
atrial_df.loc[atrial_df['Gender'] == 'Female', 'Gender'] = 1
atrial_df.loc[atrial_df['Gender'] == 'Male', 'Gender'] = 2

atrial_df['Gender'].unique()

atrial_df.drop(atrial_df.index[atrial_df['Age'] == 'Other'],inplace = True)

atrial_df['Age']

le = preprocessing.LabelEncoder()
le.fit(atrial_df['Type'])
atrial_df['Type'] = le.transform(atrial_df['Type'])

#Splitting into Clinical Matrix 
clinicalandtarget_features = ['Gender', 'Race', 'Age', 'Type']
clinical_atrial_df = atrial_df[clinicalandtarget_features]

clinical_atrial_df.head()

clinical_af_features = clinical_atrial_df[['Gender', 'Race', 'Age']]
y = atrial_df['Type']

X_c_af_train, X_c_af_test, y_train,y_test = train_test_split(clinical_af_features, y, 
                                                                test_size=0.3, random_state = 42)
                                                                
X_c_af_train.head()

rf = RandomForestRegressor(random_state=0)
rf.fit(X_c_af_train,y_train)

f_i = list(zip(clinical_af_features,rf.feature_importances_))
f_i.sort(key = lambda x : x[1])
plt.barh([x[0] for x in f_i],[x[1] for x in f_i],color='#32CD32')