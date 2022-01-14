#<range>
# Q1. 1에서 입력받은 수 까지 출력
N = int(input("수 입력 : "))

#범위설정
#1에서 N까지 iterable한 자료형을 만들기 위해 range(1,N+1)을 한다.
for i in range(1,N+1):
    print(i)

# Q2. 입력받은 두 수 사이의 수 출력
A = int(input("수 입력 : "))
B = int(input("수 입력 : "))

#A,B 두 수 사이의 수를 출력해야하니까 A + 1 을 start 로 두고 B - 1 까지 출력해야하니까
#range(A+1, B) 로 해주어야 하는데 A 가 클경우가 있다. 그래서 if 를 써도 되지만 
#range(10,1) 과 같은 경우에 step이 1 이기 때문에
#빈 리스트 즉, 자료형의 개수가 0 이기 때문에 반복횟수가 0 이되고 둘 중 하나는 실행이 애초에 안된다.
for i in range(A+1,B):
    print(i)
for i in range(A+1,B):
    print(i)