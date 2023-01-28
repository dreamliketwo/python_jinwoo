'''
while반복문
<문법>
while 조건:
    참일 때 실행할 코드
조건이 참이면 아래코드룰 실행
조건이 거짓이면 while 종료
무한 반복 가능
'''
# while 3>2:
#     print("토요일")
# while True:
#     print ("일요일")
# while False:
#     print("월요일")
# i=101
# while i<121:
#     print(i)
#     i+=1
# for i in range(101,121):
#         print(i)
# i=1
# while i<11:
#     if i%2==0:
#         print(i)
#     i+=1
i=100
while i<201:
    if i%2==0:
        if i%3==0:
            if i%5==0:
                print(i)
    i+=1
for i in range(100,201):
    if i%2==0:
        if i%3==0:
            if i%5==0:
                print(i)

