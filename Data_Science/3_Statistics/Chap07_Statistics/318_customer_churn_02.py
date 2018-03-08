import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import statsmodels.api as sm
import statsmodels.formula as smf

churn = pd.read_csv('churn.csv', sep=',', header=0)

churn.columns = [heading.lower() for heading in
                 churn.columns.str.replace(' ','_').str.replace("\'","").str.strip('?')]

# 변수별로 서로 다른 통계량 구하기
print(churn.groupby(['churn']).agg({'day_charge': ['mean', 'std'], 'eve_charge': ['mean', 'std'],
                                    'night_charge': ['mean', 'std'], 'intl_charge': ['mean', 'std'],
                                    'account_length': ['count', 'min', 'max'],
                                    'custserv_calls': ['count', 'min', 'max']}))
