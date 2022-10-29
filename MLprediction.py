import math
import pandas as pd
from sklearn.ensemble import RandomForestRegressor

train_set = pd.DataFrame(pd.read_excel("Output/DataSet.xls"))
X_train = train_set.drop(columns=["angle", "flow_rate","servo_angle"])
y_train = train_set["angle"]
test_set = pd.DataFrame(pd.read_excel("Output/test.xlsx"))
X_test = test_set.drop(columns=["angle", "flow_rate","servo_angle"])
y_test = test_set["angle"]
regressor = RandomForestRegressor(n_estimators = 50, random_state = 0)
regressor.fit(X_train, y_train)
y_pred = regressor.predict(X_test)


from sklearn.neural_network import MLPRegressor
#neural = MLPRegressor
# neural.fit(X_train, y_train)
from sklearn import metrics
print('Mean Absolute Error:', metrics.mean_absolute_error(y_test, y_pred))
print('Mean Squared Error:', metrics.mean_squared_error(y_test, y_pred))
print('Root Mean Squared Error:', math.sqrt(metrics.mean_squared_error(y_test, y_pred)))
# y_pred = neural.predict(X_test)
# print('Mean Absolute Error:', metrics.mean_absolute_error(y_test, y_pred))
# print('Mean Squared Error:', metrics.mean_squared_error(y_test, y_pred))
# print('Root Mean Squared Error:', math.sqrt(metrics.mean_squared_error(y_test, y_pred)))