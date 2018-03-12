import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import statsmodels.api as sm
import statsmodels.formula as smf
from statsmodels.formula.api import ols, glm

housing = pd.read_csv("Housing.csv", sep=",", header=0)

housing['house_driveway'] = np.where(housing['driveway'] == 'yes', 1, 0)
housing['house_recroom'] = np.where(housing['recroom'] == 'yes', 1, 0)
housing['house_fullbase'] = np.where(housing['fullbase'] == 'yes', 1, 0)
housing['house_gashw'] = np.where(housing['gashw'] == 'yes', 1, 0)
housing['house_airco'] = np.where(housing['airco'] == 'yes', 1, 0)
housing['house_prefarea'] = np.where(housing['prefarea'] == 'yes', 1, 0)

my_formula = 'price~ lotsize + bedrooms + bathrms + stories + garagepl + house_driveway + ' \
             'house_recroom + house_fullbase + house_gashw + house_airco  + house_prefarea'

lm = ols(my_formula, data= housing).fit_regularized()

dependent_variable = housing['price']
independent_variables = housing[housing.columns.difference(['price'])]
# independent_variables_standardized = (independent_variables - independent_variables.mean()) / independent_variables.std()
print(independent_variables.mean())

new_observations = housing.ix[housing.index.isin(range(10)), independent_variables.columns]
y_predicted = lm.predict(new_observations)
y_predicted_rounded = [round(score, 2) for score in y_predicted]
print(y_predicted_rounded)


