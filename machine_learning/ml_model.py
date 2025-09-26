import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

# Read the CSV file
df = pd.read_csv('machine_learning/walmart.csv')



# Preprocessing function for features
from sklearn.impute import SimpleImputer
def preprocess_data(X):
	# One-hot encode categorical features
	X = pd.get_dummies(X)
	# Impute missing values with mean
	imputer = SimpleImputer(strategy='mean')
	X_imputed = pd.DataFrame(imputer.fit_transform(X), columns=X.columns)
	return X_imputed

# Assume the last column is the target, others are features
X = df.iloc[:, :-1]
y = df.iloc[:, -1]
X = preprocess_data(X)

# Split into train and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Create and train the linear regression model
model = LinearRegression()
model.fit(X_train, y_train)

# Predict on the test set
y_pred = model.predict(X_test)

# Print first 5 predictions
print("Predictions:", y_pred[:5])