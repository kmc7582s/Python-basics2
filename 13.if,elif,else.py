#<if,elif,else>
# if = ~라면
# elif = 그게 아니고 ~ 라면 (else if의 의미)
# else = 그밖의

A = 4
if A == 1:
    print("A는 1")
elif A == 2:
    print("A는 2")
elif A == 3:
    print("A는 3")
else:
    print("해당없음")

# if, elif, else 구조에서 만약 위에서 특정 종속문장을 실행하게 되면,
# 아래의 코드는 건너 뛰게 된다.
# 위의 예에서 10 번째에서 조건이 성립되어 11 번 코드가 실행되면 
# 12 번 줄로 가지 않고, 바로 14 번째 줄로 코드가 실행된다.

#연습1)
A = 2

#if만 사용
if A == 1:
    print("A는 1")
if A == 2:
    print("A는 2")
if A == 3:
    print("A는 3")
if A > 3 or A < 1:
    print("해당없음")

#if,elif,else 사용
if A == 1:
    print("A는 1")
elif A == 2:
    print("A는 2")
elif A == 3:
    print("A는 3")
else:
    print("해당없음")

#if-elif-else 의 경우 사용자가 1,2,3 외의 입력의 경우를 else 라는 단어 하나로 처리하지만,
#if 로만 프로그래밍 한 코드는 이러한 예외상황을 전부 처리해야합니다.

#연습2) 점수 등급 프로그램
score = 84

#if
if score > 90:
    print("A")
if score > 80 and score <= 90:
    print("B")
if score > 70 and score <= 80:
    print("C")
if score <= 70:
    print("D")

#if,elif,else
if score > 90:
    print("A")
elif score > 80:
    print("B")
elif score > 70:
    print("C")
else:
    print("D")

