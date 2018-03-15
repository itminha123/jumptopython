import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import statsmodels.api as sm
import statsmodels.formula as smf

churn = pd.read_csv('churn.csv', sep=',', header=0)

churn.columns = [heading.lower() for heading in
                 churn.columns.str.replace(' ','_').str.replace("\'","").str.strip('?')]

# 새로운 변수 total_charges를 기준으로 그룹화한 뒤, 그룹별 통계량 구하기
churn['total_charges']= churn['day_charge'] + churn['eve_charge'] + \
                        churn['night_charge'] + churn['intl_charge']
factor_cut = pd.cut(churn.total_charges, 5, precision=2)
def get_stats(group):
    return {'min': group.min(), 'max': group.max(), 'count': group.count(),
            'mean': group.mean(), 'std': group.std()}
grouped = churn.custserv_calls.groupby(factor_cut)
print(grouped.apply(get_stats).unstack())