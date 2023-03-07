# # '''
# # 리수튜
# # 열거형 변수를 나타내는 자료구조 중 하나
# # <특징1> 추가하는 메소드 (맨오른쪽)
# # <특징2>뺴는 메소드(맨오른쪽)
# # <특징3>선택해서 삭제 메소드
# # <특징4>정렬 (오름 차순)(계단)
# # f=[1,3,2,4]
# # f.sort()
# # print(f)
# # g=[1,3,2,4]
# # g.reverse()
# # print(g)
# # 특8
# # 리스트와 니스트를 합칠때"+"사용
# # 특9
# # 리스트를 비울때 clear메소드 사용
# # 특10
# # 특정 위치의 값을 추가할때insert 메소드 사용
# # 특11
# # 값이 몇번째있는지 찾을 때 index 메소드사용
# # 특12
# # 리스트안에 값이 몇개인디 알아볼때 count 메소드사용
# # 특13
# # 리스트의 길이를 알고싶을때 len 함수 사용
# # 특14

# # '''
# # '''a=[1,2]
# # b=[3,4]
# # a.extend(b)
# # print(a)
# # d=[100,200]
# # d.clear()
# # print(d)
# # e=[1,2,3]
# # e.insert(1,100)
# # print(e)
# # f=[1,2,3,4,2]
# # print(f.index(2))
# # g=[1,2,3,4,2]
# # print(g.count(5))
# # h=[1,2,3,4]
# # print(len(h))
# # a=["바나나","사과","오렌지"]
# # for i in range(len(a)):
# #     print(a[i])
# # for i in a:
# #     print(i)
# # fruits=["orange","cherry","watermelon","apple","blueberry"]
# # fruits.sort()
# # fruits.reverse()

# # for i in range(len(fruits)):
# #     print(fruits[i])
# # 전번=[0,1,0,4,5,0,3,0,4,7,9]
# # 전번.clear()
# # 전번.append(0)
# # 전번.append(1)
# # 전번.append(0)
# # 전번.append(9)
# # 전번.append(8)
# # 전번.append(7)
# # 전번.append(6)
# # 전번.append(5)
# # 전번.append(4)
# # 전번.append(3)
# # print(전번)
# # 결과=[]
# # for i in range(1,21):
# #     if (i%3==0):
# #         결과.append(i)
# # 결과.reverse()
# # print(결과)
# # def 공약수(e,r):
# #     for i in range(1<e*r):
# #         min(e,r)
# #         공약수.sort
# #         print(공약수/)'''
# fruits=["orange","banana","cherry","apple"]
# # fruits.append("watermelon")
# # fruits.append("blueberry")
# # fruits.append("tomato")
# # fruits.sort()
# # fruits.reverse()
# # # print(fruits[0])
# # # print(fruits[1])
# # # print(fruits[2])
# # # print(fruits[3])
# # # a=[10,20,30]
# # # print(a)

# # # a.insert(1,100)
# # # a.insert(3,200)
# # # print(a)
# # for i in range(len(fruits)):
# #     print(fruits[i])
# for fruit in fruits:
#     print(fruit)
# o=[]
# for i in range(1,6):
#     o.append(i)
# print(o)
# for i in range(len(o)):
#     print(o[i])
# o=[]
# for i in range(1,21):
#     if (i%3==0):
#         o.append(i)
# print(o)
# o.sort()
# o.reverse()
# for i in range(len(o)):
#     print(o[i])
o=[]
for i in range(1,101):
    if (i%3==0):
        if(i%4==0):
            o.append(i)
o.sort()            
o.reverse()            
print(o)
















































































































































































































































