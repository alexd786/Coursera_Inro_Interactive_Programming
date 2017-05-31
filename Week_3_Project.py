#http://www.codeskulptor.org/#user42_EZ1KWjIDtW_0.py

import random
import simplegui
import math

guesses_left = 7
num_range = 100
secret_number = 0
guesses_left_game = 0

# helper function to start and restart the game
def new_game():
    global secret_number, guesses_left, num_range, guesses_left_game
    secret_number = random.randrange(0,num_range)
    guesses_left_game = guesses_left
    

# define event handlers for control panel
def range100():
    print "New game. Range is [0,100)"
    global guesses_left, num_range
    guesses_left = 7
    num_range = 100
    new_game()   
    

def range1000():
    print "New game. Range is [0,1000)"
    global guesses_left, num_range
    guesses_left = 10
    num_range = 1000
    new_game()
    
   
    
def input_guess(guess):
    global guesses_left_game, secret_number
    guess = int(guess)
    print "Guess was " + str(guess)
    if guess < secret_number:
        print "Higher"
    elif guess > secret_number:
        print "Lower"
    else:
        print "Correct"
        print " "
        new_game()
        return
    guesses_left_game -= 1
    if guesses_left_game == 0:
        print "You ran out of guesses. The correct number was " + str(secret_number) 
        print " "
        new_game()      
    else:
        print "Number of remaining guesses is " + str(guesses_left_game)
        print " "
    
    

    
# create frame
frame = simplegui.create_frame("Guess The Number",200,200)
frame.add_input("Input Guess", input_guess, 200)
frame.add_button("Range is [0,100)",range100,200)
frame.add_button("Range is [0,1000)",range1000,200)

# call new_game 
new_game()