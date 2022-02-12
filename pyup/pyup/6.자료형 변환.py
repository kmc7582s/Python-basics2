#<자료형 변환>

a = input("수 입력 : ") #12
b = input("수 입력 : ") #11
print(a + b) #1211
#문자열끼리 덧셈은 문자열 연결이기 때문에 문제발생
#따라서 자료형 형태 변환

#[바꿔주고 싶은 자료형](자료)
a = '12'
int(a) #str(문자열) 인 자료형을 int(정수)로 바꿔준다.

#int(input())
a = int(input('수 입력 : '))
#수를 입력하는 동시에 정수형으로 바꿔준다.

a = int(input('수 입력 : ')) #211
b = int(input('수 입력 : ')) #20
print(a + b) #231

#ex)
num1 = int(input('수1 입력 : ')) #21
num2 = int(input('수2 입력 : ')) #2
print(num1 + num2) #23
print(num1 - num2) #19