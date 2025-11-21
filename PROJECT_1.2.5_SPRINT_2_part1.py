import turtle as trtl
import time

#----Initialize turtles----
wn = trtl.Screen()
wn.setup(width=1000, height=600) #sets the screen size as the backgrounds are different sizes

def initialize_turtle():
    '''Initializes the turtle using the parameter name and labels it as the name specified
    Makes it easier to initialize turtles and keep them hidden'''
    t = trtl.Turtle()
    t.hideturtle()
    t.penup()
    return t

#call initialize_turtle function
player = trtl.Turtle()
choice1 = initialize_turtle()
choice2 = initialize_turtle()
yeschoice = initialize_turtle()
nochoice = initialize_turtle()
river = initialize_turtle()
queen = initialize_turtle()
yeschoice2 = initialize_turtle()
nochoice2 = initialize_turtle()
intro = initialize_turtle()

#----Register shapes----
image_file = "the_turtle.gif" #image from pixilart by pinkissocool
cave_image = "cave_choice.gif" #image created with giphy by me
waterfall_image = "waterfall_choice.gif" #image created with giphy by me
queen_image = 'ocean_queen.gif' #image by Dreamstime
king_image = 'burrow_king.gif' #image from Soul Knight Wiki
yes_image = 'yes_choice.gif' #image created with giphy by me
no_image = 'no_choice.gif'  #image created with giphy by me
over_image = 'game_over.gif' #image by Dorothy Lear from Dribble
castle_bg = 'castle.gif' #image from pixilart by Grabrela

wn.register_shape(queen_image)
wn.register_shape(image_file)
wn.register_shape(cave_image)
wn.register_shape(waterfall_image)
wn.register_shape(king_image)
wn.register_shape(yes_image)
wn.register_shape(no_image)
wn.register_shape(over_image)
wn.register_shape(castle_bg)

choice1.shape(cave_image)
choice2.shape(waterfall_image)
player.shape(image_file)

player.penup()
player.goto(0, -200)

wn.bgpic('default.gif') #image from iStock

style = ('Caveat', 15, 'bold')
intro.goto(20, 80)
intro.write("Welcome, player, to Turtle Quest! \nMy name's Trotter and you are\ngoing to guide me on our adventure today! \nYou will be given two options as we\nmove through the land. There is a dark overlord \nin these parts and he's out for \nour town next! We must stop him! \n(click s to begin)", font=style, align='center')

#----Game variables ----
terminate = False
stop1 = False
stop2 = False
riddle = "I speak without a mouth and hear without ears. I have no body, but I come alive with the wind. What am I? (ghost, secret, echo, wind are your options)"
answer = "echo"
problem = "Mr. Lee has 32 students in his first period class. He has twice that \nnumber of students in his second and fourth period \nclasses separately. He has half that number of students in \nhis third period class. He has a total of 180 students. \nIf he has no fifth period class, how many students are in his sixth period class?"
math_answer = 4

#---- Game methods ----
def begin():
    '''Initializes the waterfall background and presents the user with two choices through a conversation.
    Asks the user whether they want to go in the waterfall or cave and moves the turtle according
    to which turtle button they click later in the code'''
    global terminate
    global choice1
    global choice2
    if not terminate:
        player.goto(500, -200)
        wn.bgpic('panel-2.gif') #image from lospec by bobablin
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

def test_river():
    global yeschoice
    global nochoice
    global river
    global intro
    global player
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
    yeschoice.onclick(riddle_question)
    nochoice.onclick(dead_end)

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
        wn.bgpic('underwater.gif') #image from cute kawaii resources by beaches
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
        wn.ontimer(test_river, 2000)
        stop1 = True
        stop2 = True
        
def test_cave():
    global yeschoice2
    global nochoice2
    global river
    global intro
    global player
    intro.clear()
    river.clear()
    river.goto(0,250)
    river.write("Take the test?", font=style, align='center')
    yeschoice2.penup()
    yeschoice2.shape(yes_image)
    yeschoice2.goto(-100,200)
    nochoice2.penup()
    nochoice2.shape(no_image)   
    nochoice2.goto(100,200)
    yeschoice2.showturtle()
    nochoice2.showturtle()
    nochoice2.onclick(dead_end)
    yeschoice2.onclick(math)          

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
        wn.bgpic('cave_bg.gif') #image from deviantart by kristyglas
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
        wn.ontimer(test_cave, 2000)

def castle(land):
    if land == "river":
        player.goto(600, -200)
    else:
        player.goto(600, -230)
    player.hideturtle()
    player.goto(-600, -250)
    river.clear()
    intro.clear()
    player.showturtle()
    time.sleep(1)
    choice1.hideturtle()
    queen.hideturtle()
    choice2.hideturtle()
    wn.bgpic(castle_bg)
    player.goto(-100, -250)
    time.sleep(1)
    intro.pencolor("white")
    intro.goto(0, 150)
    intro.write("With the help of the turtle king and \nthe turtle queen, we have gathered \nan army to fight the dark overlord! \nGood luck, brave turtle (click r to go inside)!", font=style, align='center')

def riddle_question(x, y):
    global intro
    global river
    global player
    global yeschoice
    global nochoice
    yeschoice.hideturtle()
    nochoice.hideturtle()
    intro.clear()
    river.clear()
    river.goto(150, 150)
    intro.write("I'll take the test! I can do it!", font=style, align='center')
    time.sleep(1)
    river.write("Here is your test...", font=style, align='center')
    time.sleep(0.5)
    user_input = trtl.textinput("Please enter your answer:", riddle) #utilized google AI to learn how to create text input on turtle
    if user_input == answer:
        river.clear()
        river.write("   Very well. Since you have \nanswered my riddle correctly, \nyou may take my troops to fight the dark one", font=style, align='center')
        time.sleep(1)
        castle("river")
    else:
        river.clear()
        river.write("If you cannot solve such a simple problem, \nyou are not fit to lead my troops!", font=style, align='center')
        time.sleep(2)
        dead_end()

def math(x, y):
    global intro
    global river
    global player
    global yeschoice2
    global nochoice2
    yeschoice2.hideturtle()
    nochoice2.hideturtle()
    intro.clear()
    river.clear()
    river.goto(-250, -100)
    intro.write("I'll take the test! I can do it!", font=style, align='center')
    time.sleep(1)
    river.write("Here is your test...", font=style, align='center')
    time.sleep(0.5)
    user_input = trtl.textinput("Please enter your answer", problem) #utilized google AI to learn how to create text input on turtle
    if user_input == str(math_answer):
        river.clear()
        river.write("Very well. \nSince you have answered my problem \ncorrectly, you may take my troops to fight the dark one", font=style, align='center')
        time.sleep(1)
        castle("cave")
    else:
        river.clear()
        river.write("If you cannot solve such a simple problem, \nyou are not fit to lead my troops!", font=style, align='center')
        time.sleep(2)
        dead_end()

def dead_end(x=None, y=None):
    global player
    global choice1
    global choice2 
    global yeschoice
    global nochoice
    global yeschoice2
    global nochoice2
    global river
    global intro
    global queen
    time.sleep(1)
    wn.bgpic(over_image)
    player.hideturtle()
    choice1.hideturtle()
    choice2.hideturtle()
    yeschoice.hideturtle()
    nochoice.hideturtle()
    yeschoice2.hideturtle()
    nochoice2.hideturtle()
    river.clear()
    intro.clear()
    queen.hideturtle()

#---Turtle onclick methods---
wn.onkeypress(begin, "s")
choice1.onclick(cave)
choice2.onclick(waterfall)

wn.listen()
wn.mainloop()