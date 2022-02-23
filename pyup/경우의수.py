# 잔돈을 입력받고, 1000원, 500원, 100원으로 받을 수 있는 
# 경우의 수를 모두 출력

money = int(input("잔돈입력 : "))

천원 = money // 1000 
오백원 = money // 500
백원 = money // 100

for i in range(천원+ 1):
    for j in range(오백원 + 1):
        for k in range(백원 + 1):
            if 1000 * i + 500 * j + 100 * k == money:
                print("1000",i,"장\t500",j,"개\t100",k)
