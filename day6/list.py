'''
리스트
-열거형 변수를 나타내는 자료구조 중 하나
열거형변수=기차
-리스트는 대괄호를 이용함
.리스트안의 값들을 쉼표로 구분함
<특1>
리스트 안의 요소는 대괄호로 접근할 수 있음(indeing)
-왼쪽부터 0번쨰임
-오른쪽부터 -1번째임
<특징>
빈 리스트 만들수 있음
ex)a=[]
<특징3>
요소를 추가할때는 append 메소드를 이용함
.단,맨 뒤에만 추가됨.
<특징4>
요소를 뺄때는 pop메소드를 이용함
.단,맨 마지막 요소만 재거됨
<특징5>
요소값을 이용해서 제거할 때는 remove 메소드 사용함. 
<특징6>
오름차순 정렬할때는 sort 메소드를 사용
정렬:오름차순[1,2,3,4]
     내림차순[4,3,2,1]
     [2,4,1,3]
<특징7>
내림차순 정렬할 때는 reverse 메소드 사용
'''
a=10
b="인기"
c=["사과","귤","바나나"]
d=[1,2,3,4]
e=["사과",2,"귤",4]
# print(a)
# print(b)
# print(c)
# print(d)
# print(e)
# print(c[0])
# print(c[1])
# print(c[2])
# print(c[-1])
# print(c[-2])
# print(c[-3])
# print(d[1]**d[2])
# print(d[-1]%d[1])
# 민기=[]
# print(민기)
# 민기.append("말 안들음")
# print(민기)
# 민기.append("공부도 안함(노 팩트)")
# print(민기)
# 민기.pop("ㅎㅎㅎㅎㅎㅎㅎㅎㅎㅎㅎㅎㅎㅎㅎㅎㅎㅎㅎㅎㅎㅎㅎㅎㅎㅎㅎㅎㅎㅎㅎㅎㅎㅎㅎㅎㅎㅎㅎㅎㅎㅎ")
# print(민기)
# 진우=["뺀질","블랙","모자"]
# print(진우)
# 진우.pop()
# print(진우)
# 진우.remove("뺀질")
# print(진우)
num=[2,4,1,3]
print(num)
num.sort()
print(num)
fruit=["watermelon","orange","apple","banana"]
print(fruit)
fruit.sort()
print(fruit)
num.reverse()
print(num)
fruit.reverse()
print(fruit)