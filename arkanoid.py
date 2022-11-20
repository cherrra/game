import random
import pgzrun

title = "gameeee"
width = 800
height = 500

plat = Actor("plain.png")
plat.x = 120
plat.y = 420

balls = Actor("ball.png")
balls.x = 30
balls.y = 300
balls_x_speed = 1
balls_y_speed = 1

brick_list = []

def draw():
    screen.blit("background.png", (0,0))
    plat.draw()
    balls.draw()
    for br in brick_list:
        br.draw()

def brick(x,y,image):
    br_x = x
    br_y = y
    for i in range(8):
        br = Actor(image)
        br.x = br_x
        br.y = br_y
        br_x += 70
        brick_list.append(br)


def update():
    global balls_x_speed, balls_y_speed
    if keyboard.left:
        plat.x = plat.x - 5
    if keyboard.right:
        plat.x = plat.x + 5

    update_balls()
    for br in brick_list:
        if balls.colliderect(br):
            brick_list.remove(br)
            balls_y_speed *= -1

    if plat.colliderect(balls):
        balls_y_speed *= -1
        rand = random.randint(0,1)
        if rand:
            balls_x_speed *= -1

def update_balls():
    global balls_x_speed, balls_y_speed
    balls.x -= balls_x_speed
    balls.y -= balls_y_speed
    if (balls.x >= width) or (balls.x <= 0):
        balls_x_speed *= -1
    if (balls.y >= height) or (balls.y <= 0):
        balls_y_speed *= -1

coloured_box_list = ["blue_brick.png", "purple_brick.png",
                     "grey_brick.png"]
x = 120
y = 100
for coloured_box in coloured_box_list:
    brick(x, y, coloured_box)
    y += 50

pgzrun.go()