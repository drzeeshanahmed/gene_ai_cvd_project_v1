f,ax = plt.subplots(figsize=(18, 18))
sns.heatmap(genomic_cvd_df.corr(), annot=True, linewidths=.5, fmt= '.1f',ax=ax, cmap = LinearSegmentedColormap.from_list('rg',[ "black", "#AB4242"], N=256), 
                        linecolor = 'black')
best_genes_cvd = [ "FLNA", "ATP2A2", "LEMD3", "ENO2", "GLMN", "SLC2A1", "DDX41", "Type"]

genomic_cvd_df_1 = genomic_cvd_df[best_genes_cvd]
f,ax = plt.subplots(figsize=(18, 18))
sns.heatmap(genomic_cvd_df_1.corr(), annot=True, linewidths=.5, fmt= '.1f',ax=ax, cmap = LinearSegmentedColormap.from_list('rg',[ "black", "#AB4242"], N=256), 
                        linecolor = 'black')

