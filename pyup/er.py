"""
n=0
for i in range(1,6):
    n += i
print(n)


li = [95,100,98,78,65,55,78,52,97,98]
print(li)

"""

a = int(input("입력 : "))
b = list(map(int, input().split()))
 
for i in range(a) : 
    for j in range(a) :
        print(b[j], end = ' ')
    for z in range(a-1) :
        temp = b[z]
        b[z] = b[z+1]
        b[z+1] = temp