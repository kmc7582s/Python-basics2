#<for(복합연산자(합)>
#1부터 10까지의 합
su = 0 
for i in range(1,11):
    su += i
print(su)

#1부텨 100까지의 합
num = 0
for i in range(1,101):
    su += i
print(num)

#1에서 N까지의 합
N = int(input("수 입력 : "))
total = 0
for i in range(1,N+1):
    total += i
print(total)     