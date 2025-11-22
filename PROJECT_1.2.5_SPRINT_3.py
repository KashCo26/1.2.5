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
bowser = initialize_turtle()

#----Register shapes----
image_file = "the_turtle.gif" #image from Pixilart by pinkissocool
cave_image = "cave_choice.gif" #image created with giphy by me
waterfall_image = "waterfall_choice.gif" #image created with giphy by me
queen_image = 'ocean_queen.gif' #image by Dreamstime
king_image = 'burrow_king.gif' #image from Soul Knight Wiki
yes_image = 'yes_choice.gif' #image created with giphy by me
no_image = 'no_choice.gif'  #image created with giphy by me
over_image = 'game_over.gif' #image by Dorothy Lear from Dribble
castle_bg = 'castle.gif' #image from Pixilart by Grabrela
bowser_image = 'bowser.gif' #image from Alpha Coders by robokoboto
castle_hall = 'inside_castle.gif' #image from PixelJoint
turtle_fireball = 'turtle_fireball.gif' #image from Pixilart by the-ernis
bowser_fireball = 'bowser_fireball.gif' #image from Pixilart by the-ernis

wn.register_shape(queen_image)
wn.register_shape(image_file)
wn.register_shape(cave_image)
wn.register_shape(waterfall_image)
wn.register_shape(king_image)
wn.register_shape(yes_image)
wn.register_shape(no_image)
wn.register_shape(over_image)
wn.register_shape(castle_bg)
wn.register_shape(bowser_image)

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
    global terminate, choice1, choice2
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
    '''Uses the turtle writer to write out a dialogue. Asks the user to take the test
    and according to what turtle they click, a different function is called'''
    global yeschoice, nochoice, river, intro, player
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

def waterfall(x, y): #takes parameters (x,y) as it is an onclick function
    '''changes the background to match the waterfall and starts a conversation
    between the user and the river queen. after a 2 second pause, the program calls the take
    test function'''
    global stop1, stop2
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
    '''asks the user if they would like to take the test and calls the 
    corresponding function'''
    global yeschoice2, nochoice2, river, intro, player
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

def cave(x, y): #takes parameters (x,y) as it is an onclick function
    '''changes the background to a cave background and entails a conversation
    between the user and burrow king. At the end, it transitions to test_cave to ask about the
    test'''
    global stop2, stop1 #ensure that if a turtle is clicked again, the function is not called
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
    '''according to the land parameter, the player moves off screen differently to ensure
    that it does not look like it is flying. It sets the background to outside the castle
    and tells the user to go int'''
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
    intro.pencolor("black")
    intro.goto(0, 150)
    intro.write("With the help of the turtle king and \nthe turtle queen, we have gathered \nan army to fight the dark overlord! \nGood luck, brave turtle (click r to go inside)!", font=style, align='center')

def riddle_question(x, y): #takes parameters (x,y) as it is an onclick function
    '''when the user is asked the riddle by the river queen, a turtle input window pops
    up and the user enters their answer to the riddle. If their answer is correct, they proceed.
    Else, they lose.'''
    global intro, river, player, yeschoice, nochoice
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

def math(x, y): #takes parameters (x,y) as it is an onclick function
    '''when the user is asked the problem by the burrow king, a turtle input window pops
    up and the user enters their answer to the problem. If their answer is correct, they proceed.
    Else, they lose.'''
    global intro, river, player, yeschoice2, nochoice2
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

def boss_dialogue():
    '''changes the background to inside the castle and starts a dialogue with
    the bad guy. Then, it calls the boss_fight function'''
    intro.clear()
    river.clear()
    player.goto(100, -50)
    player.hideturtle()
    player.goto(-600, -250)
    wn.bgpic(castle_hall)
    bowser.shape(bowser_image)
    river.goto(200, 0)
    bowser.goto(300, -150)
    bowser.showturtle()
    intro.goto(-200, 0)
    player.showturtle()
    player.goto(-300, -150)
    time.sleep(1)
    river.pencolor("white")
    intro.pencolor("white")
    river.write("Who are you?!", font=style, align='center')
    time.sleep(0.5)
    intro.write("I am Trotter and I\n have come to stop you \nfrom bothering the townspeople!", font=style, align='center')
    time.sleep(0.5)
    river.clear()
    river.write("Hahahahaha! YOU! DEFEAT ME?? \nNo one can defeat me MUAHAHA!", font=style, align='center')
    time.sleep(1)
    intro.clear()
    intro.write("We will see about that! I challenge you!", font=style, align='center')
    time.sleep(0.5)
    river.clear("Okay pipsqueak! Let's fight!", font=style, align='center')
    time.sleep(2)
    boss_fight()

def boss_fight():
    '''The fireball and bowser_ball lists are initialized and the lives are set as well.
    The program tells the user how to start and checks if the lives have changed of either 
    party. Bowser attacks steadily every 2.5 seconds whereas the user attacks when they
    click a.'''
    global fireballs, bowser_balls, user_lives, bowser_lives
    fireballs = []
    bowser_balls = []
    intro.clear()
    river.clear()
    intro.write("Click a to attack!")
    intro.goto(-300, 200)
    river.goto(300, 200)
    user_lives = 5
    bowser_lives = 5
    while user_lives > 0 or bowser_lives > 0:
        time.sleep(2.5)
        bowser_attack()
    if user_lives == 0:
        dead_end()
    elif bowser_lives == 0:
        win()

def if_collide(): #code from 1.1.8 but slightly modified
    '''Program goes through every ball in each fireball list and checks if it 
    has collided with the user or bowser. If so, they lose a life.'''
    global fireballs, bowser_balls, user_lives, bowser_lives
    intro.write(f"Lives left: {user_lives}", font=style, align='center')
    river.write(f"Lives left: {bowser_lives}", font=style, align='center')
    for ht in fireballs: 
        if (abs(ht.xcor() - bowser.xcor()) < 20) and (abs(ht.ycor() - bowser.ycor()) < 20):
                bowser_lives -= 1
                ht.hideturtle()
                fireballs.remove(ht)
    for vt in bowser_balls:
        if (abs(vt.xcor() - player.xcor()) < 20) and (abs(vt.ycor() - player.ycor()) < 20):
            user_lives -= 1
            vt.hideturtle()
            bowser_balls.remove(vt)
    if user_lives == 0:
        dead_end()
    elif bowser_lives == 0:
        win()

def bowser_attack():
    '''Updates the lives left in the program and initializes the turtles for when bowser attacks'''
    global fireballs, bowser_balls, user_lives, bowser_lives
    intro.write(f"Lives left: {user_lives}", font=style, align='center')
    river.write(f"Lives left: {bowser_lives}", font=style, align='center')
    '''code from 1.2.3 Apple Avalanche but slightly modified'''
    ball = trtl.Turtle()
    ball.hideturtle()
    ball.penup()
    ball.goto(-280, -130)
    ball.showturtle()
    ball.shape(bowser_fireball)
    bowser_balls.append(ball)
    ball.goto(300, -130)
    if user_lives == 0:
        dead_end()
    elif bowser_lives == 0:
        win()
           

def attack():
    '''Updates the lives left and initializes the turtles for when the user clicks a'''
    global fireballs, bowser_balls, user_lives, bowser_lives
    intro.write(f"Lives left: {user_lives}", font=style, align='center')
    river.write(f"Lives left: {bowser_lives}", font=style, align='center')
    '''code from 1.2.3 Apple Avalanche but slightly modified'''
    fireball = trtl.Turtle()
    fireball.hideturtle()
    fireball.penup()
    fireball.goto(-280, -130)
    fireball.showturtle()
    fireball.shape(turtle_fireball)
    fireballs.append(fireball)
    fireball.goto(300, -130)
    if user_lives == 0:
        dead_end()
    elif bowser_lives == 0:
        win()


def win():
    '''If the user defeats bowser, the program displays a screen showing that they win'''
    global player, choice1, choice2, yeschoice, nochoice, yeschoice2, nochoice2, river, intro, queen
    time.sleep(1)
    wn.bgpic('win.gif')
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

def dead_end(x=None, y=None): #takes parameters (x,y) as it is an onclick function
    '''If the user happens to make a mistake or die, it displays the you lose screen'''
    global player, choice1, choice2, yeschoice, nochoice, yeschoice2, nochoice2, river, intro, queen
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
wn.onkeypress(boss_dialogue, "r")
wn.onkeypress(begin, "s")
wn.onkeypress(attack, "a")
choice1.onclick(cave)
choice2.onclick(waterfall)

wn.listen()
wn.mainloop()