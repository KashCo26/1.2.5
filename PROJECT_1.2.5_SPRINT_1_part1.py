import turtle as trtl

#----Initialize turtles----
player = trtl.Turtle()
image_file = "the_turtle.gif"

wn = trtl.Screen()
wn.register_shape(image_file)
player.shape(image_file)

player.shapesize(stretch_wid=2, stretch_len=3, outline=5)

player.penup()
player.goto(0, -200)

wn.bgpic('default.gif')

intro = trtl.Turtle()
style = ('Caveat', 15, 'bold')
intro.penup()
intro.hideturtle()
intro.goto(20, 80)
intro.write("Welcome, player, to Turtle quest! \nMy name's Trotter and you are\ngoing to guide me on our adventure today! \nYou will be given two options as we\nmove through the land. There is a dark overlord \nin these parts and he's out for \nour town next! We must stop him! \n(click s to begin)", font=style, align='center')

#----Turtle onclick methods----
def begin():
    player.goto(400, -200)

wn.onkeypress(begin, "s")

wn.listen()
wn.mainloop()