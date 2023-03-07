# 진우=[]
# for i in range(1,21):
#     if i%3==0:
#         진우.append(i)
# 진우.reverse()
# print(결과)
# 결과=[]
# for i in range(1,11):
#     if i%4!=0:
#         결과.append(i)
# 결과.reverse()
# print(결과)

# def 구구단(num):
#     결과=[]
#     for i in range(1,10):
#         결과.append(num*i)
#     결과.reverse()
#     print(결과)


# 구구단(3)
# 구구단(7)
def 짝수(num):
    결과=[]
    for i in range(1,num*2+1):
        if i%2==0:
            결과.append(i)
    결과.reverse()
    print(결과)
짝수(3)
짝수(6)
짝수(4)