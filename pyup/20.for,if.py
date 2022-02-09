
#<for,if>
#for,if 병합된 문제 해결

#1~99의 짝수를 모두 출력하는 프로그램

for i in range(1,100):
    if i % 2 == 0:
        print(i)

#range만 사용
 
for i in range(2,100,2):
    print(i)

#연습)
# 1에서 사용자가 입력한 수까지의 짝수 출력 프로그램
N = int(input("수 입력 : "))
for i in range(1,N+1):
    if i % 2 == 0:
        print(i)

# 1에서 사용자가 입력한 수까지의 짝수의 합 프로그램
num = int(input("수 입력 : "))
total = 0
for i in range(1,num+1):
    if i % 2 == 0:
        total += i
print(total)
