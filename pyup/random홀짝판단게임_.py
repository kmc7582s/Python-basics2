import random    
import os
import time

life = 5
score = 0

while True:
    if life == 0:
        print("Game Over")
        break
    N = random.randint(10,99)
    print("현재 목숨", life,"현재 점수",score)
    user = int(input("input 홀(0), 짝(1) : "))

    if N % 2 == 0:
        if user == 0:
            life -= 1
            print("틀렸습니다.")
        else:
            score += 100
            print("맞았습니다.")
    else:
        if user == 0:
            score += 100
            print("맞았습니다.")
        else:
            life -= 1
            print("틀렸습니다.")   

    print("컴퓨터의 숫자는",N,"이었습니다.")
    print()
    time.sleep(1)
    os.system('cls')

print("총 점수 :",score)