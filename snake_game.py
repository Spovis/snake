import turtle
import time
import random

window = turtle.Screen()
win_width = 600
win_height = 600

head = turtle.Turtle("square")
head.direction = 'stop'
head.x = 100
head.y = 100
head.score = 0
head.delay = .2
vel = 20
apple = turtle.Turtle("square")
apple.direction = 'stop'
apple.x = 20
apple.y = 260
bodys = []

def startup():
    window
    window.title("Snake")
    window.bgcolor("teal")
    window.setup(width=win_width, height=win_height)
    window.tracer(0)

    head.speed(0)
    head.shape("square")
    head.color("dark green")
    head.penup()
    head.goto(head.x, head.y)

    apple.shape("square")
    apple.color("red")
    apple.penup()
    apple.goto(apple.x, apple.y)

def check_got_apple(hx,hy,ax,ay):
    if hx == ax and hy == ay:
        head.score += 1
        apple.x = 20*(random.randint((-win_width/40)+1,(win_width/40)-1))
        apple.y = 20*(random.randint((-win_height/40)+1,(win_height/40)-1))
        for index in range(len(bodys)-1,0,-1):
            while apple.x == bodys[index].x:
                apple.x = 20 * (random.randint((-win_width / 40) + 1, (win_width / 40) - 1))
                apple.y = 20 * (random.randint((-win_height / 40) + 1, (win_height / 40) - 1))
        apple.goto(apple.x,apple.y)
        print(str(head.score))
        make_body()
        if head.delay >= .08:
            head.delay -= .01



def make_body():
    new_body = turtle.Turtle()
    new_body.speed = 0
    new_body.penup()
    new_body.color('dark green')
    new_body.shape('square')
    bodys.append(new_body)
    new_body.goto(head.x,head.y)


def r():
    if len(bodys) >= 1:
        if not bodys[0].x > head.x:
            head.direction = 'right'
    else:
        if not head.direction == 'left':
            head.direction = 'right'
def l():
    if len(bodys) >= 1:
        if not bodys[0].x < head.x:
            head.direction = 'left'
    else:
        if not head.direction == 'right':
            head.direction = 'left'
def u():
    if len(bodys) >= 1:
        if not bodys[0].y > head.y:
            head.direction = 'up'
    else:
        if not head.direction == 'down':
            head.direction ='up'
def d():
    if len(bodys) >= 1:
        if not bodys[0].y < head.y:
            head.direction = 'down'
    else:
        if not head.direction == 'up':
            head.direction ='down'


window.listen()
window.onkey(r, 'd')
window.onkey(l, 'a')
window.onkey(u, 'w')
window.onkey(d, 's')

def death():
    head.goto(head.x, head.y)
    window.update()
    time.sleep(.05)
    window.clear()
    window.bgcolor('teal')
    head.goto(0,30)
    head.write('Your score was', font=("Comic Sans", 15, "normal"))
    head.goto(0,0)
    head.write(str(head.score),font=("Comic Sans", 15, "normal"))
    time.sleep(3)
    window.bye()


def move():
    for index in range(len(bodys)-1,0,-1):
        bodys[index].x = bodys[index-1].x
        bodys[index].y = bodys[index-1].y
        bodys[index].goto(bodys[index].x,bodys[index].y)
    if len(bodys) >= 1:
        bodys[0].x = head.x
        bodys[0].y = head.y
        bodys[0].goto(bodys[0].x, bodys[0].y)

    if head.direction == 'right':
        head.x += vel
        if head.x >= (win_width/2):
            death()
    if head.direction == 'left':
        head.x -= vel
        if head.x <= 0-(win_width/2):
            death()
    if head.direction == 'up':
        head.y += vel
        if head.y >= win_height/2:
            death()
    if head.direction == 'down':
        head.y -= vel
        if head.y <= (0-(win_height/2)):
            death()
    head.goto(head.x, head.y)

    for index in range(len(bodys)-1,0,-1):
        if bodys[index].x == head.x and bodys[index].y == head.y:
            death()




def main():
    while True:
        window.update()
        move()
        time.sleep(head.delay)
        check_got_apple(head.x,head.y,apple.x,apple.y)
startup()
main()
