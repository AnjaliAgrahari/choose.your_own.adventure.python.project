name = input("Type your name: ")
print("Welcome", name, "to the adventure!")
answer = input("You are on a dirt road, it has come to an end and you can go left or right. which way would u like to choose to go? ").lower()

if answer == "left":
    answer = input("You come to a river, you can walk around it or swim accross? Type walk to walk around and swim to swim across: ").lower()
    
    if answer == "swim":
        print("Your swim across and were eaten by an alligator")
    elif answer == "walk":
        print("you walked for many miles , ran out of water and you lost the game ") 
    else:
        print()

elif answer == "right":
    answer = input("you come to a bridge ,it wobbly, do you want to cross or head back? ").lower()
    if answer == "back":
        print("You go back and lose")
    elif answer == "cross":
        answer =  input("You cross the bridge and meet a strange. Do you talk to stranger. Do you talk to them (yes/no)? ").lower()
        if answer =="yes":
            print("you talk to the stranger and they give you gold. You WIN!")
        elif answer == "no":
            print("You don't talk to stranger they are offended and you lose. " )
        else:
         print("Not a valid option. You lose :(")

else:
 print("Not a valid option. You lose :(")
