# Import libraries
import numpy as np
from sklearn import datasets
from sklearn.model_selection import train_test_split
import os
from joblib import load
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

# Load model
clf = load(MODEL_PATH)

# Run inference
print("Predicting...")
y_pred = clf.predict(X_test[:10])
print("Predicted price by the model:", np.around(y_pred,1))
print("Ground-truth price:", y_test[:10])