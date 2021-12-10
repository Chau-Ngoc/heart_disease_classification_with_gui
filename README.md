# Heart Disease Classification with GUI
Welcome to this repository. The notebook in this repository will analyze the dataset downloaded from [this Kaggle page](https://www.kaggle.com/cherngs/heart-disease-cleveland-uci) and build a classification model to predict whether a person have heart disease or not base on his/her medical status. A patient's medical status includes:
1. age: age in years
2. sex (1 = male; 0 = female)
3. cp - chest pain type (4 values)
    * Value 0: typical angina
    * Value 1: atypical angina
    * Value 2: non-anginal pain
    * Value 3: asymptomatic
4. trestbps: resting blood pressure (in mm Hg on admission to the hospital)
5. chol - serum cholestoral in mg/dl
6. fbs - fasting blood sugar > 120 mg/dl (1 = true; 0 = false)
7. restecg - resting electrocardiographic results (values 0,1,2)
    * Value 0: normal
    * Value 1: having ST-T wave abnormality (T wave inversions and/or ST elevation or depression of > 0.05 mV)
    * Value 2: showing probable or definite left ventricular hypertrophy by Estes' criteria
8. thalach - maximum heart rate achieved
9. exang - exercise induced angina (1 = yes; 0 = no)
10. oldpeak - ST depression induced by exercise relative to rest
11. slope - the slope of the peak exercise ST segment
    * Value 0: upsloping
    * Value 1: flat
    * Value 2: downsloping
12. ca - number of major vessels (0-3) colored by flourosopy
13. thal - 0 = normal; 1 = fixed defect; 2 = reversable defectage
14. target - have heart disease or not (1 = NO heart disease, 0 = HAVE heart disease)

**Note:** this notebook uses plotly library to plot some graphs. You won't be able to see those graphs if you open this notebook on Github. Instead, please open this notebook in [nbviewer](https://nbviewer.org/github/Chau-Ngoc/heart_disease_classification_with_gui/blob/main/heart_disease_classification.ipynb#top)

## GUI Window that handles Patient's Medical Status
Running window_.py file will open a window for user to input their medical status. This window implements a trained model to predict. The patient's result will return as a popup window telling them whether they have heart disease or not.

### Enjoy!