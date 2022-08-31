cvd_df = pd.read_csv("CVD_Data.csv")
cvd_df.head()

cvd_df.describe()

cvd_df.fillna('Other',inplace=True)

cvd_df.loc[cvd_df['Race'] == 'White ', 'Race'] = 'White'

cvd_df.loc[cvd_df['Race'] == 'White ', 'Race'] = 'White'
cvd_df.loc[cvd_df['Race'] == 'Other', 'Race'] = 6
cvd_df.loc[cvd_df['Race'] == 'White', 'Race'] = 1
cvd_df.loc[cvd_df['Race'] == 'Black', 'Race'] = 2
cvd_df.loc[cvd_df['Race'] == 'Asian', 'Race'] = 19
cvd_df.loc[cvd_df['Race'] == 'Decline to Answer', 'Race'] = 7

cvd_df.loc[cvd_df['Gender'] == 'Other', 'Gender'] = 999
cvd_df.loc[cvd_df['Gender'] == 'Female', 'Gender'] = 1
cvd_df.loc[cvd_df['Gender'] == 'Male', 'Gender'] = 2

cvd_df.drop(cvd_df.index[cvd_df['Age'] == 'Other'],inplace = True)

print(cvd_df['Gender'].unique())
print(cvd_df['Race'].unique())
print(cvd_df['Age'].unique())

le = preprocessing.LabelEncoder()
le.fit(cvd_df['Type'])
cvd_df['Type'] = le.transform(cvd_df['Type'])

clinicalandtarget_features = ['Gender', 'Race', 'Age', 'Type']
clinical_cvd_df = cvd_df[clinicalandtarget_features]

clinical_cvd_df.head()

clinical_cvd_features = clinical_cvd_df[['Gender', 'Race', 'Age']]
y_cvd = cvd_df['Type']

X_c_cvd_train, X_c_cvd_test, y_cvd_train,y_cvd_test = train_test_split(clinical_cvd_features, y_cvd, 
                                                                test_size=0.3, random_state = 42)
                                                                
X_c_cvd_train.head()

rf = RandomForestRegressor(random_state=0)
rf.fit(X_c_cvd_train,y_cvd_train)

f_i = list(zip(clinical_cvd_features,rf.feature_importances_))
f_i.sort(key = lambda x : x[1])
plt.barh([x[0] for x in f_i],[x[1] for x in f_i], color = '#AB4242')

