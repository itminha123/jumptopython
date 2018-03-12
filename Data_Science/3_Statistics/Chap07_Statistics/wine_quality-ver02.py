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
# print(wine.head())
# # data.head() - 불러온 데이터의 첫 4개 행을 프린트합니다.
# # 10개 행을 원하면 10을 괄호안에 넣으면 됩니다. data.head(10)
#
# print(wine.describe())
# """
# count = 관측값 갯수
# mean = 평균
# std = 표준편차
# min = 최소값
# 25% = 25번째 백분위수
# 50% = 중앙값
# 75% = 75번째 백분위수
# max = 최대값
# """
# print(sorted(wine.quality.unique()))
# #[3, 4, 5, 6, 7, 8, 9] = quality 중복값 제거
# print(wine.quality.value_counts())
# # 각 유일값에 해당하는 해당 갯수

# print(wine.groupby('type')[['quality']].describe())
# Red와 White 를 구분하여 quality 열의 요약 통계를 출력
# groupby 함수는 type 열의 두값을 그룹화(여기서는 Red, White)
# describe 함수는 세로 방향으로 출력
# unstack 함수는 결과를 가로방향으로 재 구조화
"""
      quality                                             
        count      mean       std  min  25%  50%  75%  max
type                                                      
red    1599.0  5.636023  0.807569  3.0  5.0  6.0  6.0  8.0
white  4898.0  5.877909  0.885639  3.0  5.0  6.0  6.0  9.0
"""

# print(wine.groupby('type')[['quality']].describe().unstack('type'))
# Red와 White 를 구분하여 quality 열의 요약 통계를 출력
# groupby 함수는 type 열의 두값을 그룹화(여기서는 Red, White)
# describe 함수는 세로 방향으로 출력
# unstack 함수는 결과를 가로방향으로 재 구조화
"""
                type 
quality  count  red      1599.000000
                white    4898.000000
         mean   red         5.636023
                white       5.877909
         std    red         0.807569
                white       0.885639
         min    red         3.000000
                white       3.000000
         25%    red         5.000000
                white       5.000000
         50%    red         6.000000
                white       6.000000
         75%    red         6.000000
                white       6.000000
         max    red         8.000000
                white       9.000000
dtype: float64
"""
print(wine.groupby('type')[['quality']].quantile([0.25, 0.75]).unstack('type'))
# quantile 함수를 이용 quality 열의 25번째, 75번째 백분위수를 출력