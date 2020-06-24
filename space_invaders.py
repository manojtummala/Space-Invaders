import turtle
import os
import math
import random

wn = turtle.Screen()
wn.bgcolor("black")
wn.title("SPACE INVADERS")
wn.bgpic("space_invaders_background.gif")
wn.tracer(0)

wn.register_shape("invader.gif")
wn.register_shape("ship.gif")


border_pen = turtle.Turtle()
border_pen.speed(0) #fastest speed possible
border_pen.color("white")
border_pen.penup()
border_pen.setposition(-300, -300) #as per to centre of the screen
border_pen.pendown()
border_pen.pensize(4)
for side in range(4):
	border_pen.fd(600)
	border_pen.lt(90) #rotateing by 90 degrees
border_pen.hideturtle()


score = 0
score_pen = turtle.Turtle()
score_pen.speed(0)
score_pen.color("white")
score_pen.penup()
score_pen.setposition(-290, 280)
scorestring = "Score: %s" %score
score_pen.write(scorestring, False, align = "left", font = ("Arial", 14, "normal"))
score_pen.hideturtle()


ship = turtle.Turtle()
ship.color("green")
ship.shape("ship.gif")
ship.penup()
ship.speed(0)
ship.setposition(0,-250)
ship.setheading(90) #same as rotating but just changing where it is facing

ship_move = 20 #the distance it moves when we press

def left():
	x = ship.xcor() #you take x co ordinate
	x -= ship_move
	if x < -280: #this condition is for the triangle not to cross the boundary
		x = -280
	ship.setx(x) #fix the new co ordinate

def right():
	x = ship.xcor()
	x += ship_move
	if x > 280:
		x = 280
	ship.setx(x)



#creating multiple enemies
number_of_enemies = 30
enemies = []
for i in range(number_of_enemies):
	enemies.append(turtle.Turtle())

enemy_start_x = -200
enemy_start_y = 250
enemy_number = 0
for enemy in enemies:
	enemy.color("red")
	enemy.shape("invader.gif")
	enemy.penup()
	enemy.speed(0)
	x = enemy_start_x + (50 * enemy_number)
	y = enemy_start_y
	enemy.setposition(x, y)
	enemy_number += 1
	if enemy_number == 10:
		enemy_start_y -= 50
		enemy_number = 0

enemy_move = 0.07

#creating shooting
bullet = turtle.Turtle()
bullet.color("yellow")
bullet.shape("triangle")
bullet.speed(0)
bullet.penup()
bullet.setheading(90)
bullet.shapesize(0.4, 0.4)
bullet.hideturtle()

bullet_move = 3 #speed of bullet or movement of bullet
bulletstate = "ready"

def fire_bullet():
	global bulletstate
	if bulletstate == "ready":
		bulletstate = "fire"
		x = ship.xcor()
		y = ship.ycor() + 15
		bullet.setposition(x,y)
		bullet.showturtle()

def isCollision(t1, t2):
	distance = math.sqrt(math.pow(t1.xcor() - t2.xcor(), 2) + math.pow(t1.ycor() - t2.ycor(),2))
	if distance < 15:
		return True
	else:
		return False

turtle.listen() #to detect the keyboard bindings
turtle.onkey(left, "Left") #reacts to the key presses
turtle.onkey(right, "Right")
turtle.onkey(fire_bullet, "space")


#main game loop
while True:
	wn.update()
	for enemy in enemies:
		x = enemy.xcor() #to make the enemy to move towards right
		x += enemy_move
		enemy.setx(x)

		if enemy.xcor() > 280:
			for e in enemies:
				y = e.ycor() # to make the nemy to move back and forth without crossing the boundary
				y -= 40
				e.sety(y)
			enemy_move *= -1 	

		if enemy.xcor() < -280:
			for e in enemies: #moves all enimes down even if one touches border
				y = e.ycor()
				y -= 40
				e.sety(y)
			enemy_move *= -1

		if isCollision(bullet,enemy):
			bullet.hideturtle()
			bulletstate = "ready"
			bullet.setposition(0, -400)
			#reset the enemy.. if collision occurs
			enemy.setposition(0, 10000)
			score += 10
			scorestring = "Score: %s" %score
			score_pen.clear()
			score_pen.write(scorestring, False, align = "left", font = ("Arial", 14, "normal"))

		if isCollision(ship,enemy):
			ship.hideturtle()
			enemy.hideturtle()
			print("GAME OVER")
			break

	if bulletstate == "fire": #moving bullet only if it is in fire mode
		y = bullet.ycor()  #moving bullet
		y += bullet_move
		bullet.sety(y)

	if bullet.ycor() > 275: #checking if bullet crosses the boundary 
		bullet.hideturtle() #and if it does then it will be set back to ready mode
		bulletstate = "ready"

	

delay = input("press enter to terminate...")

