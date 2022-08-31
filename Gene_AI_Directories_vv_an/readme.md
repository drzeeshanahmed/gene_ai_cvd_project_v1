# Gene AI CVD Source Code

### Source Code 
Main source code is Listed at: CVD_AF_HF_sourceCode.ipynb
All unoperated data listed at: AF_Data.csv, CVD_Data.csv, HF_Data.csv (folder names explained below):
    - Atrial Fibrilation --> AF 
    - Cardio-Vascular Disease --> CVD 
    - Heart-Failure Disease --> HF 

## Sub-Folder Distribution Explained

- Each Folder has 3 python code snips that are demarcated by the [folder_name]_[cvd_name].py (e.g. a_cvd.py)
- All of the Data Preprocessing for all three cvds are split in subdirectory A & D
    - All Environment Loading & Data Preprocessing occurs in A 
    - All genomic dataset preparation occurs in D

### Main Focus per Distribution
- A: Random Forest Regression on Clinical Submatrix
- B: SelectKBest algorithm, with chi-square test scoring metric, on Clinical Submatrix
- C: Visualize a Swarm Plot on Clinical Submatrix 
- D: Random Forest Regression, Recursive Feature Elimination & Cross Validation on genomic Submatrix
- E: SelectKBest algorithm, with chi-square test scoring metric, on genomic Submatrix
- F: Visualize a swarm plot on genomic submatrix 
- G: Visualize genomic submatrix into a correlation heatmap
- H: Confusion Matrix for Type I & II errors 

### Results 
- Each Folder, other than B & E Contain image results to reference while B & E output a pandas dataframe 
