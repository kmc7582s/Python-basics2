#break는 반복문 안에서만 사용할 수 있습니다.

#break : 반복문 탈출
for i in range(10):
    print(i)
    if i == 2:
        break

for i in range(10):
    if i == 2:
        break
    print(i)
#if 로 검사를 하고 출력하는 프로그램이기 때문에
#0, 1 에 대해서만 print 가 실행되고 끝나는 프로그램이 된다.

for i in range(10):
    for j in range(10):
        print(j)
        break
#반복문 중첩에서는 자신이 속한 종속문장만 탈출한다는 것을 알 수 있다!



