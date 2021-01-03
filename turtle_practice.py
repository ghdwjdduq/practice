
import random
import turtle
from imageTools import *


from tkinter import *

rootWin = None
E1 = None
labelDisplay = None
txt = None
newLabel = None


def mainGUI():
    global rootWin
    global E1
    global txt
    global newLabel

    rootWin = Tk()
    rootWin.title("Hangman")

    labelInstruct = Label(rootWin, text="Guess the word!")
    labelInstruct.grid(row=0, column=0)

    txt = StringVar()

    L1 = Label(rootWin, text="let's play?")
    L1.grid(row=3, column=0)

    testButton = Button(rootWin, text="start", font="TimesNewRoman 12", bg="#997711", fg="blue",
                        command=testButtonResponse)
    testButton.grid(row=1, column=1)
    newLabel = Label(rootWin)
    newLabel.grid(row=2, column=2)

    rootWin.mainloop()

def testButtonResponse():
    global newLabel
    txt = newLabel["text"]
    print("clicked")
    turtMove()




hangy = turtle.Turtle()

def drawHang():
    hangy.goto(-10,0)
    hangy.left(90)
    hangy.forward(200)
    hangy.right(90)
    hangy.forward(200)
    hangy.right(90)
    hangy.forward(30)
    #face
    hangy.up()
    hangy.goto(150, 130)
    hangy.down()
    hangy.circle(40)
    hangy.up()
    hangy.goto(190, 90)
    hangy.down()

def drawBody():
    hangy.forward(90)


def drawArm():
    hangy.right(90)
    hangy.forward(50)
    hangy.forward(-50)

def drawHead():
    hangy.up()
    hangy.goto(150, 130)
    hangy.down()
    hangy.circle(40)
    hangy.up()
    hangy.goto(190, 90)


def drawleg():
    hangy.right(20)
    hangy.forward(80)
    hangy.forward(-80)

def drawotherleg():
    hangy.left(40)
    hangy.forward(80)
    hangy.forward(-80)
    hangy.right(200)
    hangy.forward(30)

def drawOtherArm():
    hangy.left(180)
    hangy.forward(50)
    hangy.up()

def drawEye():
    hangy.goto(170, 140)
    hangy.down()
    hangy.circle(10)
    hangy.up()

def drawOtherEye():
    hangy.goto(220, 140)
    hangy.down()
    hangy.circle(10)
    hangy.up()

def sadFace():
    hangy.goto(190, 125)
    hangy.down()
    hangy.circle(5)
    hangy.up()




def drawHangy(accumulator):
    if accumulator == 0:
        return
    if accumulator == 1:
        drawHang()
    if accumulator == 2:
        # drawHang()
        drawBody()
    if accumulator == 3:
        # drawHang()
        # drawBody()
        drawleg()
    if accumulator == 4:
        # drawHang()
        # drawBody()
        # drawleg()
        drawotherleg()
    if accumulator == 5:

        # drawHang()
        # drawBody()
        # drawleg()
        # drawotherleg()
        drawArm()

    if accumulator == 6:

        # drawHang()
        # drawBody()
        # drawleg()
        # drawotherleg()
        # drawArm()
        drawOtherArm()

    if accumulator == 7:

        # drawHang()
        # drawBody()
        # drawleg()
        # drawotherleg()
        # drawArm()
        # drawOtherArm()
        drawEye()

    if accumulator == 8:

        # drawHang()
        # drawBody()
        # drawleg()
        # drawotherleg()
        # drawArm()
        # drawOtherArm()
        # drawEye()
        drawOtherEye()

    if accumulator == 9:
        # drawHang()
        # drawBody()
        # drawleg()
        # drawotherleg()
        # drawArm()
        # drawOtherArm()
        # drawEye()
        # drawOtherEye()
        sadFace()

# drawHangy(9)


t = turtle.Turtle()
turt = turtle.Turtle()
# p = turtle.Turtle()
win = turtle.Screen()

listed_letters = ["orange"]

def turtMove():
    chosen_word = random.choice(listed_letters).lower()
    a = (len((chosen_word)))
    # print(chosen_word)
    print("there are" , a, "letters in this word")
    for i in range(a):
        t.up()
        t.goto(35*i, i+50)
        t.down()
        t.forward(20)
        t.up()
    errorcount = 0
    tries=9
    wordList = [None] * len(chosen_word)
    print(wordList)
    for i in range(len(wordList)):
        if wordList[i] == None:
            wordList[i] = ""
    print(wordList)
    t.goto(-70,0)
    while tries !=0:
        user_response = input("What do you think the word/letter will be?")
        print(user_response)
        if user_response == chosen_word:
            print("you did it!")
            return
        elif user_response in chosen_word:
            print("yay")
            tries += -1
            print("you have", tries, "tries remaining")
            for i in range(len(chosen_word)):
                if chosen_word[i] == user_response:
                    turt.up()
                    turt.goto(35*i, i+50)
                    turt.down()
                    turt.write(user_response, font=("Arial", 15, "normal"))
            print(chosen_word)
            for i in range(len(chosen_word)):
                if chosen_word[i] == user_response:
                    wordList[i] = user_response
            print(wordList)
            if ''.join(wordList) == chosen_word:
                print("You've guessed the word ", chosen_word)
                return
        else:
            print("sad")
            tries+=-1
            print("you have", tries, "tries remaining")
            errorcount += 1
            print("you made", errorcount, "error(s)")
            drawHangy(errorcount)
            if tries == 0:
                print("YOU LOSE")

mainGUI()
win.exitonclick()