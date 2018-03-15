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

#그룹별 기술 통계 구하기
print(churn.groupby(['churn'])[['day_charge', 'eve_charge', 'night_charge',
    'intl_charge', 'account_length', 'custserv_calls']].agg(['count', 'mean', 'std']))

# 변수별로 서로 다른 통계량 구하기
print(churn.groupby(['churn']).agg({'day_charge': ['mean', 'std'], 'eve_charge': ['mean', 'std'],
                                    'night_charge': ['mean', 'std'], 'intl_charge': ['mean', 'std'],
                                    'account_length': ['count', 'min', 'max'],
                                    'custserv_calls': ['count', 'min', 'max']}))

# 새로운 변수 total_charges를 기준으로 그룹화한 뒤, 그룹별 통계량 구하기
churn['total_charges']= churn['day_charge'] + churn['eve_charge'] + \
                        churn['night_charge'] + churn['intl_charge']
factor_cut = pd.cut(churn.total_charges, 5, precision=2)
def get_stats(group):
    return {'min': group.min(), 'max': group.max(), 'count': group.count(),
            'mean': group.mean(), 'std': group.std()}
grouped = churn.custserv_calls.groupby(factor_cut)
print(grouped.apply(get_stats).unstack())

#account_length 열의 사분위수를 기준으로 분할한 뒤,
#그룹별 통계량 구하기
factor_qcut = pd.qcut(churn.account_length, [0., 0.25, 0.5, 0.75, 1.])
grouped = churn.custserv_calls.groupby(factor_qcut)
print(grouped.apply(get_stats).unstack())