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

def inverse_logit(model_formula):
	from math import exp
	return (1.0 / (1.0 + exp(-model_formula)))*100.0

cust_serv_mean = float(logit_model.params[0]) + \
                 float(logit_model.params[1]) * float(churn['account_length'].mean()) + \
                 float(logit_model.params[2]) * float(churn['custserv_calls'].mean()) + \
                 float(logit_model.params[3]) * float(churn['total_charges'].mean())

cust_serv_mean_minus_one = float(logit_model.params[0]) + \
                           float(logit_model.params[1]) * float(churn['account_length'].mean()) + \
                           float(logit_model.params[2]) * float(churn['custserv_calls'].mean() - 1.0) + \
                           float(logit_model.params[3]) * float(churn['total_charges'].mean())

print(cust_serv_mean)
print(churn['custserv_calls'].mean() - 1.0)
print(cust_serv_mean_minus_one)
print("Probability of churn when account length changes by 1: %.2f" % (
inverse_logit(cust_serv_mean) - inverse_logit(cust_serv_mean_minus_one)))