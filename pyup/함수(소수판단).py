# 풀이1

def 약수의개수반환(N):
    count = 0
    for i in range(1, N+1):
        if N % i == 0:
            count += 1
    return count                

A = int(input("수를 입력하세요 : "))
A_약수 = 약수의개수반환(A)
if A_약수 == 2:
    print("소수입니다.")
else:
    print("소수가 아닙니다.")



# 풀이2

def 소수판단(N):
    for i in range(2,N):
        if N % i == 0:
            return False
    return True

A = int(input("수를 입력하세요 : "))
if 소수판단(A):
    print("소수입니다.")
else:
    print("소수가 아닙니다.")