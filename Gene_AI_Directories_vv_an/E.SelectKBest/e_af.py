chisq_selected_features = SelectKBest(score_func = chi2, k = 7)
fit = chisq_selected_features.fit(X_tpm_train, y_train)
dfscores = pd.DataFrame(fit.scores_)
dfcolumns = pd.DataFrame(X_tpm_train.columns)
featuresScores = pd.concat([dfcolumns, dfscores], axis = 1)
featuresScores.columns = ['Genomic Feature', 'Score']
print(featuresScores.nlargest(7,'Score'))