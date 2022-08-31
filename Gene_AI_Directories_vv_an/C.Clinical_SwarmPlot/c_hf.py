sns.set(style="whitegrid", palette="muted")


clinical_heart_df_melt = pd.melt(clinical_heart_df, id_vars = "Type",
                                    var_name = "features",
                                    value_name = "value")

plt.figure(figsize=(10,10))
sns.swarmplot(x="features", y=