from engi1020.arduino import *
import random

category= input('Choose: animal, country, colors: ').lower()

#script for animal category
if category == 'animal':
    def animalset():
        animalList=[["tiger"],["lion"], ['cat'], ['dog'], ['elephant'],['snake']]
        animalSet = set(animalList[random.randint(0,6)])
        return animalSet
    def userset(x):
        user_list= []
        user_list.append(x)
        user_set = set(user_list)
        return user_set
    def gamedecision(x):
        y = animalset()
        realset = y.intersection(userset(x))
        buttonPressed = digital_read(dpin)
        while realset == set():
                lcd_clear()
                lcd_rgb(255,0,0)
                buzzer_note(bnpin, 275, 500)
                realset = y.intersection(userset(input('guess or press the button for a hint').lower()))
                while buttonPressed == 0:
                    buttonPressed = digital_read(dpin)
                    if buttonPressed == 1:
                        for i in y:
                            print('This is a', len(i), 'letter word')
                    else:
                        break

        else:
            lcd_clear()
            lcd_rgb(0,255,0)
            lcd_print('you won')
            buzzer_note(bnpin, 270, 700)
            buzzer_note(bnpin, 215, 500)
            buzzer_note(bnpin, 250, 1000)
    game = gamedecision(input('Guess the word').lower())

#script for country category
elif category == 'country':
    def countryset():
        countryList = [['america'], ['brazil'], ['canada'],['saudiarabia'],['england'],['kenya'], ['australia']]
        countrySet = set(countryList[random.randint(0, 7)])
        return countrySet


    def userset(x):
        user_list = []
        user_list.append(x)
        user_set = set(user_list)
        return user_set


    def gamedecision(x):
        y = countryset()
        realset = y.intersection(userset(x))
        buttonPressed = digital_read(dpin)
        while realset == set():
            lcd_clear()
            lcd_rgb(255, 0, 0)
            buzzer_note(bnpin, 275, 500)
            realset = y.intersection(userset(input('guess or press the button for a hint').lower()))
            while buttonPressed == 0:
                buttonPressed = digital_read(dpin)
                if buttonPressed == 1:
                    for i in y:
                        print('This is a', len(i), 'letter word')
                else:
                    break


        else:
            lcd_clear()
            lcd_rgb(0, 255, 0)
            lcd_print('you won')
            buzzer_note(bnpin, 270, 700)
            buzzer_note(bnpin, 215, 500)
            buzzer_note(bnpin, 250, 1000)
    game = gamedecision(input('Guess the word').lower())

#script for colors category
elif category == 'colors':
    def colorset():
        colorList = [['red'], ["orange"], ['yellow'], ['green'], ['blue'], ['purple'], ['pink']]
        colorSet = set(colorList[random.randint(0, 8)])
        return colorSet


    def userset(x):
        user_list = []
        user_list.append(x)
        user_set = set(user_list)
        return user_set


    def gamedecision(x):
        y = colorset()
        realset = y.intersection(userset(x))
        buttonPressed = digital_read(dpin)
        while realset == set():
            lcd_clear()
            lcd_rgb(255, 0, 0)
            buzzer_note(bpin, 275, 500)
            realset = y.intersection(userset(input('guess or press the button for a hint').lower()))
            while buttonPressed == 0:
                buttonPressed = digital_read(dpin)
                if buttonPressed == 1:
                    for i in y:
                        print('This is a', len(i), 'letter word')
                else:
                    break


        else:
            lcd_clear()
            lcd_rgb(0, 255, 0)
            lcd_print('you won')
            buzzer_note(bnpin, 270, 700)
            buzzer_note(bnpin, 215, 500)
            buzzer_note(bnpin, 250, 1000)
    game = gamedecision(input('Guess the word').lower())













