'''
함수
미리 만들어서 반복된 작업을 할 때 사용
1.만드는 작업
2.사용하는 작업 
<문법1>
def 함수이름 ():
    내용 작성
<문법2>
def 함수이름(입력값):
    입력값을 이용한 내용 작성
    입력값이 여러개면 쉼표로 구분
<문법3>
def 함수이름(입력값):
    입력값을 이용한 내용 작성
    return출력값
출력값이 여러개면 쉼표로 구분'''
# def 진우():
#     print("정진우 입니다.")
# def 진우2(반복횟수):
#     for i in range(반복횟수):
#         print("정진우예요")

# 진우2(5)
# 진우2(3)
# def 거듭제곱(아래숫자,윗숫자):
#     결과=아래숫자**윗숫자
#     return 결과

# print(거듭제곱(2,3))
# print(거듭제곱(2,4))
# print(거듭제곱(2,10))
def 삼각형넓이(밑변,높이):
    결과=밑변*높이/2
    return 결과

print(삼각형넓이(5,4)) 
print(삼각형넓이(6,10)) 

def 구구단(e):
    for i in range(10):
        print(e*i)

구구단(3)
구구단(8)

def 짝수(e):
    for i in range(2,e*2+1):
        if(i%2==0):
            print(i)
        

짝수(3)
짝수(10)