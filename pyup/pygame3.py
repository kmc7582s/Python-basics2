import random
import os
import time

print("="*20)
print("1. 쉬움(한자리수)")
print("2. 보통(두자리수)")
print("3. 하드(세자리수)")
print("="*20)
level = int(input("난이도 선택 :"))

if level == 1:
    r1 = 1
    r2 = 9
elif level == 2:
    r1 = 10
    r2 = 99
elif level == 3:
    r1 = 100
    r2 = 999

life = 5
score = 0

while True:

    if life <= 0:
        print("니 점수",score)
        print("GAME OVER!!")
        break
    
    A = random.randint(r1,r2)
    B = random.randint(r1,r2)
    op = random.randint(0,1) # 0 이면 덧셈문제, 1 이면 뺄셈 문제
    s200 = random.randint(1,5) # 1이면 200점짜리 문제로 만들래
    l2 = random.randint(1,4) # 1이면 life -2

    print("현재 목숨 :",life,"\t현재 점수 :",score)
    
    if s200 == 1:
        점수 = 200
        print("이번에는 200점 짜리 문제입니다.")
    else:
        점수 = 100

    if l2 == 1:
        라이프 = 2
        print("이번에 못맞추면 life -2")
    else:
        라이프 = 1

    if op == 0:
        print(A,"+",B,"=", end= " ")
        정답 = A+B
    elif op == 1:
        if A > B:
            print(A,"-",B,"=", end= " ")
            정답 = A - B
        else:
            print(B,"-",A,"=", end= " ")
            정답 = B - A

    user = int(input())

    if user == 정답:
        score += 점수
        print("맞췄습니다 :)")
    else:
        life -= 라이프
        print("틀렸습니다 :(")
    time.sleep(0.7)
    os.system("cls")

    print("계속하시겠습니까?")
    선택 = int(input("예(1) 아니오(0) ?"))
    if 선택 == 0:
        print("프로그램 종료!!")
        break 
