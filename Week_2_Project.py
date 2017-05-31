# Rock-paper-scissors-lizard-Spock template
#http://www.codeskulptor.org/#user42_xYwMiGTRXM_0.py

# The key idea of this program is to equate the strings
# "rock", "paper", "scissors", "lizard", "Spock" to numbers
# as follows:
#
# 0 - rock
# 1 - Spock
# 2 - paper
# 3 - lizard
# 4 - scissors

import random


def name_to_number(name):

    if name == "rock":
        return 0
    elif name == "Spock":
        return 1
    elif name == "paper":
        return 2
    elif name == "lizard":
        return 3
    elif name == "scissors":
        return 4
    else:
        return "Not a valid name."


def number_to_name(number):
    if number == 0:
        return "rock"
    if number == 1:
        return "Spock"
    if number == 2:
        return "paper"
    if number == 3:
        return "lizard"
    if number == 4:
        return "scissors"
    else:
        return "Not a valid number."

    

def rpsls(player_choice):     
    print " " 
    print "Players chooses " + player_choice
    player_number = name_to_number(player_choice)
    comp_number = random.randrange(0,5)
    comp_choice = number_to_name(comp_number)   
    print "Computer chooses " + comp_choice 
    diff_mod_5 = (comp_number - player_number) % 5
    
    if diff_mod_5 == 1 or diff_mod_5 == 2:
        print "Computer Wins!"
    elif diff_mod_5 == 3 or diff_mod_5 == 4:
        print "Player Wins!"
    else:
        print "Tie!"
    
rpsls("rock")
rpsls("Spock")
rpsls("paper")
rpsls("lizard")
rpsls("scissors")

