genomic_atrial_df=genomic_atrial_df.apply(lambda x: pd.to_numeric(x, errors='ignore'))

f,ax = plt.subplots(figsize=(18, 18))
sns.heatmap(genomic_atrial_df.corr(), annot=True, linewidths=.5, fmt= '.1f',ax=ax, cmap = LinearSegmentedColormap.from_list('rg',[ "black", "#32CD32"], N=256), 
                        linecolor = 'black')

best_genes_af = ["CYP4F2","SELP","KCNJ2","NUP155", "ATF4", "KCNE3", "MYBPC3", "Type"]
genomic_atrial_df_1 = genomic_atrial_df[best_genes_af]

f,ax = plt.subplots(figsize=(18, 18))
sns.heatmap(genomic_atrial_df_1.corr(), annot=True, linewidths=.5, fmt= '.1f',ax=ax, 
                        cmap = LinearSegmentedColormap.from_list('rg',[ "black", "#32CD32"], N=256), 
                        linecolor = 'black')

