# import turtle as t
# import random as r
# import song

# t.setup(1000,1000)
# t.pensize(7)
# t.hideturtle()
# t.speed(0)
# t.colormode(255)
# t.penup()

# 가사 = song.사전
# print(가사)

# for i in len(가사):
#     t.color(r.randint(0,255),r.randint(0,255),r.randint(0,255))
#     t.goto(r.randint(-300,300),r.randint(-400,400))
#     t.write(i, font=("맑은고딕",2*(가사[i]+7),"bold"))
# t.mainloop()


import turtle as t
import random as r

dynamite가사 = """'Cause I-I-I'm in the stars tonight
So watch me bring the fire and set the night alight
Shoes on, get up in the morn'
Cup of milk, let's rock and roll
King Kong, kick the drum, rolling on like a Rolling Stone
Sing song when I'm walking home
Jump up to the top, LeBron
Ding dong, call me on my phone
Ice tea and a game of ping pong, huh
This is getting heavy
Can you hear the bass boom? I'm ready (woo hoo)
Life is sweet as honey
Yeah, this beat cha-ching like money, huh
Disco overload, I'm into that, I'm good to go
I'm diamond, you know I glow up
Hey, so let's go
'Cause I-I-I'm in the stars tonight
So watch me bring the fire and set the night alight (hey)
Shining through the city with a little funk and soul
So I'ma light it up like dynamite, whoa oh oh
Bring a friend, join the crowd
Whoever wanna come along
Word up, talk the talk
Just move like we off the wall
Day or night, the sky's alight
So we dance to the break of dawn
Ladies and gentlemen, I got the medicine
So you should keep ya eyes on the ball, huh
This is getting heavy
Can you hear the bass boom? I'm ready (woo hoo)
Life is sweet as honey
Yeah, this beat cha-ching like money
Disco overload, I'm into that, I'm good to go
I'm diamond, you know I glow up
Let's go
'Cause I-I-I'm in the stars tonight
So watch me bring the fire and set the night alight (hey)
Shining through the city with a little funk and soul
So I'ma light it up like dynamite, whoa oh oh
Dy-na-na-na, na-na, na-na-na, na-na-na, life is dynamite
Dy-na-na-na, na-na, na-na-na, na-na-na, life is dynamite
Shining through the city with a little funk and soul
So I'ma light it up like dynamite, whoa oh oh
Dy-na-na-na, na-na, na-na, ayy
Dy-na-na-na, na-na, na-na, ayy
Dy-na-na-na, na-na, na-na, ayy
Light it up like dynamite
Dy-na-na-na, na-na, na-na, ayy
Dy-na-na-na, na-na, na-na, ayy
Dy-na-na-na, na-na, na-na, ayy
Light it up like dynamite
'Cause I-I-I'm in the stars tonight
So watch me bring the fire and set the night alight
Shining through the city with a little funk and soul
So I'ma light it up like dynamite (this is ah)
'Cause I-I-I'm in the stars tonight
So watch me bring the fire and set the night alight (alight, oh)
Shining through the city with a little funk and soul
So I'ma light it up like dynamite, whoa (light it up like dynamite)
Dy-na-na-na, na-na, na-na-na, na-na-na, life is dynamite
Dy-na-na-na, na-na, na-na-na, na-na-na, life is dynamite
Shining through the city with a little funk and soul
So I'ma light it up like dynamite, whoa oh oh"""

걸러야할단어목록 = "()_!?,\n"
for i in 걸러야할단어목록:
    dynamite가사 = dynamite가사.replace(i,"")
dynamite가사 = dynamite가사.replace("-"," ")
dynamite단어 = dynamite가사.split(' ')
dynamite사전 = {}
for i in set(dynamite단어):
    dynamite사전[i] = dynamite단어.count(i)

t.shapesize(2)
t.speed(0)        
t.hideturtle()
t.penup()             

t.colormode(255)
for i in dynamite사전:
    for j in i:
        t.write(i, font=("맑은고딕", (dynamite사전[i]+4)*2, 'bold')) 
        t.goto(r.randint(-300,250), r.randint(-200,150))  
        t.pencolor(r.randint(0,255),r.randint(0,255),r.randint(0,255))   
t.hideturtle()
t.mainloop()
