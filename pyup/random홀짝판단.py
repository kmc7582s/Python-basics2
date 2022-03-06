import random

N = random.randint(10,99)
user = int(input("input 홀(0), 짝(1) : "))

if N % 2 == 0:
    if user == 0:
        print("틀렸습니다.")
    else:
        print("맞았습니다.")
else:
    if user == 0:
        print("맞았습니다.")
    else:
        print("틀렸습니다.")

print("컴퓨터의 숫자는",N,"이었습니다.") 