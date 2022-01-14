#<error>

#칸 띄우기 잘못했을 경우 에러
 if True:
     print(1) #IndentationError: unexpected indent

#선언하지 않은 변수사용했을 경우 에러
print(s) #NameError: name 's' is not defined

#TypeError
num = input("수를 입력하세요")
print(num+3) #TypeError: can only concatenate str (not "int") to str
#str형과 int형의 덧셈에서 주로 발생
#TypeError가 발생하면 우측의 에러 점검

#오타발생에러
#SyntaxError (Pyrhon이 작성한 프로그램을 이해하지 못합니다. 프로그램을 실행할 수 없습니다.)
#괄호가 덜 닫혀있거나, 따옴표를 닫아주지 않으면 발생
print("1"  #SyntaxError: unexpected EOF while parsing

#Runtime error. : 프로그램 실행 중에(runtime) 에러 메시지와 함께 프로그램이 갑자기 종료되는 것을 말합니다.

