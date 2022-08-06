# template for "Guess the number" mini-project
# input will come from buttons and an input field
# all output for the game will be printed in the console

import simplegui
import random
import math


#initialize global variables used in the code
secret_number = 0
range = 100
counter = 0


# helper function to start and restart the game
def new_game():
    print " " 
    print "New game. Range is from 0 to", int(range)
    global secret_number
    if range == 100:
        secret_number = random.randrange(0, 100)
    else:
        secret_number = random.randrange(0, 1000)
        
    print "Number of remaining guesses is", int(num_guess())
    return secret_number    
        
        
# define event handlers for control panel
def range100():
    global range
    range = 100
    new_game()
    return range     

def range1000():
    # button that changes the range to [0,1000) and starts a new game     
    global range
    range = 1000
    new_game()
    return range

def num_guess():
    global counter
    counter = math.ceil(math.log(range, 2))
    return counter

    
def input_guess(guess):
    print " "
    guess = int(guess)
    print "Guess was", guess
    global counter
    
    if counter > 0:
        
        if guess > secret_number:
            counter -= 1
            print "Number of remianing guesses is", int(counter)
            print "Higher!"
        elif guess < secret_number:
            counter -= 1
            print "Number of remianing guesses is", int(counter)
            print "Lower!"
        else:
            print "Correct!"
            
    else:
        print "You are out of guesses. You Lose! - Game Over!"
        new_game()

    
# create frame
f = simplegui.create_frame("Guess the number", 200, 200)

# register event handlers for control elements and start frame
f.add_button("Range is [0, 100)", range100, 200)
f.add_button("Range is [0, 1000)", range1000, 200)
f.add_input("Enter a guess", input_guess, 200)

# call new_game 
new_game()


# always remember to check your completed program against the grading rubric
