heart_features = ["ADRB1","EPO","AMPD1","MMP2",
                    "NPR1","PIK3C2A","EDN1","NR3C2","ACE","NOS3","CORIN","HSPB7"
                    ,"ANKRD1","MYH7","IL6","MYBPC3","NPPA","CDKN2B-AS1","UTS2","NPPC","VCL"
                    ,"ADRB2","TNF","ADM","MME","CST3","LGALS3", "Type"]
genomic_heart_df = heart_df[heart_features]

genomic_heart_df.head()

X_heart = genomic_heart_df[["ADRB1","EPO","AMPD1","MMP2",
                    "NPR1","PIK3C2A","EDN1","NR3C2","ACE","NOS3","CORIN","HSPB7"
                    ,"ANKRD1","MYH7","IL6","MYBPC3","NPPA","CDKN2B-AS1","UTS2","NPPC","VCL"
                    ,"ADRB2","TNF","ADM","MME","CST3","LGALS3"]]
y_heart = genomic_heart_df["Type"]

X_heart_train,X_heart_test, y_heart_train,y_heart_test = train_test_split(X_heart, y_heart, test_size=0.3)
X_heart_train.head()

rf1 = RandomForestRegressor(random_state=0)
rf1.fit(X_heart_train,y_heart_train)

feature_tpm_selector1 = RFECV(rf1,cv=5,scoring="neg_mean_squared_error") #5-fold Cross Validation to make sure
feature_tpm_selector1.fit(X_heart_train,y_heart_train)
rf1 = RandomForestRegressor(random_state=0)
rf1.fit(X_heart_train,y_heart_train)

feature_tpm_selector1 = RFECV(rf1,cv=5,scoring="neg_mean_squared_error") #5-fold Cross Validation to make sure
feature_tpm_selector1.fit(X_heart_train,y_heart_train)

f_i = list(zip(["ADRB1","EPO","AMPD1","MMP2",
                    "NPR1","PIK3C2A","EDN1","NR3C2","ACE","NOS3","CORIN","HSPB7"
                    ,"ANKRD1","MYH7","IL6","MYBPC3","NPPA","CDKN2B-AS1","UTS2","NPPC","VCL"
                    ,"ADRB2","TNF","ADM","MME","CST3","LGALS3"],rf1.feature_importances_))
f_i.sort(key = lambda x : x[1])

from matplotlib.pyplot import figure

plt.figure(figsize = (10,10))
plt.barh([x[0] for x in f_i],[x[1] for x in f_i])