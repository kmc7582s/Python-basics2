# 월을 입력받고, 계절을 출력하는 프로그램
mon = int(input("월 입력 : "))

# 1)
if 1<=mon<=12 :
    if 3<=mon<=5 :
        print("봄")
    elif 6<=mon<=8:
        print("여름")
    elif 9<=mon<11:
        print("가을")
    else:
        print("겨울")
else:
    print("잘못입력!")

# 2)
if 1<=mon<=12:
    mon = mon%12
    if mon<3:
        print("겨울")
    elif mon<6:
        print("봄")
    elif mon<9:
        print("여름")
    else:
        print("가을")
else:
    print("잘못입력!")

