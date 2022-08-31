sns.set(style="whitegrid", palette="muted")


clinical_cvd_df_melt = pd.melt(clinical_cvd_df, id_vars = "Type",
                                    var_name = "features",
                                    value_name = "value")

plt.figure(figsize=(10,10))
sns.swarmplot(x="features", y="value", hue="Type", data=clinical_cvd_df_melt, color = '#AB4242')
plt.xticks(rotation=90)