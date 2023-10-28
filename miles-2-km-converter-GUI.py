
#                        DESCRIPTION
             --------------------------------

# In this project, we create a simple project, we create a simple miles to KM converter GUI using Python TKinter.
# We want the user to be able to enter miles (integer or float), and click on a "calculate" button to get the
# the equivalence in kilometers with wording that says is equal to <the equivalence in km>
# Please see the screenshot of what the final GUI looks like. 
# See the screenshot of the project outcome [here] (https://github.com/Ray-DevOps/Python-Notes/blob/main/GUI-with-Python-TKinter/miles-to-km-converter/miles-2-km.jpg)


#                         SOLUTION
               --------------------------------
from tkinter import *                                          # We import all the classes in the tkinter module since we would need a bunch of them

window = Tk()                                                  # We create a window object from the window class and define the specifications of the GUI window
window.minsize(width=500, height=300)
window.title("Miles to km Converter")



first_unit = Label(text="Miles", font=("Arial", 16))          # We create objects from the label class to write the various texts to appear on the GUI
first_unit.place(x=340, y=40)

second_unit = Label(text=" Km", font=("Arial", 16))
second_unit.place(x=340, y=90)

response = Label(text="is equal to", font=("Arial", 16))
response.place(x=140, y=90)


input = Entry(width=10, font=("Arial", 18))                   # We create a text entry field from the Entry class which allows the user to enter the number of miles to be converted
input.place(x=200, y=40)


result = Label(text=f" ", font=("Arial", 16))                 # The results label is a text but left for now as an empty string. The empty field would be replaced by the calculation on line 38
result.place(x=270, y=90)
def button_clicked():
    result.config(text=f"{round(float(input.get()) * 1.60934, 2)}")

button = Button(text="Calculate", command=button_clicked, font=("Arial", 15))
button.place(x=220, y=130)


window.mainloop()                                            # window.mainloop() tells Python to run the Tkinter event loop. This method listens for events, such as button clicks or keypresses, 
                                                             # and blocks any code that comes after it from running until you close the window where you called the method.
