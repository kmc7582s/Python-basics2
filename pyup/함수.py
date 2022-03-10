# 기본형식
# def 함수의이름(입력값1, 입력값2, ... ):
#     함수의 내용
#     return 반환값1, 반환값2, ...

def add1(A, B):           # A,B 를 입력받는 add 라는 함수를 선언
    return A+B           # A+B 가 반환되도록 한다.

# 만약 두 수를 입력받고, 두 수의 합을 출력하는 프로그래밍을 하여라(함수사용)
# 방법 1
def add2(A,B):
    return A+B

C = int(input("수 입력 : "))
D = int(input("수 입력 : "))

print(add2(C,D))         # 반환되는 값을 바로 출력해주거나

# 방법 2
def add3(A,B):
    return A+B

C = int(input("수 입력 : "))
D = int(input("수 입력 : "))

F = add3(C,D)          # 반환되는 값을 저장할 변수를 만들어 주거나
print(F)

# 방법 3
def add4(A,B):          # 함수를 수정하거나
    print(A+B)

C = int(input("수 입력 : "))
D = int(input("수 입력 : "))

add4(C,D)          
