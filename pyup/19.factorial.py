#<factorial(팩토리얼)>
# 팩토리얼은 수학에서 '!'라는 표시로 사용된다.
# N! = N * (N-1) * (N-2) * ... * 1 
# 곱을 축적할 떄는 *= 를 사용한다.

# 정수를 입력받고(N), N!을 구하는 프로그램
N = int(input("수 입력 : "))
su = 1      #su = 0 이면 어떤 수를 넣어도 값이 0이 된다. 따라서 곱하기에 지장 없는 1을 넣어준다.

for i in range(1,N+1):
    su *= i
print(su)