import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import statsmodels.api as sm
import statsmodels.formula.api as smf
from statsmodels.formula.api import ols, glm

# 데이터 셋을 pandas dataframe으로 읽기 (csv파일이라서)
wine = pd.read_csv('winequality-both.csv', sep=',', header=0)
# print(wine.columns)
"""
Index(['type', 'fixed acidity', 'volatile acidity', 'citric acid',
       'residual sugar', 'chlorides', 'free sulfur dioxide',
       'total sulfur dioxide', 'density', 'pH', 'sulphates', 'alcohol',
       'quality'],
      dtype='object')
"""
wine.columns = wine.columns.str.replace(' ', '_')
# str을 안붙이면 AttributeError: 'Index' object has no attribute 'replace' 에러가 뜸
# print(wine.columns)
"""
Index(['type', 'fixed_acidity', 'volatile_acidity', 'citric_acid',
       'residual_sugar', 'chlorides', 'free_sulfur_dioxide',
       'total_sulfur_dioxide', 'density', 'pH', 'sulphates', 'alcohol',
       'quality'],
      dtype='object')
"""
# print(wine.head())
# data.head() - 불러온 데이터의 첫 4개 행을 프린트합니다.
# 10개 행을 원하면 10을 괄호안에 넣으면 됩니다. data.head(10)

# print(wine.describe())
# 각각의 속성 값에 해당하는 값들의 표현
"""
count = 관측값 갯수
mean = 평균
std = 표준편차
min = 최소값
25% = 25번째 백분위수
50% = 중앙값
75% = 75번째 백분위수
max = 최대값
"""
print(sorted(wine.quality.unique()))
#[3, 4, 5, 6, 7, 8, 9] = quality의 중복값  제거하고 유일값(unique) 추출
print(wine.quality.value_counts())
# 각 유일값에 해당하는 해당 갯수