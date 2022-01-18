
# 수학, 과학 성적을 입력받고, 평균이 90 점 이상이면 “A”,
# 평균이 80 점 이상이면 “B”, 평균이 70 점 이상이면 “C”,
# 나머지는 “D” 가 나오도록 프로그램하세요.

수학 = int(input("수학 성적 : "))
과학 = int(input("과학 성적 : "))

평균 = (수학 + 과학)/2

# 평균에 따라서 학점이 하나만 출력되어야하고, (if, elif, else 를 사용하면 종속문장 한곳만 실행되므로)
# 80점이상이라는 조건에는 90점 미만이라는 조건이 숨어있기 때문에
# if elif else 를 사용하도록 할게요

if 평균 >= 90:
    print("A")
elif 평균 >= 80:
    print("B")
elif 평균 >= 70:
    print("C")
else:
    print("D")

# 두 수와 연산자를 입력받고 사칙연산 결과를 출력하는 프로그램을 작성하세요.
A = int(input("수 입력 : "))
B = int(input("수 입력 : "))
op = input("연산자 입력 : ")

if op == "+":
    print(A+B)
elif op == "-":
    print(A-B)
elif op == "*":
    print(A*B)
if op == "/":
    print(A/B)
else:
    print("연산자가 이상해요.")

# 월을 입력받고, 계절을 출력하는 프로그램
month = int(input("월 입력 : "))

if 1<=month<=12:
    if 3<=month<=5:
        print("봄")
    elif 6<=month<=8:
        print("여름")
    elif 9<=month<=11:
        print("가을")
    else:
        print("겨울")
else:
    ("잘못입력")

#수를 입력받고 절대값을 출력하는 프로그램
#way1
Num = int(input("수 입력 : "))

if Num < 0:
    print("절대값은",-A)
else:
    print("절대값은",A)

#way2
print(abs(A))


#구입할 사과(3000), 배(2000) 의 개수와 현재 소지
#하고있는 금액을 입력받고,
#구매가 가능할 경우 잔돈이 얼마인지 출력해주고,
#구매가 불가능할 경우 “구매불가” 라고 출력해라

사과 = int(input("사과의 개수는?"))
배 = int(input("배의 개수는?"))
money = int(input("가지고 있는 돈 : "))

총지불금액 = 사과*3000 + 배*2000

if money >= 총지불금액: #돈이 충분할 경우
    print("잔돈은",money-총지불금액)  
else:
    print("구매불가! 필요한금액 : ", 총지불금액-money)

# 수(A)를 입력받고,
# A가 3의 배수이면 “3의 배수입니다.”
# A가 5의 배수이면 “5의 배수입니다.”
# 15의 배수일 경우 “15의 배수입니다.”
# 판단하는 프로그램
A = int(input("수 입력 : "))

if A % 15 == 0:
    print("15의 배수입니다.")
elif A % 5 == 0:
    print("5의 배수입니다.")
elif A % 3 == 0:
    print("3의 배수입니다.")
# 15는 92번,94번의 조건에서 모두 True이기 때문에 15의 배수를 검출하는 것을 선행해주어야한다.

#자판기)
print("="*20)
print("1. 아메리카노")
print("2. 카페라떼")
print("="*20)
메뉴 = int(input("메뉴 선택 : "))

if 메뉴 == 1 or 메뉴 == 2:
    print("="*20)
    print("1. ICE")
    print("2. HOT")
    print("="*20)
    온도 = int(input("온도 선택 : "))
    if 메뉴 == 1:
        if 온도 == 1:
            print("아이스 아메리카노 선택")
        elif 온도 == 2:
            print("따뜻한 아메리카노 선택")
        else:
            print("온도를 잘못입력!")
    elif 메뉴 == 2:
        if 온도 == 1:
            print("아이스 카페라떼 선택")
        elif 온도 == 2:
            print("따듯한 카페라떼 선택")
        else:
            print("온도를 잘못입력!")
else:
    print("메뉴 잘못입력!!")

#생년월일을 입력받고, 무슨 띠인지 출력하는 프로그램
# 자축인묘진사오미신유술해 (쥐,소,호랑이,토끼,용,뱀,말,양,원숭이,닭,개,돼지)
birth = int(input("생년월일 입력 : "))
index = birth // 10000 % 12

if index == 1:
    print("닭")
elif index == 2:
    print("개띠")
elif index == 3:
    print("돼지띠")
elif index == 4:
    print("쥐띠")
elif index == 5:
    print("소띠")
elif index == 6:
    print("호랑이띠")
elif index == 7:
    print("토끼띠")
elif index == 8:
    print("용띠")
elif index == 9:
    print("뱀띠")
elif index == 10:
    print("말띠")
elif index == 11:
    print("양띠")
elif index == 0:
    print("원숭이띠")

#태어난해를 입력받고, 무슨 띠인지 출력하는 프로그램
birth = int(input("태어난 해 입력 : "))

if birth % 12 == 1:
    print("닭띠")
elif birth % 12 == 2:
    print("개띠")
elif birth % 12 == 3:
    print("돼지띠")
elif birth % 12 == 4:
    print("돼지띠")
elif birth % 12 == 5:
    print("쥐띠")
elif birth % 12 == 6:
    print("소띠")
elif birth % 12 == 7:
    print("호랑이띠")
elif birth % 12 == 8:
    print("토끼띠")
elif birth % 12 == 9:
    print("용띠")
elif birth % 12 == 10:
    print("뱀띠")
elif birth % 12 == 11:
    print("말띠")
elif birth % 12 == 12:
    print("양띠")
elif birth % 12 == 0:
    print("원숭이띠")

# A-B-C-D 순서로 돌아가면서 한 명당  청소를 하기로 했다, 첫 날은 A 가 청소를 한다고 했을 때
# N 일째 당번은 누구인가?
N = int(input("몇 일?"))

if N % 4 == 1:
    print("A")
elif N % 4 == 2:
    print("B")
elif N % 4 == 3:
    print("C")
else:
    print("D")

# 오늘은 금요일이다. N 일 후에는 무슨 요일일까?
N = int(input("몇 일후?"))

if N % 7 == 1:
    print("토요일")
elif N % 7 == 2:
    print("일요일")
elif N % 7 == 3:
    print("월요일")
elif N % 7 == 4:
    print("화요일")
elif N % 7 == 5:
    print("수요일")
elif N % 7 == 6:
    print("목요일")
else:
    print("금요일")

# 시간과 분을 입력받고, 30분 전 시간을 출력해주는 프로그램
hour = int(input("시간 입력 : "))
min = int(input("분 입력 : "))

총분 = hour*60 + min -30

if 총분 < 0:
    총분 += 1440
print("30분 전 시간 :",총분//60,"시간",총분%60,"분")

# 년도를 입력받고, 윤년인지 아닌지 판별하는 프로그램
년도 = int(input("연도를 입력하세요 :"))

if 년도 % 400 == 0:
    print("윤년입니다.")
elif 년도 % 100 == 0:
    print("평년입니다.")
elif 년도 % 4 == 0:
    print("윤년입니다.")
else:
    print("평년입니다.")

#윤년)

N = int(input("수 입력 : "))

if N % 400 == 0:
    print("윤년", N)
elif N % 100 == 0:
    pass
elif N % 4 == 0:
    print("윤년", N)
else:
    pass
