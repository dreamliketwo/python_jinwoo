'''python
for 3가지
숫자 1
for i in range(10)
범위 (숫자2)
for i in range(0,10)
범우ㅣ,증감(숫자3)
for i in range(0,10,1) '''
if예제
apple=10
orange=20
if apple>orange:
    print("사과가 큼")
else:
    print("오랜지가 큼")
math=100
english=1000
if math>english:
    print("수학을 더 잘함")
elif math>english:
    print("영어를 더 잘함")
else math=english:
    print("영어 수학 비슷")
for i in range(3):
    print("안녕")
for i in range(10):
    print(i+1)
for i in range(1,11):
    print(i)
for i in range(1,11):
    if(i%2==0):
        print(i)
sum=0

for i in range(10,21):
    if i%3==0:
        sum+=i
print(sum)
su=0
sum=0

for i in range(1,101):
    if (i%2==0):
        sum+=i
    elif (i%2==1):
        su+=i
print(sum-su)

for i in range(50,81):
    if (i%3==0):
        if (i%4==0):
            print(i)
sum=1

for i in range(1,21):
    if (i%5==0):
        sum*=i
print(sum)