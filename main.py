import tkinter
from tkinter import *

window = Tk()
window.title("BMI Calculator")
window.minsize(width=300, height=250)

weight_input_label = Label(text="Enter Your Weight(kg)")
weight_input_label.config(fg="black")
weight_input_label.pack()

weight_input = Entry(width=10)
weight_input.focus()
weight_input.pack()

height_input_label = Label(text="Enter Your Height(cm)")
height_input_label.config(fg="black")
height_input_label.pack()

height_input = Entry(width=10)
height_input.pack()


def button_clicked():
    weight = weight_input.get()
    height = height_input.get()

    if weight == "" or height == "":
        message.config(text="Enter both weight and height!")
    else:
        try:
            bmi = float(weight) / (float(height) / 100) ** 2
            result_string = write_result(bmi)
            message.config(text=result_string)
        except:
            message.config(text="Enter a valid number!")


my_button = Button(text="Calculate", command=button_clicked)
my_button.config(bg="white")
my_button.pack()

message = Label()
message.pack()


def write_result(bmi):
    result_string = f"Your BMI is : {round(bmi, 2)}, you are "
    if bmi <= 16:
        result_string += "severely thin!"
    elif 16 < bmi <= 17:
        result_string += "moderately thin"
    elif 17 < bmi <= 18.5:
        result_string += "mild thin"
    elif 18.5 < bmi <= 25:
        result_string += "normal"
    elif 25 < bmi <= 30:
        result_string += "overweight"
    elif 30 < bmi <= 35:
        result_string += "obese class 1"
    elif 35 < bmi <= 40:
        result_string += "obese class 2"
    else:
        result_string += "obese class 3"

    return result_string

tkinter.mainloop()
