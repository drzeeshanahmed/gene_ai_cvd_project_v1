sns.set(style="whitegrid", palette="muted")

genomic_heart_df_melt = pd.melt(genomic_heart_df, id_vars = "Type",
                                    var_name = "features",
                                    value_name = "value")

plt.figure(figsize=(30,30))
sns.swarmplot(x="features", y="value", hue="Type", data=genomic_heart_df_melt, color = "#4169E1")
plt.xticks(rotation=90)