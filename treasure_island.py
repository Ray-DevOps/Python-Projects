# This code is the code for the Treasure Island Game. To clearly understand the requirements, see the Treasure 

# Island flow chart at [here] (https://github.com/Ray-DevOps/Python-Projects/blob/main/Treasure%20Island.pdf)



print("Welcome to Treasure Island. Your mission is to find the treasure.")

direction = (input("You are at the first intersection. Choose 'left' or 'right': ")).lower()

if direction == 'left':
    swim_or_wait = (input("Great job. You made it safely to the lake. Would you swim or wait?: ")).lower()
    if swim_or_wait == "wait":
        door_color = (input("Great job. You made it to the final door. Which door would  you take? Blue, yellow, or red?: ")).lower()
        if door_color == "yellow":
            print("Congratulations! You have won")
        elif door_color == "red":
            print("Oh no! You were burned by fire. Game Over.")
        elif door_color == "blue":
            print("Oh sorry! You were eaten by beasts. Game Over.")
        else:
            print("Sorry! You took the wrong door. Game over")
    else:
        print("Oh no! You were attacked by trout.Game Over!.")
else:
    print("You fell into a hole. Game over!")
