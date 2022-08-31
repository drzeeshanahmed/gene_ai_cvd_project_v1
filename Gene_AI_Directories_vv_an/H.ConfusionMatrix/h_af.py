X_tpm_features_1 = genomic_atrial_df_1[["CYP4F2","SELP","KCNJ2","NUP155", "ATF4", "KCNE3", "MYBPC3"]]
y = genomic_atrial_df_1["Type"]

x_train, x_test, y_train, y_test = train_test_split(X_tpm_features_1, y, test_size=0.3, random_state=42)

clf_rf = RandomForestClassifier(random_state=43)      
clr_rf = clf_rf.fit(x_train,y_train)

ac = accuracy_score(y_test,clf_rf.predict(x_test))
print('Accuracy is: ',ac)
cm = confusion_matrix(y_test,clf_rf.predict(x_test))
sns.heatmap(cm,annot=True,fmt="d")