chisq_selected_features = SelectKBest(score_func = chi2, k = 7)
fit = chisq_selected_features.fit(X_cvd_train, y_cvd_train)
dfscores_cvd = pd.DataFrame(fit.scores_)
dfcolumns_cvd = pd.DataFrame(X_cvd_train.columns)
featuresScores_1 = pd.concat([dfcolumns_cvd, dfscores_cvd], axis = 1)
featuresScores_1.columns = ['Genomic Feature', 'Score']
print(featuresScores_1.nlargest(7,'Score'))
#HBA1, FLNA, ATP2A2, DDX41, LEMD3, ENO2, FADD
#LEMD3, ATP2A2, FLNA, TRPV1, GLMN, SLC2A1, ENO2

#Common: FLNA, ATP2A2, LEMD3, ENO2
#Throw-in: HBA1, SLC2A1, DDX41