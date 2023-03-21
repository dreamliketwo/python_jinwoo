'''
그래프 그리기
모듈 설치
-터미널 창에서 커맨드 이용
-pip install 모듈 이름
-pip list
-matplotlid'''

import matplotlib.pyplot as plt

6
# plt.figure()
# plt.plot([-1,1,-1,1],[-1,1,-1,1],'r',[-1,1,-1,1],[-1,1,-1,1],'g')
# plt.xlabel("height")
# plt.ylabel("weight")
# plt.show()  1   2
# import matplotlib.pyplot as plt

# plt.figure()
# x1=[0,1,2]
# y1=[0,1,2]
# x2=[0,1,2]
# y2=[0,1/2,1]
# x3=[0,1,2]
# y3=[0,2,4]
# plt.plot(x1,y1,x2,y2,x3,y3)
# plt.xlabel("height")
# plt.ylabel("weight")
# plt.show()
# import matplotlib.pyplot as plt

# plt.figure()
# x1=[-1,0]
# y1=[0,1]
# x2=[0,-1]
# y2=[-1,0]
# x3=[0,1]
# y3=[-1,0]
# x4=[0, 1]
# y4=[-1,0]
# plt.plot(x1,y1,x2,y2,x3,y3,x4,y4)
# plt.xlabel("height")
# plt.ylabel("weight")
# plt.show()
plt.figure()
x1=[]
y1=[]
for i in range(6):
    x1.append(i)
    y1.append(2*i+3)


plt.plot(x1,y1)
plt.xlabel("x")
plt.ylabel("y")
plt.show()