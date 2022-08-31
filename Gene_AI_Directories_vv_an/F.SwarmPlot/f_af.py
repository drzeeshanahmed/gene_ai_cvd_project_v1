sns.set(style="whitegrid", palette="muted")

genomic_atrial_df_melt = pd.melt(genomic_atrial_df, id_vars = "Type",
                                    var_name = "features",
                                    value_name = "value")

plt.figure(figsize=(20,20))
sns.swarmplot(x="features", y="value", hue="Type", data=genomic_atrial_df_melt, color = '#32CD32')
plt.xticks(rotation=90)