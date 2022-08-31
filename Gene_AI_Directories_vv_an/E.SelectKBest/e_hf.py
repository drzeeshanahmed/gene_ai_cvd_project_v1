chisq_selected_features = SelectKBest(score_func = chi2, k = 7)
fit = chisq_selected_features.fit(X_heart_train, y_heart_train)
dfscores = pd.DataFrame(fit.scores_)
dfcolumns = pd.DataFrame(X_heart_train.columns)
featuresScores = pd.concat([dfcolumns, dfscores], axis = 1)
featuresScores.columns = ['Genomic Feature', 'Score']
print(featuresScores.nlargest(7,'Score'))
#NR3C2, P1K3C2A, MME, VCL, ACE, LGALS3, MYBPC3, CORIN
#MME, VCL, LGALS3, ADM, PIK3C2A, NR3C2, ADRB2

#Common: NR3C2, P1K3C2A, MME, VCL

featuresScores.to_csv(r'HeartFailure/HFGenomicResults/HF_chi2results.csv', index = False)