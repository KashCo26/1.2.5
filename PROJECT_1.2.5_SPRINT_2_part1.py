import turtle as trtl
import time

#----Initialize turtles----
wn = trtl.Screen()
wn.setup(width=1000, height=600)
player = trtl.Turtle()
image_file = "the_turtle.gif"

riddle = "I speak without a mouth and hear without ears. I have no body, but I come alive with the wind. What am I?"
answer = "echo"

choice1 = trtl.Turtle()
choice1.hideturtle()
choice2 = trtl.Turtle()
choice2.hideturtle()
yeschoice = trtl.Turtle()
yeschoice.hideturtle()
nochoice = trtl.Turtle()
nochoice.hideturtle() 
river = trtl.Turtle()
river.hideturtle()
queen = trtl.Turtle()
queen.hideturtle()
queen.penup()

#----Register shapes----
cave_image = "cave_choice.gif" #gif created with giphy
waterfall_image = "waterfall_choice.gif" #gif created with giphy
queen_image = 'ocean_queen.gif'
king_image = 'burrow_king.gif'
yes_image = 'yes_choice.gif' #gif created with giphy
no_image = 'no_choice.gif'  #gif created with giphy
wn.register_shape(queen_image)
wn.register_shape(image_file)
wn.register_shape(cave_image)
wn.register_shape(waterfall_image)
wn.register_shape(king_image)
wn.register_shape(yes_image)
wn.register_shape(no_image)
wn.register_shape('game_over')

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
        intro.write("\n\n\n\nI heard that the river queen doesn't like \nhim! But also, the burrow king doesn't \nlike him either! Who should we ask for help?", font=style, align='center')
        choice1.penup()
        choice1.goto(50,-50)
        choice1.showturtle()
        choice2.penup()
        choice2.goto(250, -200)
        choice2.showturtle()
        terminate = True

def waterfall(x, y):
    global stop1
    global stop2
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
        river.write("Very well... for the river\nBut if I am to\nlend you my help, \nyou must pass a test", font=style, align='center')
        stop1 = True
        stop2 = True
        time.sleep(2)
        intro.clear()
        river.clear()
        river.goto(240,-150)
        river.pencolor("white")
        river.write("Take the test?", font=style, align='center')
        yeschoice.penup()
        yeschoice.shape(yes_image)
        yeschoice.goto(150,-200)
        nochoice.penup()
        nochoice.shape(no_image)   
        nochoice.goto(350,-200)
        yeschoice.showturtle()
        nochoice.showturtle()

def cave(x, y):
    global stop2
    global stop1
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
        river.penup()
        river.goto(-250, -100)
        river.pencolor("white")
        river.write("Hello turtle...\nWhat do the land dwellers \nhave to do with the \npoor burrow king?", font=style, align='center')
        intro.pencolor("white")
        intro.goto(200, -100)
        time.sleep(2)
        intro.write("The dark overlord has been drilling \nthe caves and disturbing the peace!\nPlease help me stop him!", font=style, align='center')  
        river.clear()
        time.sleep(2)
        river.write("Very well... for the caves\nBut if I am to\nlend you my help, \nyou must pass a test", font=style, align='center')
        stop2 = True
        stop1 = True

def riddle():
    pass
def dead_end():
    wn.bgpic('game_over')

wn.onkeypress(begin, "s")
choice1.onclick(cave)
choice2.onclick(waterfall)
yeschoice.onclick(riddle)
nochoice.onclick(dead_end)

wn.listen()
wn.mainloop()