genomicandtarget_features = ['SCN1B', 'NPPA-AS1', 'KCNQ1', 'KCNE1', 'VKORC1', 'ATF4', 'KCNH2', 'SELP', 'PDE4D', 'ACE', 'PRKAR1B', 'NUP155',
           'CYP4F2', 'ABCC9', 'KCNJ2-AS1', 'CFAP20', 'KCNJ2', 'MYBPC3', 'KCNE3', 'PF4', 'PPBP', 'MYL4', 'Type']
genomic_atrial_df = atrial_df[genomicandtarget_features]

genomic_atrial_df.head()

X_tpm = genomic_atrial_df[['SCN1B', 'NPPA-AS1', 'KCNQ1', 'KCNE1', 'VKORC1', 'ATF4', 'KCNH2', 'SELP', 'PDE4D', 'ACE', 'PRKAR1B', 'NUP155',
           'CYP4F2', 'ABCC9', 'KCNJ2-AS1', 'CFAP20', 'KCNJ2', 'MYBPC3', 'KCNE3', 'PF4', 'PPBP', 'MYL4']]
y_tpm = genomic_atrial_df['Type']

X_tpm_train,X_tpm_test, y_train,y_test = train_test_split(X_tpm, y_tpm, train_size = 0.8, test_size=0.2)
X_tpm_train.head()

rf1 = RandomForestRegressor(random_state=0)
rf1.fit(X_tpm_train,y_train)

feature_tpm_selector1 = RFECV(rf1,cv=5) #5-fold Cross Validation to make sure
feature_tpm_selector1.fit(X_tpm_train,y_train)

f_i = list(zip(['SCN1B', 'NPPA-AS1', 'KCNQ1', 'KCNE1', 'VKORC1', 'ATF4', 'KCNH2', 'SELP', 'PDE4D', 'ACE', 'PRKAR1B', 'NUP155',
           'CYP4F2', 'ABCC9', 'KCNJ2-AS1', 'CFAP20', 'KCNJ2', 'MYBPC3', 'KCNE3', 'PF4', 'PPBP', 'MYL4'],rf1.feature_importances_))
f_i.sort(key = lambda x : x[1])

from matplotlib.pyplot import figure

plt.figure(figsize = (10,10))
plt.barh([x[0] for x in f_i],[x[1] for x in f_i], color = '#32CD32')