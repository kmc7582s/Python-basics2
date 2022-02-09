from tkinter import Y
import turtle as t

N = int(input("몇 각형 ? "))

col = ["red","orange","green","blue","navy","purple"]

t.color("blue")
t.pensize(7)
t.shape("turtle")
t.speed(0)

for k in range(3,N+1):
    t.color(col[k%len(col)])
    # N 각형을 그리는 코드!
    for i in range(k):
        t.fd(100)
        t.lt(360/N)


t.mainloop()
