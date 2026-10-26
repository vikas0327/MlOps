from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
import joblib
from pathlib import Path


iris = load_iris()
X=iris.data
y=iris.target
x_train, x_test, y_train, y_test = train_test_split(X,y,test_size=0.2,random_state=42)

clf = RandomForestClassifier(n_estimators=100, random_state=42)

clf.fit(x_train,y_train)

# make prediction on test dataset
y_pred = clf.predict(x_test)

#calculate the accuracy
accuracy = accuracy_score(y_test,y_pred)
print(f"Accuray: {accuracy}")

# save the trained model
model_dir = Path("model")
model_dir.mkdir(parents=True,exist_ok=True)
model_path = model_dir / "iris_random_forest_model.joblib"
joblib.dump(clf, model_path)
print(f"Model saved to {model_path}")