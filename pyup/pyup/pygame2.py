import random

while True:
    print("="*20)
    print("1. 쉬움(한자리)")
    print("2. 보통(두자리)")
    print("3. 어려움(세자리)")
    print("="*20)
    level = int(input("난이도 선택 :"))

    if level == 1:
        life = 3
        N = random.randint(1,9)
    elif level == 2:
        life = 6
        N = random.randint(10, 99)
    elif level == 3:
        life = 10
        N = random.randint(100,999)

    count = 0

    while True:
        if count == life:
            print("GAME OVER!!")
            break
        print("♥"*(life-count)+"♡"*count)
        user = int(input("숫자입력 : "))
        if N > user:
            print("Up")
        elif N < user:
            print("Down")
        else:
            print("Corret !!!")
            break
        count += 1

    print("계속하시겠습니까?")
    선택 = int(input("예(1) 아니오(0) ?"))
    if 선택 == 0:
        print("프로그램 종료!!")
        break 