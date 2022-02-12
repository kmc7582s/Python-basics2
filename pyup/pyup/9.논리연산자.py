#<논리연산자>
#bool값을 변환하는 연산자2
#[bool값 끼리의 연산]을 합니다. 대표적으로 and 와 or이 있습니다.

print(True and True)    #True 
print(True and False)   #False
print(False and True)   #False
print(False and False)  #False
# and는 둘다 True일 경우 True를 반환!

print(True or True)     #True
print(True or False)    #True
print(False or True)    #True
print(False or False)   #False
# or은 둘다 False일 경우 False를 반환!

print(not True)     #False
print(not False)    #True

#ex1)  A 가 10보다 크다 그리고 20 보다 작다
#     A > 10   and    A < 20    
#     -----           ------ 
#     bool값   and    bool값

A = 30
print(A > 10 and A < 20)    #False
print(A > 10 or A < 20)     #True
print(not A > 10 and not A > 10) #False
