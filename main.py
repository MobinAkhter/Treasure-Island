# ASCII ART code
# 3 single quotes allow the print statement to work with multiple lines
print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

choiceOne = input("You're at a crossroad, where do you want to go? Type 'left' or 'right'.\n").lower()

if choiceOne == "right":
    print("You fell into a hole. Game Over.")
elif choiceOne == "left":
    choiceTwo = input("You've come to a lake. There is an island in the middle of the lake. Type 'wait' to wait for a "
                      "boat. Type "
                      "'swim' to swim across.\n").lower()
    if choiceTwo == "wait":
        choiceThree = input(
            "You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow, and one blue. "
            "Which color do you choose?\n").lower()
        if choiceThree == "red":
            print("Its a room full of fire. Game over!")
        elif choiceThree == "yellow":
            print("You found the treasure. You Win!")
        elif choiceThree == "blue":
            print("You entered a room of beasts. Game Over.")

    else:
        print("You got attacked by an angry trout. Game over.")
