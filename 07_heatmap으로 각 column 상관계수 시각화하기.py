# 각 column의 상관관계를 색깔로 시각화하는 heatmap을 보여주는 함수

# 라이브러리 불러오기
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 샘플 데이터프레임 만들기
sample_df = pd.DataFrame(data={'언어':[88, 76, 45, 95, 82], '수리':[35, 89, 77, 56, 84], '외국어':[100, 97, 80, 95, 73], '사회탐구':[50, 45, 32, 27, 46]})

# 각 column간의 상관계수 구하기
sample_df.corr()

# 상관계수 시각화하기
plt.figure(figsize=(20, 20)) # 시각화할 공간 크기 설정
sns.heatmap(data=sample_df.corr(), annot=True, fmt='.2f', linewidths=.5, cmap='Blues')
