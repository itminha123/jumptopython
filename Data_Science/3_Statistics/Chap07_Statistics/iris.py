import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import statsmodels.api as sm
import statsmodels.formula as smf
import random
#데이터셋을 데이터프레임으로 읽음

iris = pd.read_csv('iris.csv', sep=',', header=0)

iris.columns = [heading.lower() for heading in iris.columns.str.replace('.','_')]

iris['variety01'] = np.where(iris['variety'] == 'Setosa', 1., 0.)

print(iris.head())

# 그룹별 기술통계 구하기
# print(iris.groupby(['variety'])[['sepal_length', 'sepal_width', 'petal_length', 'petal_width']].agg(['count', 'mean', 'std']))


dependent_variable = iris['variety01']
independent_variables = iris[['sepal_length', 'sepal_width', 'petal_length', 'petal_width']]
independent_variables_with_constant = sm.add_constant(independent_variables, prepend=True)
logit_model = sm.Logit(dependent_variable, independent_variables_with_constant).fit_regularized()

# 기존 데이터셋의 첫 10개 값을 가지고 '새로운' 관측값 데이터셋을 만듦
new_observations = iris.ix[iris.index.isin(random.sample(range(100), 10)), independent_variables.columns]
new_observations_with_constant = sm.add_constant(new_observations, prepend=True)
y_predicted = logit_model.predict(new_observations_with_constant)
y_predicted_rounded = [round(score, 2) for score in y_predicted]
print(y_predicted_rounded)

result = []
for i in y_predicted:
    if i == 1.0 :
        result.append("Setosa")
    else:
        result.append("not Setosa")
print(result)