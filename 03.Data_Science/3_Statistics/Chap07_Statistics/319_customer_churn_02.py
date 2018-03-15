import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import statsmodels.api as sm
import statsmodels.formula as smf

churn = pd.read_csv('churn.csv', sep=',', header=0)

churn.columns = [heading.lower() for heading in
                 churn.columns.str.replace(' ','_').str.replace("\'","").str.strip('?')]

# intl_plan 와 vmail_plan 열에 대한 이진형 지시변수를 만들고,
# churn 열과 병합하여 새로운 데이터프레임을 생성하기
intl_dummies = pd.get_dummies(churn['intl_plan'], prefix='intl_plan')
vmail_dummies = pd.get_dummies(churn['vmail_plan'], prefix='vmail_plan')
churn_with_dummies = churn[['churn']].join([intl_dummies, vmail_dummies])
print(churn_with_dummies.head())