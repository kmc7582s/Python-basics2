import random
import os
import time

life = 5
score = 0


while True:

    if life == 0:
        print("GAME OVER !!")
        print("내 점수 :",score)
        break
    
    N = random.randint(10,99)
    print("현재 목숨 :",life, "\t현재점수:",score)
    user = (input("홀(1)? 짝(0)? "))

    if N % 2 == 0:
        if user == 0:
            score += 100
            print("맞았습니다.")
        else:
            life -= 1
            print("틀렸습니다.")
    else:
        if user == 1:
            score += 100
            print("맞았습니다.")
        else:
            life -= 1
            print("틀렸습니다.")
    print("원래 수는", N,"이었습니다.")


    time.sleep(1)
    os.system("cls")

