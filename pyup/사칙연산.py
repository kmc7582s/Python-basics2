# 두 수와 연산자를 입력받고 사칙연산 결과를 출력하는 프로그램을 작성하세요.
# (연산자에 이상한 값이 들어가면 "연산자가 이상해요" 라고 출력하도록 하세요)
#A, B=map(int, input().split())
A = int(input("수 입력 : "))
B = int(input("수 입력 : "))
op = input("연산자 입력 (+,-,*,/) : ")

if op == "+":
    print(A + B)
elif op == "-":
    print(A - B)
elif op == "*":
    print(A * B)
elif op == "/":
    print(A/B)
else:
    print("연산자가 이상해요.")