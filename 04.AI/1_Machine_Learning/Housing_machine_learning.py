import pandas as pd
import numpy as np
from sklearn.tree import DecisionTreeRegressor

housing_file_path = 'housing.csv'
housing = pd.read_csv(housing_file_path)
# print (housing.columns)

housing['housing_driveway'] = np.where(housing['driveway'] == 'yes', 1, 0)
housing['housing_recroom'] = np.where(housing['recroom'] == 'yes', 1, 0)
housing['housing_fullbase'] = np.where(housing['fullbase'] == 'yes', 1, 0)
housing['housing_gashw'] = np.where(housing['gashw'] == 'yes', 1, 0)
housing['housing_airco'] = np.where(housing['airco'] == 'yes', 1, 0)
housing['housing_prefarea'] = np.where(housing['prefarea'] == 'yes', 1, 0)

housing_price_data = housing.price
# print(housing_price_data)

housing_price_datalist = []
housing_price_predict_list = []
i = 0
while True:
    if i != 500:
        housing_price_datalist.append(housing_price_data[i])
        i = i + 1
    else:
        break

housing_predictors = ['lotsize', 'bedrooms', 'bathrms', 'stories', 'housing_driveway', 'housing_recroom',
                      'housing_fullbase', 'housing_gashw', 'housing_airco', 'garagepl', 'housing_prefarea']

y = housing_price_data
x = housing[housing_predictors]

housing_model = DecisionTreeRegressor()
housing_model.fit(x, y)

t = 0
while True:
    if t != 540:
        housing_price_predict_list.append(housing_model.predict(x)[t])
        # housing_price_predict_list.append(housing_model.predict(x.head())[t])
        t = t + 1
    else:
        break
print(housing_price_predict_list)

A = housing_price_datalist
B = housing_price_predict_list
result_value = 0
for value in [x - y for x, y in zip(A, B)]:
    result_value += value **2
count_value = result_value / len(A)

print("Cost Function : %s" % count_value)

"""                  m
Cost Function = 1/m ∑ (선값(x) - 실제값(x))^2
                    i=1
"""
