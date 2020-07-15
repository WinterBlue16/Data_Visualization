# 시각화의 기본인 matplotlib 라이브러리를 사용해 막대 그래프를 그려보자.

# 라이브러리 불러오기
import matplotlib.pyplot as plt

# 데이터 시각화하기(꺾은선그래프)
plt.title('그래프 제목')
plt.xlabel('x축 제목')
plt.ylabel('y축 제목')
plt.bar(데이터프레임 column1, 데이터프레임 column2) #(x축, y축)

plt.show()
