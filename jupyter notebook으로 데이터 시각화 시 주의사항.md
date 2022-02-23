## jupyter notebook으로 데이터 시각화 시 주의사항

> jupyter notebook으로 데이터 시각화를 진행할 때 고려할 점들에 대해 설명하는 문서입니다. 



### 1. matplotlib

> matplotlib 사용 시 그래프가 코드 실행 시 바로 보이게 하고 싶다면 라이브러리들을 import하는 가장 마지막 줄에 아래 코드를 추가해야 합니다. 

```python
%matplotlib inline
```

