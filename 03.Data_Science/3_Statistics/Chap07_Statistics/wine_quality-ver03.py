import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import statsmodels.api as sm
import statsmodels.formula.api as smf
from statsmodels.formula.api import ols, glm

# 데이터 셋을 pandas dataframe으로 읽기 (csv파일이라서)
wine = pd.read_csv('winequality-both.csv', sep=',', header=0)
wine.columns = wine.columns.str.replace(' ', '_')


red_wine = wine.ix[wine['type']=='red', 'quality']
print(red_wine.value_counts())
white_wine = wine.ix[wine['type']=='white', 'quality']
#
sns.set_style("dark")
print(sns.distplot(red_wine, \
		norm_hist=True, kde=False, color="red", label="Red wine"))
print(sns.distplot(white_wine, \
		norm_hist=True, kde=False, color="blue", label="White wine"))
plt.xlabel("Quality Score")
plt.ylabel("Density")
plt.title("Distribution of Quality by Wine Type")
plt.legend()
plt.show()
#
# # 와인 종류에 따라 품질의 차이 검정
# print(wine.groupby(['type'])[['quality']].agg(['std', 'mean']))
# # 그룹별 품질의 평균과 표준편차
# tstat, pvalue, df = sm.stats.ttest_ind(red_wine, white_wine)
# print('tstat: %.3f  pvalue: %.4f' % (tstat, pvalue))
# """
#         quality
#             std      mean
# type
# red    0.807569  5.636023
# white  0.885639  5.877909
# tstat: -9.686  pvalue: 0.0000
# """

