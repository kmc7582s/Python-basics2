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