# 데이터프레임의 전체 분포를 시각화하기
# 전체 데이터의 형태를 파악하는 데 도움을 주며, 대체적으로 데이터 분석 초기에 사용

# 라이브러리 불러오기
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 샘플 데이터프레임 만들기
sample_df = pd.DataFrame(data={'언어':[88, 76, 45, 95, 82], '수리':[35, 89, 77, 56, 84], '외국어':[100, 97, 80, 95, 73], '사회탐구':[50, 45, 32, 27, 46]})

# 시각화
sns.pairplot(data=sample_df)
plt.show()
