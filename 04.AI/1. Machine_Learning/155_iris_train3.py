import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import statsmodels.api as sm
import statsmodels.formula as smf
import random
from  sklearn import svm, metrics

iris = pd.read_csv('iris01.csv', sep=',', header=0)

iris['variety01'] = np.where(iris['Name'] == 'Iris-versicolor', 1., 0.)

# print(iris.head(100))

dependent_variable = iris['variety01']
independent_variables = iris[['SepalLength', 'SepalWidth', 'PetalLength', 'PetalWidth']]
independent_variables_with_constant = sm.add_constant(independent_variables, prepend=True)
logit_model = sm.Logit(dependent_variable, independent_variables_with_constant).fit_regularized()

# 기존 데이터셋의 첫 10개 값을 가지고 '새로운' 관측값 데이터셋을 만듦
new_observations = iris.ix[iris.index.isin(random.sample(range(100), 25)), independent_variables.columns]
new_observations_with_constant = sm.add_constant(new_observations, prepend=True)
y_predicted = logit_model.predict(new_observations_with_constant)
y_predicted_rounded = [round(score, 2) for score in y_predicted]
print(y_predicted_rounded)

result = []
versicolor = 0
for i in y_predicted_rounded:
    if i > 1.0 :
        result.append('Iris-versicolor')
    else:
        result.append('Iris-virginica')
print(result)

from sklearn.model_selection import train_test_split

csv_data = iris[["SepalLength", "SepalWidth", "PetalLength", "PetalWidth"]]
csv_label = iris["Name"]
train_data, test_data, train_label, test_label = train_test_split(csv_data, csv_label)

# print(len(test_label))
# print(train_data)

ac_score = metrics.accuracy_score(test_label , result)

print(ac_score)
