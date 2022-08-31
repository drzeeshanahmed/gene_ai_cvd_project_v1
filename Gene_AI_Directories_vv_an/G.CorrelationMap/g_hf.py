genomic_heart_df=genomic_heart_df.apply(lambda x: pd.to_numeric(x, errors='ignore'))

f,ax = plt.subplots(figsize=(18, 18))
sns.heatmap(genomic_heart_df.corr(), annot=True, linewidths=.5, fmt= '.1f',ax=ax, cmap = LinearSegmentedColormap.from_list('rg',[ "black", "#4169E1"], N=256), 
                        linecolor = 'black')

best_genes_hf = ["NR3C2", "PIK3C2A", "MME", "VCL", "MYBPC3", "ACE", "ADM", "Type"]
genomic_heart_df_1 = genomic_heart_df[best_genes_hf]

f,ax = plt.subplots(figsize=(18, 18))
sns.heatmap(genomic_heart_df_1.corr(), annot=True, linewidths=.5, fmt= '.1f',ax=ax, cmap = LinearSegmentedColormap.from_list('rg',[ "black", "#4169E1"], N=256), 
                        linecolor = 'black')