# These are the 16 fundamental steps to create Game in python
#
# 1: Import module
# 2: Set up the screen
# 3: Register the shapes
# 4: Draw border
# 5: Set the score to 0
# 6: Draw the score 
# 7: Create the PLayer
# 8: Create a variable"playerspeed"
# 9: Choose the number of enemies
#10: Create empty list of enemies
#11: Add enemies to the list
#12: Create the enemy
#13: Create the player's bullet
#14: Move the player left and right
#15: Create keyboard bindings
#16: Main game loop


# 1: Import module
import turtle
import os
import math
import random

# 2: Set up the screen
window = turtle.Screen()
window.bgcolor("black")
window.title("Tank Adventure")
#window.bgpic("background.gif")

# 3: Register the shapes
turtle.register_shape("enemy.gif")
turtle.register_shape("player.gif")

# 4: Draw border
border = turtle.Turtle()
border.speed(0)
border.color("white")
border.penup()
border.setposition(-300,-300)
border.pendown()
border.pensize(3)
for side in range(4):
    border.fd(600)
    border.lt(90)
    border.hideturtle()

# 5: Set the score to 0
score = 0

# 6: Draw the score
score_pen = turtle.Turtle()
score_pen.speed(0)
score_pen.color("white")
score_pen.penup()
score_pen.setposition(-290, 280)
scorestring = "score: %s" %score
score_pen.write(scorestring, False, align="left", font=("Arial", 14, "normal"))
score_pen.hideturtle()

# 7: Create the PLayer
player = turtle.Turtle()
#player.color("blue")
player.shape("player.gif")
player.penup()
player.speed(0)
player.setposition(0, -250)
player.setheading(90) 

# 8: Create a variable"playerspeed"
#and trying to control player using right or left arrow keys
playerspeed = 15

# 9: Choose the number of enemies
number_of_enemies = 5

#10: Create empty list of enemies
enemies = []

#11: Add enemies to the list
for i in range(number_of_enemies):
    #12: Create the enemy
    enemies.append(turtle.Turtle())

for enemy in enemies: 
    #enemy.color("red")
    enemy.shape("enemy.gif")
    enemy.penup()
    enemy.speed(0)
    enemy.setposition(-200, 250)
    x = random.randint(-200, 200)
    y = random.randint(100, 250)
    enemy.setposition(x, y)

enemyspeed = 2

#13: Create the player's bullet
bullet = turtle.Turtle()
bullet.color("yellow")
bullet.shape("triangle")
bullet.penup()
bullet.speed(0)
bullet.setheading(90)
bullet.shapesize(0.5, 0.5)
bullet.hideturtle()

bulletspeed = 40
#define bullet state (there are 2 state)
#(1)ready - ready to fire
#(2)fire - bullet is firing
bulletstate = "ready"

#14: Move the player left and right
#move_left defination which difines turtle to move left
def move_left():
    x = player.xcor()
    x -= playerspeed
    if x < -280:
        x = -280
    player.setx(x)

#move_right defination which difines turtle to move right
def move_right():
    x = player.xcor()
    x += playerspeed
    if x > 280:
        x = 280
    player.setx(x)

#move_up defination which difines turtle to move up
def move_up():
    y = player.ycor()
    y += playerspeed
    player.sety(y)

#move_down defination which difines turtle to move down
def move_down():
    y = player.ycor()
    y -= playerspeed
    player.sety(y)

#fire_bullet defination which enables bullet turtle to fire
def fire_bullet():
    #declare bulletstate as global if it needs changed
    global bulletstate
    if bulletstate == "ready":
       #os.system("laser.wav&") 
        bulletstate = "fire"
        #move the bullet to the just above the player
        x = player.xcor()
        y = player.ycor() +10
        bullet.setposition(x, y)
        bullet.showturtle()

# isCollision defination states if 2 object collide with each 
def isCollision(t1, t2):
    distance = math.sqrt(math.pow(t1.xcor()-t2.xcor(),2)+math.pow(t1.ycor(),2))
    if distance < 15:
        return True
    else:
        return False

#15: Create keyboard bindings
turtle.listen()
turtle.onkeypress(move_left, "Left")    # binds the left key
turtle.onkeypress(move_right, "Right")  # binds the right key
#turtle.onkeypress(move_up, "Up")        # binds the up key
#turtle.onkeypress(move_down, "Down")    # binds the down key
turtle.onkeypress(fire_bullet, "space") # binds the space key 

#main game loop
while True:
    for enemy in enemies:
        #move the enemy
        x = enemy.xcor()
        x +=enemyspeed
        enemy.setx(x)

        #move the enemy back and down
        if enemy.xcor() > 280:
            #moves all the enemy down 
            for e in enemies:
                y = e.ycor()
                y -= 40
                e.sety(y)
            #change enemy direction    
            enemyspeed *= -1
            
        if enemy.xcor() < -280:
            #moves all enemies down
            for e in enemies:
                y = e.ycor()
                y -= 40
                e.sety(y)
            #change enemy direction
            enemyspeed *= -1
            
        #check for a collision between the bullet and the enemy
        if isCollision(bullet, enemy):
            #os.system("explosion.wav&")
            #reset the bullet
            bullet.hideturtle()
            bulletstate = "ready"
            bullet.setposition(0, -400)
            #reset the enemy
            x = random.randint(-200, 200)
            y = random.randint(100, 250)
            enemy.setposition(x, y)
            #update the score
            score += 10
            scorestring = "Score: %s" %score
            score_pen.clear()
            score_pen.write(scorestring, False, align="left", font=("Arial", 14, "normal"))

        if isCollision(player, enemy):
            player.hideturtle()
            enemy.hideturtle()
            print("Game Over")
            break
    
    #move the bullet
    if bulletstate == "fire":    
        y = bullet.ycor()
        y += bulletspeed
        bullet.sety(y)
    #check to see if the bullet has gone to the top
    if bullet.ycor() > 275:
        bullet.hideturtle()
        bulletstate = "ready"

   
     

delay = input("Press enter to finsh.")

