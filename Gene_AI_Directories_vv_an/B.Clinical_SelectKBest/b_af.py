chisq_selected_features = SelectKBest(score_func = chi2, k = 3)
fit = chisq_selected_features.fit(X_c_af_train, y_train)
dfscores = pd.DataFrame(fit.scores_)
dfcolumns = pd.DataFrame(X_c_af_train.columns)
featuresScores = pd.concat([dfcolumns, dfscores], axis = 1)
featuresScores.columns = ['Clinical Feature', 'Score']
print(featuresScores.nlargest(3,'Score'))