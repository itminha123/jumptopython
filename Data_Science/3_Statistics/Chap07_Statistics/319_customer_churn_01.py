import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import statsmodels.api as sm
import statsmodels.formula as smf

churn = pd.read_csv('churn.csv', sep=',', header=0)

churn.columns = [heading.lower() for heading in
                 churn.columns.str.replace(' ','_').str.replace("\'","").str.strip('?')]
def get_stats(group):
    return {'min': group.min(), 'max': group.max(), 'count': group.count(),
            'mean': group.mean(), 'std': group.std()}

#account_length 열의 사분위수를 기준으로 분할한 뒤,
#그룹별 통계량 구하기
factor_qcut = pd.qcut(churn.account_length, [0., 0.25, 0.5, 0.75, 1.])
grouped = churn.custserv_calls.groupby(factor_qcut)
print(grouped.apply(get_stats).unstack())