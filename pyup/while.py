#while 형식
'''
while [ Bool ]:
    [      while 의 종속문장         ]

'''
# Bool 값이 참일 때 동안 종속문장을 반복합니다.

# 사용자가 0 을 입력할 때까지 반복하기

while True: 
    user = int(input("그만하려면 0를 누를 입력하세요."))
    if user == 0:                                   # user 가 0을 입력하면 종료
        print("프로그램을 종료합니다.")
        break

# 사용자가 q 를 입력할 때까지 반복하기

while True:
    user = input("그만하려면 q를 누를 입력하세요.") # 문자열을 받아야하니까 int(X)
    if user == 'q': # q를 입력하면 종료
        print("프로그램을 종료합니다.")
        break

# 1)
# 종료를 누를때까지 숫자들을 리스트에 담는것
li = []
while True:
    user = input("그만하려면 q를 누를 입력하세요.") 
    if user == 'q': # q를 입력하면 종료
        print("프로그램을 종료합니다.")
        break
    li.append(int(user))
# 그럼 이상 사용자가 숫자를 입력하면 list 에 추가하는 while 문을 끝냈습니다.
print(li)

# 2)
# 문자열하고 점을 찍고 isnumeric()   > 숫자로 바꿀 수 있는 문자는 True 반환
li = []
while True:
    user = input("그만하려면 q를 누를 입력하세요.") 
    if user == 'q': # q를 입력하면 종료
        print("프로그램을 종료합니다.")
        break
    if user.isnumeric():
        li.append(int(user))
    else:
        print("숫자만 입력하세요!!!!")
# 그럼 이상 사용자가 숫자를 입력하면 list 에 추가하는 while 문을 끝냈습니다.
print(li)


# 종료를 누를때까지 숫자들의 합을 출력
li = []
while True:
    user = input("그만하려면 q를 누를 입력하세요.") 
    if user == 'q': 
        print("프로그램을 종료합니다.")
        break
    li.append(int(user))
print(sum(li))
