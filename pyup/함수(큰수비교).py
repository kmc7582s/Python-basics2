# X, Y 를 입력받고 둘중 큰수를 출력하세요.

def 함수1(A, B):
    if A > B:
        return A
    else:
        return B

def 함수2(A, B):
    if A >= B:
        print(f"{A}가 크다")
    else:
        print(f"{B}가 크다")

X = int(input("수 입력 : "))
Y = int(input("수 입력 : "))

max_XY = 함수1(X,Y)
print(f"{max_XY}가 더 크다.")

함수2(X,Y)
