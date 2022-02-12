#<순서가 있는 자료형-리스트,튜플>
A = [1, 2, 'hello', "world", True]
B = (4, False, 'a', "b",4.3)

print(type(A))  #<class 'list'>
print(type(B))  #<class 'tuple'>

#','쉽표를 기준으로 숫자,문자열,Bool 값과 같은 다양한 자료형들을 묶는 것을 알 수 있다!!
#순서가 있다는 표현이 의미하는 것은 묶어놓은 자료들이 각각의 번호표가 있다는 것이다.
#이러한 번호표를 index(인덱스)라고 한다.
#인덱스 통해 각각의 접근 가능
#많은 프로그래밍 언어에서 인덱스는 0부터 시작


A = [1, 2, 'hello', "world", True]
# 1은 A 리스트에서 첫번째 자료이기 때문에 index는 0 이다.
# 2는 A 리스트에서 두번째 자료이기 때문에 index는 1 이다.
# ??은 A 리스트에서 N번재 자료이기 때문에 index는 N-1 이다.

#각각의 자료에 접근하는 방법은 리스트, 튜플의 이름[index] 입니다.

A = [1, 2, 'hello', "world", True]
# 1은 A 리스트에서 첫번째 자료이기 때문에 A[0] 이다.
# ....
# ??은 A 리스트에서 N번째 자료이기 때문에 A[N-1] 이다.

#리스트와 튜플의 차이)
#'자료의 변경이 가능한가?' 에 따라 차이가 있다.
#list는 list내의 자료를 변경할 수 있다.
#이와 달리, tuple은 tuple내의 자료를 변경이 불가하다.

A = [1, 2, 'hello', "world", True]
B = (4, False, 'a', "b", 4.3)

print(A[0], A[2], A[4])
print(B[1], B[3])

A[0] = 2 #2를 A list의 index가 0 인 곳에 대입한다.
B[1] = 3 #3을 B list의 index가 1 인 곳에 대입한다. 
# B[1] <-TypeError: 'tuple' object does not support item assignment
# 에러발생이유: tuple은 tuple내의 자료를 변경할 수 없기 때문이다.

# 형변환을 하면 tuple의 자료를 변경할 수 있다.!!!
# tuple > list로 변환 > 정보 수정 >tuple로 변환

B = (4, False , 'a', "b", 4.3) #tuple
print('변경 전 :',B)
B = list(B) #list로 변환
B[1] = 3 #정보 수정
B = tuple(B) #tuple로 변환
print('변경 후 :',B)





#<리스트 자료 추가,수정,삭제>

li = [1, 2, 'abc', 2.1, 1, True]

print(li[0], li[3])

print(len(li)) #요소의 개수

li.append("Hello")
print(li)      #요소 추가(끝)

li.insert(0, False)
print(li)      #요소 추가(위치지정)

print(li.pop()) #요소 삭제(반환)
B = li.pop()    #요소를 반환해서 B에 대입
print(B)

print(li.count(1)) #리스트 내 요소의 개수 반환

print(li.index(1)) #요소의 인덱스를 반환

print(li.extend([1,2,3])) #리스트에 여러값(리스트) 추가

A = li.copy()  # 리스트 깊은 복사

li.sort()      # 리스트 복사

li.reverse()   # 리스트 뒤집기

li.clear()     #요소 전부 삭제, 초기화