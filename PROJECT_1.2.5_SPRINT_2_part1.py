import turtle as trtl
import time

#----Initialize turtles----
wn = trtl.Screen()
player = trtl.Turtle()
image_file = "the_turtle.gif"

choice1 = trtl.Turtle()
choice1.hideturtle()
cave_image = "cave_choice.gif"
choice2 = trtl.Turtle()
choice2.hideturtle()
waterfall_image = "waterfall_choice.gif"
queen_image = 'ocean_queen.gif'
king_image = 'burrow_king.gif'
wn.register_shape(queen_image)
wn.register_shape(image_file)
wn.register_shape(cave_image)
wn.register_shape(waterfall_image)
wn.register_shape(king_image)

choice1.shape(cave_image)
choice2.shape(waterfall_image)
player.shape(image_file)

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
terminate = False

def begin():
    global terminate
    global choice1
    global choice2
    if not terminate:
        player.goto(500, -200)
        wn.bgpic('panel-2.gif')
        intro.clear()
        player.hideturtle()
        player.goto(-500, -100)
        player.showturtle()
        player.goto(-200, -100)
        intro.pencolor("white")
        intro.goto(20, 150)
        intro.write("Welcome to the waterfall meadow! To stop the \ndark overlord, we will need some help!", font=style, align = 'center')
        intro.goto(20, 80)
        time.sleep(1)
        intro.write("\n\n\n\nI heard that the river queen doesn't like \nhim! But also, the burrow king doesn't \nlike him either! Who should we ask for help?", font=style, align='center')
        choice1.penup()
        choice1.goto(50,-50)
        choice1.showturtle()
        choice2.penup()
        choice2.goto(250, -200)
        choice2.showturtle()
        terminate = True

def waterfall(x, y):
    intro.clear()
    choice1.hideturtle()
    choice2.hideturtle()
    player.goto(250,-200)
    choice1.shape(queen_image)
    choice1.goto(300, 100)
    player.hideturtle()
    player.goto(-500, -200)
    choice1.showturtle()
    wn.bgpic('underwater.gif')
    time.sleep(1)
    player.showturtle()
    player.goto(-300, -200)

def cave(x, y):
    intro.clear()
    choice1.hideturtle()
    choice2.hideturtle()
    player.goto(50, -50)
    choice1.shape(king_image)
    choice1.goto(-300, -200)
    player.hideturtle()
    player.goto(500, -230)
    time.sleep(1)
    choice1.showturtle()
    wn.bgpic('cave_bg.gif')
    player.showturtle()
    player.goto(200, -230)

wn.onkeypress(begin, "s")
choice1.onclick(cave)
choice2.onclick(waterfall)

wn.listen()
wn.mainloop()