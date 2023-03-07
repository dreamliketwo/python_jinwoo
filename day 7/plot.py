'''
그래프 그리기
모듈 설치
-터미널 창에서 커맨드 이용
-pip install 모듈 이름
-pip list
-matplotlid'''

import matplotlib.pyplot as plt


plt.figure()
plt.plot([0,1,2],[0,1,2],'r',[0,1,2],[0,1,4],'g')
plt.xlabel("height")
plt.ylabel("weight")
plt.show()