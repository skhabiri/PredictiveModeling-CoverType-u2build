**Forestcover-build2:** 

The dataset has 15K rows and 56 columns. Most of the columns are numerical and a few features, “Wilderness Area” and “Soil Type” have been encoded with OneHotEncoder. The target label is “Cover_Type”, which is categorical with seven numerical classes. There are some very high and very low cardinal features that will be dropped. The many encoded features “Wilderness Area” and “Soil Type” will be decoded into two categorical features for better visualization. The heatmap of the correlation matrix shows the dependency of features to each other. Pairplot of Soil_Type and “Wilderness Area” vs an unrelated feature show how those features are able to separate the target. A countplot and distplot shows the distribution of features and labels, and shows the amount of skew in the distribution. The data is split into X and y and train and val and highly imbalanced features are dropped. Since all the target labels are balanced the base model shows 1/7 prediction accuracy. For this work we compare the scores of LogisticRegression(), RidgeClassifier(), RandomForestClassifier(), GradientBoostingClassifier(), XGBClassifier(). Next we fit each estimator and get the metrics report, including confusion metrics, feature importances, permutation importances. We also explore early stopping in xgboost. Next we use validation_curve() to plot the training vs validation curve while sweeping one of the model parameters. SImilarly RandomizedSearchCV() allows to tune hyperparameters and do all of them at once instead of sweeping each parameter once at the time. After fitting the model,to evaluate the dependency of each target class labels to a particular feature, we use both partial_dependence from sklearn and pdp from pdpbox. pdp_isolate() gives pdp_values for a single feature vs each target class label, while pdp_interact() allows to evaluate multiple features codependency to each of target class labels. In pdp we can specify the number of points in the grid for better granularity. To see the effect of all features on a particular target class label in a single query, or in other words to see the local effect of each feature on each of 7 target class labels we use shap. Shap_values magnitude and signs shows the strength and direction of any feature to the target class label of interest.

**Libraries:**
```
import pandas as pd
import numpy as np
import category_encoders as ce
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import FunctionTransformer
from sklearn.impute import SimpleImputer
from sklearn.linear_model import RidgeCV
from sklearn.linear_model import RidgeClassifier
from sklearn.pipeline import make_pipeline
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.ensemble import RandomForestClassifier
from xgboost import XGBClassifier
from sklearn.model_selection import GridSearchCV, RandomizedSearchCV
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import validation_curve
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, mean_absolute_error
from sklearn.metrics import plot_confusion_matrix, classification_report, confusion_matrix
import pickle
import random 
from scipy import stats
from sklearn.inspection import permutation_importance
from sklearn.inspection import partial_dependence, plot_partial_dependence
from pdpbox import pdp
from pdpbox.pdp import pdp_interact, pdp_interact_plot
import shap
```
https://github.com/skhabiri/forestcover-metrics
