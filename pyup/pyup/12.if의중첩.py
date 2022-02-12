#문제에 따라 if의 종속문장에서 if를 다시 사용할 수 있다.
#if[    ]:
#   if[    ]:
#       [ 종속문장 ]

#A를 입력받고, A가 10보다 작은 짝수인지 판별하는 프로그램

#sol1)
A = int(input("A 입력 : "))

if A < 10:
    if A % 2 == 0:
        print("짝수")
    print("10보다 작다.")

#sol2) 
A = int(input("A 입력 : "))

if A < 10 and A % 2 == 0:
    print("A는 10보다 작은 짝수이다.")



