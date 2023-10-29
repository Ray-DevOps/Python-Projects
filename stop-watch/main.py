
#                            DESCRIPTION
#                 --------------------------------------

# In this project, we build a stop-watch whereby when we click on the "start" button, the watch starts a count-down
# from 5 minutes till 0. We use a tomato image for design. See tomato.png [here] (https://github.com/Ray-DevOps/Python-Projects/blob/main/stop-watch/tomato.png)
# We use tkinter to build the widgets of the GUI such as the buttons and labels
# We use canvas to be able to write on the background image, etc. Canvas allows us to write or paste an image on another image


from tkinter import *
import math
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"


def start_timer():
    count_down(5 * 60)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):

    count_min = math.floor(count/60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        window.after(1000, count_down, count - 1)


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro")
window.minsize(width=500, height=400)
window.configure(background="yellow")


canvas = Canvas(width=500, height=400, bg=GREEN, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(250, 185, image=tomato_img)
timer_text = canvas.create_text(250, 200, text="00:00", fill="green", font=("Arial", 20, "bold"))
canvas.create_text(250, 40, text="Timer", fill="grey", font=("Courier", 40))
canvas.pack()

start_button = Button(text="Start", command=start_timer, font=("Arial", 8))
start_button.place(x=100, y=300)

def reset_timer():
    canvas.itemconfig(timer_text, text="00:00")

reset_button = Button(text="Reset", command=reset_timer, font=("Arial", 8))
reset_button.place(x=360, y=300)



window.mainloop()               # window.mainloop() tells Python to run the Tkinter event loop. This method listens for events, such as button clicks or keypresses, 
                                # and blocks any code that comes after it from running until you close the window where you called the method.
