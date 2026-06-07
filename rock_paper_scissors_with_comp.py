from logging import log
import random
a=["rock", "paper", "scissors"]
winner=""
first_usr_name = "AIII"
second_usr_name = input("Welcome to rock,paper,scissor game. \nPlease write your name for your player\n")
first_usr_choice = random.choice(a)
second_usr_choice = input("Dear " + second_usr_name + ", select your choice(rock,paper or scissors)\n")
if first_usr_choice == "rock" or "scissors" or "paper" and second_usr_choice == "rock" or "scissors" or "paper":
    if first_usr_choice == "rock":
        if second_usr_choice == "scissors":
            winner = first_usr_name
        elif second_usr_choice == "paper":
            winner = second_usr_name
    elif first_usr_choice == "paper":
        if second_usr_choice == "scissors":
            winner = second_usr_name
        elif second_usr_name == "rock":
            winner = first_usr_name
    elif first_usr_choice == "scissors":
        if second_usr_choice == "paper":
            winner = first_usr_name
        elif second_usr_choice == "rock":
            winner = second_usr_name
    
    print("Winner is " + str(winner))
else:
    print("Users don't choice rightly ")

if first_usr_choice == second_usr_choice:
    print(first_usr_name + " and " + second_usr_name +" is equal ")

print("AI choosed this section " + first_usr_choice)

