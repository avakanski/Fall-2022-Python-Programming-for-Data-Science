# Import libraries
import numpy as np
from sklearn import ensemble, datasets
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
import os
from joblib import dump
import warnings
warnings.filterwarnings('ignore')

# Directory paths 
MODEL_DIR = os.environ["MODEL_DIR"]
MODEL_FILE = os.environ["MODEL_FILE"]
MODEL_PATH = os.path.join(MODEL_DIR, MODEL_FILE)

# Load and split data
print("Loading data...")
boston = datasets.load_boston()
X_train, X_test, y_train, y_test = train_test_split(boston.data,  boston.target, random_state=13, test_size=0.1)

# Fit regression model
print("Fitting model...")
clf = ensemble.GradientBoostingRegressor()
clf.fit(X_train, y_train)

# Save the model
print("Saving model to: {}".format(MODEL_PATH))
dump(clf, MODEL_PATH)