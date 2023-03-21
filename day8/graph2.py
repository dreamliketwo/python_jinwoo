# import matplotlib.pyplot as plt
# plt.figure()
x1=[]
y1=[]
# x2=[]
# y2=[]
for i in range(-10,11):
    x1.append(i)
    y1.append(i**2)
#     x2.append(i)
#     y2.append(-i**3)

# plt.plot(x1,y1)
# plt.show()
# b=[]
# for i in range(2,5):
#     b.append(i)

# print(b)
import matplotlib.pyplot as plt
figure,axes=plt.subplots(2,2)
fruits=["apple","banana","blueberry","orange"]
counts=[4,6,5,10]
bar_color=["red","yellow","blue","orange"]
barh_color=["black"]
bari_color=["red"]
barr_color=["green"]
axes[0,0].plot(x1,y1,'go')
axes[0,1].barh(fruits,counts,color=bari_color)
axes[1,0].barh(fruits,counts,color=barh_color)
axes[1,1].bar(fruits,counts,color=bar_color)
plt.show()