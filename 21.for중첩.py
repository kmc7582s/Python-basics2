#<for 중첩>
#반복문의 종속문장에 반복문이 존재하는 경우 반복문이 중첩되었다고 표현한다.

for i in range(10):        # i 는 0-9 즉, 종속문장을 10 번 반복
    for j in range(10):    # j 는 0-9 즉, 종속문장을 10 번 반복
        print(i,j)

# 4번의 종속문장에는 또 다른 반복문이 존재합니다.
# 이 때, 밖에 존재하는 반복문을 외반복문 (4)
# 종속문장 안에 존재하는 반복문을 내반복문 (5) 이라고 합니다.

# i 가 0 일때, j 는 0 부터 9 까지 반복 (10회반복) 합니다.
# i 가 1 일때, j 는 0 부터 9 까지 반복 (10회반복) 합니다.
# i 가 2 일때, j 는 0 부터 9 까지 반복 (10회반복) 합니다.
# ...
# i 가 9 일때, j 는 0 부터 9 까지 반복 (10회반복) 합니다.
# j 가 계속해서 값을 바꾸는 반면, i 는 비교적 적게 변합니다.
# 이를 통해서, 외반복문과 내반복문의 특징을 살펴볼 수 있습니다.

#연습)
# 2단부터 9단까지 출력해주는 프로그램

for i in range(2,10):
    for j in range(1,10):
        print(i,'x',j,'=',i*j)

#N을 입력받고, 2에서 N까지 수의 약수를 출력해라
N = int(input("수 입력 : "))

for i in range(2,N+1):
    print(i,"의 약수는",end='')
    for j in range(1,i+1):
        if i % j == 0:
            print(j, end='')
    print()