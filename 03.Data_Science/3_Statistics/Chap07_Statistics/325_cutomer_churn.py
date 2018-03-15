import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import statsmodels.api as sm
import statsmodels.formula as smf

churn = pd.read_csv('churn.csv', sep=',', header=0)

churn.columns = [heading.lower() for heading in
                 churn.columns.str.replace(' ','_').str.replace("\'","").str.strip('?')]

churn['churn01'] = np.where(churn['churn'] == 'True.', 1., 0.)

churn['total_charges']= churn['day_charge'] + churn['eve_charge'] + \
                        churn['night_charge'] + churn['intl_charge']

dependent_variable = churn['churn01']
independent_variables = churn[['account_length', 'custserv_calls', 'total_charges']]
independent_variables_with_constant = sm.add_constant(independent_variables, prepend=True)
logit_model = sm.Logit(dependent_variable, independent_variables_with_constant).fit()

# 기존 데이터셋의 첫 10개 값을 가지고 '새로운' 관측값 데이터셋을 만듦
new_observations = churn.ix[churn.index.isin(range(10)), independent_variables.columns]
new_observations_with_constant = sm.add_constant(new_observations, prepend=True)
y_predicted = logit_model.predict(new_observations_with_constant)
y_predicted_rounded = [round(score, 2) for score in y_predicted]
print(y_predicted_rounded)