cvd_features = ["FGF2","TEK","GJB6","CD34","ENO2","CALD1","LEMD3","GLMN","ATP2A2","TRPV1","SMUG1","MB","KANTR","CD40LG","ZBTB8OS","DDX41","PDPN"
                    ,"SLC2A1","FADD","FLNA","HBA1", "Type"]
genomic_cvd_df = cvd_df[cvd_features]

genomic_cvd_df.head()

X_cvd = genomic_cvd_df[["FGF2","TEK","GJB6","CD34","ENO2","CALD1","LEMD3","GLMN","ATP2A2","TRPV1","SMUG1","MB","KANTR","CD40LG","ZBTB8OS","DDX41","PDPN"
                    ,"SLC2A1","FADD","FLNA","HBA1"]]
y_cvd = genomic_cvd_df["Type"]

X_cvd_train,X_cvd_test, y_cvd_train,y_cvd_test = train_test_split(X_cvd, y_cvd, test_size=0.3)
X_cvd_train.head()

rf1 = RandomForestRegressor(random_state=0)
rf1.fit(X_cvd_train,y_cvd_train)

feature_tpm_selector1 = RFECV(rf1,cv=5,scoring="neg_mean_squared_error") #5-fold Cross Validation to make sure
feature_tpm_selector1.fit(X_cvd_train,y_cvd_train)

f_i = list(zip(["FGF2","TEK","GJB6","CD34","ENO2","CALD1","LEMD3","GLMN","ATP2A2","TRPV1","SMUG1","MB","KANTR","CD40LG","ZBTB8OS","DDX41","PDPN"
                    ,"SLC2A1","FADD","FLNA","HBA1"],rf1.feature_importances_))
f_i.sort(key = lambda x : x[1])

from matplotlib.pyplot import figure

plt.figure(figsize = (10,10))
plt.barh([x[0] for x in f_i],[x[1] for x in f_i], color = '#AB4242')