# 다수의 dataframe 한 번에 표시할 때 제목을 붙이는 방법에 대해 학습한다

# 라이브러리 불러오기
import matplotlib.pyplot as plt
import pandas as pd

# dataframe 만들기
df1 = pd.DataFrame(data={'라면 종류': ['신라면', '삼양라면', '불닭볶음면', '너구리', '열라면'], '선호도' : [5, 2, 1, 3, 3]})
df2 = pd.DataFrame(data={'추가 메뉴':['치즈', '스팸', '소시지', '계란', '사리'], '선호도' : [2, 3, 2, 4, 4]})

# matplotlib으로 시각화하기(막대그래프)
 fig, ax = plt.subplots(1, 2, figsize=(20, 5)) # 1행 2열

 ax[0].set_title('나의 라면 상표 선호도')
 ax[0].bar(df1['라면 종류'], df1['선호도']) # bar=막대그래프, x축, y축
 ax[1].set_title('추가 메뉴 선호도')
 ax[1].bar(df2['추가 메뉴'], df2['선호도'])

 plt.show()
