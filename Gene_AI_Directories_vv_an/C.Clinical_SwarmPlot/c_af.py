sns.set(style="whitegrid", palette="muted")


clinical_atrial_df_melt = pd.melt(clinical_atrial_df, id_vars = "Type",
                                    var_name = "features",
                                    value_name = "value")

plt.figure(figsize=(10,10))
sns.swarmplot(x="features", y="value", hue="Type", data=clinical_atrial_df_melt, edgecolor='black', color = '#32CD32')
plt.xticks(rotation=90)