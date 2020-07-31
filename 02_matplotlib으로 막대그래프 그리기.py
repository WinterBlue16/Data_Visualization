# 시각화의 기본인 matplotlib 라이브러리를 사용해 막대 그래프를 그려보자.

# 라이브러리 불러오기
import matplotlib.pyplot as plt
import pandas as pd

# 데이터프레임 만들기
df = pd.DataFrame(data={'라면 종류': ['신라면', '삼양라면', '불닭볶음면', '너구리', '열라면'], '선호도' : [5, 2, 1, 3, 3]})

# 데이터 시각화하기(꺾은선그래프)
plt.title('나의 라면 브랜드 선호도')
plt.xlabel('라면 종류')
plt.ylabel('선호도')
plt.bar(df['라면 종류'], df['선호도']) #(x축, y축)

plt.show()
