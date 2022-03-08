# 수를 입력받고 절대값을 출력하는 프로그램

from re import A


N = int(input("수 입력 : "))

if N < 0:
    print("절대값은",-A)
else:
    print("절대값은",A)