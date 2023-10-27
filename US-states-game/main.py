
#                                         DESCRIPTION
#                                  ------------------------

# In this project, we are provided with an image of the map of the united states with names of states blanked out (blank_states_img.jpg).
# We are also presented with a cvs file with names of the 50 states as well as their x and y coordinates (see 50_states.csv)
# The player will be presented with a prompt to enter the name of any state. The purpose of the game is to test the
# players knowledge of the states in the United States. Entries are case insensitive.
# If the player correctly enters a state, the player scores a point and is asked to enter another state.
# The prompt will show the players progress, something like "11/50 States Correct".
# The game ends when the player enters all 50 states, or when the player enters the word "exit" (case insensitive).
# If the player exits the game, the game prints a csv file for the remainder states that the player didn't enter.
# This is presented in a file called "states_to_learn.csv".


#                                         SOLUTION
#                                 -------------------------

import turtle
import pandas
from writer import Writer

screen= turtle.Screen()
image = "blank_states_img.gif"
screen.addshape(image)
screen.title("US States Game")
turtle.shape(image)

data = pandas.read_csv("50_states.csv")
states = data["state"].tolist()
x_cord = data["x"].tolist()
y_cord = data["y"].tolist()
state_cords = list(zip(x_cord, y_cord))

writer = Writer()

game_on = True

guessed_states = set()

while len(guessed_states) < 50 and game_on == True:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 States Correct", prompt="What's another state's name?")
    answer_state = answer_state.capitalize()
    if answer_state == "Exit":
        game_on = False
        break
    elif answer_state in states:
        guessed_states.add(answer_state)
        ind = states.index(answer_state)
        write_cord = state_cords[ind]
        writer.goto(write_cord)
        writer.write(f"{answer_state}", move=False, align='center', font=('Arial', 8, 'normal'))
    else:
        pass

un_guessed = [ ]

for state in states:
    if state not in guessed_states:
        un_guessed.append(state)

df = pandas.DataFrame(un_guessed)
df.to_csv("states_to_learn.csv", index=True)
turtle.mainloop()




