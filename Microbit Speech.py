from microbit import *
import speech
import random 

Lengthwordarray = 3

Subject = ["He", "Mike", "Clarke",]
Verb = ["Talks", "Eats", "Drinks"]
Rest = ["hard", "at school", "coffee"]

def sayTheWords1(word) :
    print(word)
    speech.say(word, speed=120, pitch=100, throat=100, mouth=200)
    sleep(500)
    
def sayTheWords2():
    willekeurigGetal = random.randint(0, Lengthwordarray - 1)
    display.show(willekeurigGetal)
    sayTheWords1(Subject[willekeurigGetal])
    sayTheWords1(Verb[willekeurigGetal])
    sayTheWords1(Rest[willekeurigGetal])
    
while True:
    if button_a.is_pressed():
        display.show(Image.HAPPY)
        sayTheWords1("Hello. I am happy")
    elif button_b.is_pressed():
        display.show(Image.SAD)
        sayTheWords1("Why are you sad?")
    elif display.read_light_level() < 40:
        sayTheWords2()
    else:
        display.show(Image.SQUARE)