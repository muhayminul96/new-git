import turtle
import random

hello=turtle.Turtle()
hello.speed(0)
hello.color("yellow")
hello.begin_fill()
for i in range(5):
    hello.forward(100)
    hello.left(90)
hello.end_fill()
hello.color("blue")
hello.backward(100)
hello.begin_fill()
for i in range(5):
    hello.forward(100)
    hello.left(90)
hello.end_fill()
hello.penup()
hello.backward(100)
hello.pendown()
hello.color("gray")
hello.begin_fill()
for i in range(5):
    hello.forward(100)
    hello.left(90)
hello.end_fill()

hello.color("red")
hello.penup()
hello.backward(100)
hello.pendown()
hello.begin_fill()
for i in range(5):
    hello.forward(100)
    hello.left(90)
hello.end_fill()
hello.penup()
hello.backward(300)
hello.pendown()
hello.begin_fill()
hello.circle(56)
hello.end_fill()
hello.penup()
hello.left(90)
hello.forward(24)
player_one = turtle.Turtle()
player_one.color("green")
player_one.shape("turtle")
player_one.penup()
player_one.goto(-200,100)
player_two = player_one.clone()
player_two.color("blue")
player_two.penup()
player_two.goto(-200,-100)
player_one.goto(300,60)
player_one.pendown()
player_one.circle(40)
player_one.penup()
player_one.goto(-200,100)
player_two.goto(300,-140)
player_two.pendown()
player_two.circle(40)
player_two.penup()
player_two.goto(-200,-100)
die = [1,2,3,4,5,6]
for i in range(20):

     if player_one.pos() >= (300,100):

             print("Player One Wins!")

             break

     elif player_two.pos() >= (300,-100):

             print("Player Two Wins!")

             break

     else:

             player_one_turn = input("Press 'Enter' to roll the die ")

             die_outcome = random.choice(die)

             print("The result of the die roll is: ")

             print(die_outcome)

             print("The number of steps will be: ")

             print(20*die_outcome)

             player_one.fd(20*die_outcome)

             player_two_turn = input("Press 'Enter' to roll the die ")

             d = random.choice(die)

             print("The result of the die roll is: ")

             print(die_outcome)

             print("The number of steps will be: ")

             print(20*die_outcome)

             player_two.fd(20*die_outcome)




turtle.done()