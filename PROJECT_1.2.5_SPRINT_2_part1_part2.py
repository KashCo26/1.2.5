import turtle as trtl
import time

#----Initialize turtles----
wn = trtl.Screen()
wn.setup(width=1000, height=600)
player = trtl.Turtle()
image_file = "the_turtle.gif"

choice1 = trtl.Turtle()
choice1.hideturtle()
cave_image = "cave_choice.gif"
choice2 = trtl.Turtle()
choice2.hideturtle()
river = trtl.Turtle()
river.hideturtle()
queen = trtl.Turtle()
queen.hideturtle()
queen.penup()
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
stop1 = False
stop2 = False

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
        intro.write("I heard that the river queen doesn't like \nhim! But also, the burrow king doesn't \nlike him either! Who should we ask for help?", font=style, align='center')
        choice1.penup()
        choice1.goto(50,-50)
        choice1.showturtle()
        choice2.penup()
        choice2.goto(250, -200)
        choice2.showturtle()
        terminate = True

def waterfall(x, y):
    global stop1
    if not stop1:
        intro.clear()
        choice1.hideturtle()
        choice2.hideturtle()
        player.goto(250,-200)
        queen.shape(queen_image)
        queen.goto(300, 100)
        player.hideturtle()
        player.goto(-500, -200)
        wn.bgpic('underwater.gif')
        queen.showturtle()
        time.sleep(1)
        player.showturtle()
        player.goto(-300, -200)
        river.penup()
        river.goto(150, 150)
        river.pencolor("white")
        river.write("Hello turtle...\nWhat do the land dwellers \nhave to do with the \npoor river queen?", font=style, align='center')
        intro.pencolor("green")
        intro.goto(5, -250)
        time.sleep(2)
        intro.write("The dark overlord has been polluting \nthe river and disturbing the peace!\nPlease help me stop him!", font=style, align='center')  
        river.clear()
        time.sleep(2)
        river.write("Very well... for the river\nBut if I am too\nlend you my help, \nyou must pass a test", font=style, align='center')
        
        stop1 = True

def cave(x, y):
    global stop2
    if not stop2:
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
        stop2 = True

wn.onkeypress(begin, "s")
choice1.onclick(cave)
choice2.onclick(waterfall)

wn.listen()
wn.mainloop()