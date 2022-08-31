genomic_cvd_df=genomic_cvd_df.apply(lambda x: pd.to_numeric(x, errors='ignore'))
genomic_cvd_df_reduce = genomic_cvd_df[["FGF2","TEK","GJB6","CD34","ENO2","CALD1","LEMD3","GLMN","ATP2A2","TRPV1","SMUG1","MB","KANTR","CD40LG","ZBTB8OS","DDX41","PDPN"
                    ,"SLC2A1","FADD","FLNA", "Type"]]

sns.set(style="whitegrid", palette="muted")

genomic_cvd_df_melt = pd.melt(genomic_cvd_df_reduce, id_vars = "Type",
                                    var_name = "features",
                                    value_name = "value")

plt.figure(figsize=(100,100))
sns.swarmplot(x="features", y="value", hue="Type", data=genomic_cvd_df_melt, color = '#AB4242')
plt.xticks(rotation=90)