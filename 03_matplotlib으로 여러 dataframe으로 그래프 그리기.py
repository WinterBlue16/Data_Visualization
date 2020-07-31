# 다수의 dataframe 한 번에 표시하는 기본 코드를 학습한다
# 월별로 나누어져 있는 data를 쪼개어 여러 개의 dataframe을 생성하면, 그 결과를 한 번에 확인하고 싶을 때가 있다.
# 그럴 때 가장 기본적으로 사용할 수 있는 코드이다.

# 라이브러리 불러오기
import matplotlib.pyplot as plt
import pandas as pd

# dataframe 만들기
df1 = pd.DataFrame(data={'라면 종류': ['신라면', '삼양라면', '불닭볶음면', '너구리', '열라면'], '선호도' : [5, 2, 1, 3, 3]})
df2 = pd.DataFrame(data={'추가 메뉴':['치즈', '스팸', '소시지', '계란', '사리'], '선호도' : [2, 3, 2, 4, 4]})

# matplotlib으로 시각화하기(막대그래프)
 fig, ax = plt.subplots(1, 2, figsize=(20, 5)) # 1행 2열

 ax[0].bar(df1['라면 종류'], df1['선호도']) # bar=막대그래프, x축, y축
 ax[1].bar(df2['추가 메뉴'], df2['선호도'])

 plt.show()

 # matplotlib으로 시각화하기(꺾은선그래프)
  fig, ax = plt.subplots(1, 2, figsize=(20, 5)) # 1행 2열

  ax[0].plot(df1['라면 종류'], df1['선호도']) # bar=막대그래프, x축, y축
  ax[1].plot(df2['추가 메뉴'], df2['선호도'])

  plt.show()
