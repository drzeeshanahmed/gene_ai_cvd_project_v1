heart_df = pd.read_csv("HF_Data.csv")
heart_df.head()

heart_df.fillna('Other',inplace=True)

heart_df.describe()

print(heart_df['Gender'].unique())
print(heart_df['Race'].unique())
print(heart_df['Age'].unique())

heart_df.loc[heart_df['Race'] == 'White ', 'Race'] = 'White'

heart_df.loc[heart_df['Race'] == 'Other', 'Race'] = 6
heart_df.loc[heart_df['Race'] == 'White', 'Race'] = 1
heart_df.loc[heart_df['Race'] == 'Black', 'Race'] = 2
heart_df.loc[heart_df['Race'] == 'Asian', 'Race'] = 19
heart_df.loc[heart_df['Race'] == 'Decline to Answer', 'Race'] = 7

heart_df.loc[heart_df['Gender'] == 'Other', 'Gender'] = 999
heart_df.loc[heart_df['Gender'] == 'Female', 'Gender'] = 1
heart_df.loc[heart_df['Gender'] == 'Male', 'Gender'] = 2

le = preprocessing.LabelEncoder()
le.fit(heart_df['Type'])
heart_df['Type'] = le.transform(heart_df['Type'])

clinicalandtarget_features = ['Gender', 'Race', 'Age', 'Type']
clinical_heart_df = heart_df[clinicalandtarget_features]

clinical_heart_df.head()

clinical_hf_features = clinical_heart_df[['Gender', 'Race', 'Age']]
y = heart_df['Type']

X_c_hf_train, X_c_hf_test, y_train,y_test = train_test_split(clinical_hf_features, y, 
                                                                test_size=0.3, random_state = 42)
                                                                
X_c_hf_train.head()

rf = RandomForestRegressor(random_state=0)
rf.fit(X_c_hf_train,y_train)

f_i = list(zip(clinical_hf_features,rf.feature_importances_))
f_i.sort(key = lambda x : x[1])
plt.barh([x[0] for x in f_i],[x[1] for x in f_i])