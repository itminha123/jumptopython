import pandas as pd
import numpy as np
from sklearn.tree import DecisionTreeRegressor
from sklearn import svm, metrics
import random
from sklearn.model_selection import train_test_split

housing_file_path = 'housing.csv'
housing = pd.read_csv(housing_file_path)
# print (housing.columns)

# random.shuffle(housing)

housing['housing_driveway'] = np.where(housing['driveway'] == 'yes', 1, 0)
housing['housing_recroom'] = np.where(housing['recroom'] == 'yes', 1, 0)
housing['housing_fullbase'] = np.where(housing['fullbase'] == 'yes', 1, 0)
housing['housing_gashw'] = np.where(housing['gashw'] == 'yes', 1, 0)
housing['housing_airco'] = np.where(housing['airco'] == 'yes', 1, 0)
housing['housing_prefarea'] = np.where(housing['prefarea'] == 'yes', 1, 0)

housing_price_data = housing.price
# print(housing_price_data)

csv_data = housing[['lotsize', 'bedrooms', 'bathrms', 'stories', 'housing_driveway', 'housing_recroom',
                      'housing_fullbase', 'housing_gashw', 'housing_airco', 'garagepl', 'housing_prefarea']]
csv_label = housing["price"]

#학습 전용 데이터와 데스트 전용 데이터로 나누기 ----(3)
train_data, test_data, train_label, test_label = train_test_split(csv_data, csv_label)

print(len(test_label))
#데이터 학습시키고 예측하기 ----(4)
clf = svm.SVC()
clf.fit(train_data, train_label)
pre = clf.predict(test_data)
print(len(pre))
#정답률 구하기 ----(5)
ac_score = metrics.accuracy_score(test_label, pre)
print("전체 데이터 수: %d" %(len(csv_data)))
print("학습 전용 데이터 수: %d" % len(train_data))
print("테스트 데이터 수: %d" %len(test_data))
print("정답률 =", ac_score)
# print(train_label)

A = pre
B = test_label
result_value = 0
for value in [x - y for x, y in zip(A, B)]:
    result_value += value **2
count_value = result_value / len(A)

print("Cost Function : %s" % count_value)

