import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import statsmodels.api as sm
import statsmodels.formula as smf

#데이터셋을 데이터프레임으로 읽음
churn = pd.read_csv('churn.csv', sep=',', header=0)

churn.columns = [heading.lower() for heading in
                 churn.columns.str.replace(' ','_').str.replace("\'","").str.strip('?')]

churn['churn01'] = np.where(churn['churn'] == 'True.', 1., 0.)
print(churn.head())