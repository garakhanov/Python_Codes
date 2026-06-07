first_usr_name = input("Please write your name for first player\n")
second_usr_name = input("Please write your name for second player\n")
first_usr_choice = input("Dear " + first_usr_name + ", select your choice(rock,paper or scissors)\n")
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
    print("Winner is " + winner)
else:
    print("Users don't choice rightly ")

if first_usr_choice == second_usr_choice:
    print(first_usr_name + " and " + second_usr_name +" is equal ")

