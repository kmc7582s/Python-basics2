#<복합연산자>
#어떤 값을 축적할 때 주로 사용된다.

a=10
b='a'

a += 3      # a = a + 3
a -= 4      # a = a - 4
a *= 2      # a = a * 2
a /= 5      # a = a / 5
a //= 3     # a = a // 3 (몫)
a **= 4     # a = a ** 4 (제곱)
b += 'c'    # b = b + 'c' = ac
b *= 4      # b = b * 4   = aaaa

print(a)
print(b)