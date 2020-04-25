from tkinter import *
from tkinter import ttk
import tkinter
import random
import time


def linear_search(values, search_for):
    global iterations
    iterations = 0
    search_at = 0
    search_res = False
    while search_at < len(values) and search_res is False:
        iterations += 1
        canvas.itemconfig(id_list[search_at], fill='blue')
        canvas.update()
        if values[search_at] == search_for:
            search_res = True
        else:
            search_at += 1
        time.sleep(0.01)


def interpolation_search(values, search_for):
    global iterations
    iterations = 0
    index_zero = 0
    index_n = (len(values) - 1)
    while index_zero <= index_n and values[index_zero] <= search_for <= values[index_n]:
        iterations += 1
        canvas.itemconfig(id_list[index_zero], fill='blue')
        canvas.update()
        index_middle = index_zero + int(((float(index_n - index_zero) / (values[index_n] - values[index_zero]))
                                         * (search_for - values[index_zero])))
        if values[index_middle] == search_for:
            return
        if values[index_middle] < search_for:
            index_zero = index_middle + 1
    return


def circle(x, y, interval):
    global object_id
    global total
    object_id = canvas.create_oval(x + spacing * interval, y + spacing,
                                   x + spacing * interval + diameter, y + spacing + diameter, outline='blue')
    id_list.append(object_id)
    total += 1


def generate_visual(prompt):
    global search_for_index
    search_for_index = 0
    id_list.clear()
    canvas.delete('all')
    try:
        user_value = int(user_input.get("1.0", END))
        prompt.configure(fg='white')
        search_for_index = random.randint(1, user_value - 1)
        x = 325
        y = 60
        spacing_interval = 0
        for i in range(user_value):
            circle(x, y, spacing_interval)
            spacing_interval += 1
            if spacing_interval == 38:
                y += spacing
                spacing_interval = 0
        search_for_value = id_list[search_for_index]
        canvas.itemconfig(search_for_value, fill='blue')
    except ValueError:
        prompt.configure(fg='red')
    print(id_list)


window = Tk()
win_w = 1512
win_h = 1044

canvas = Canvas(window, width=win_w, height=win_h, bg='black')
canvas.pack()

user_prompt = Label(window, text='Please enter a number: 0 < n < 1216', bg='black', fg='white')
user_prompt.place(x=50, y=65)
user_input = Text(window, width=25, height=1)
user_input.place(x=50, y=100)
generate = Button(window, text='Generate', bg='black', fg='white', command=lambda: generate_visual(user_prompt))
generate.place(x=50, y=135)

spacing = 30
diameter = 15

object_id = 0
id_list = []
total = 0

search_for_index = 0
search_for_value = 0
iterations = 0

linear_search_button = Button(window, text='Linear Search', command=lambda: linear_search(id_list, search_for_value))
linear_search_button.place(x=50, y=205)
interpolation_search_button = Button(window, text='Interpolation Search', command=lambda: interpolation_search(id_list, search_for_value))
interpolation_search_button.place(x=50, y=240)

window.mainloop()
