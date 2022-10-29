import pandas as pd
from sklearn.tree import DecisionTreeClassifier
data_set = pd.DataFrame(pd.read_excel("Output/DataSet.xls"))
X = data_set.drop(columns=["angle", "flow_rate","servo_angle"])
print(data_set)
# print(X)
y = data_set["angle"]
model = DecisionTreeClassifier()
model.fit(X.values, y.values)
predictions = model.predict([[ 4, 1, 2.3]])
print(predictions)