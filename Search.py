from tkinter import *
from tkinter import ttk
import tkinter
import random
import time


def search_complete():
    for identification_number in id_list:
        canvas.itemconfig(id_list[identification_number], fill='blue')
        iterations_label.config(text='Iterations: ' + str(iterations))



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
    search_complete()


def binary_search(values, search_for):
    global iterations
    iterations = 0
    size = len(values)
    left = 0
    right = size - 1
    while left <= right:
        iterations += 1
        mid = (left + right) // 2
        if values[mid] < search_for:
            canvas.itemconfig(id_list[left], fill='blue')
            canvas.update()
            time.sleep(0.01)
            left = mid + 1
        elif values[mid] > search_for:
            canvas.itemconfig(id_list[right], fill='blue')
            canvas.update()
            time.sleep(0.01)
            right = mid - 1
        else:
            search_complete()


def circle(x, y, interval):
    global object_id
    global total
    object_id = canvas.create_oval(x + spacing * interval, y + spacing,
                                   x + spacing * interval + diameter, y + spacing + diameter, outline='blue')
    id_list.append(object_id)
    total += 1


def generate_visual(prompt):
    global search_for_value
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
            if spacing_interval == 70:
                y += spacing
                spacing_interval = 0
        search_for_value = id_list[search_for_index]
        canvas.itemconfig(search_for_value, fill='blue')
    except ValueError:
        prompt.configure(fg='red')


window = Tk()
win_w = 1512
win_h = 1044

canvas = Canvas(window, width=win_w, height=win_h, bg='black')
canvas.pack()

user_prompt = Label(window, text='Please enter a number: 0 < n < 4200', bg='black', fg='white')
user_prompt.place(x=50, y=65)
user_input = Text(window, width=25, height=1)
user_input.place(x=50, y=100)
generate = Button(window, text='Generate', bg='black', fg='white', command=lambda: generate_visual(user_prompt))
generate.place(x=50, y=135)

spacing = 16
diameter = 8

object_id = 0
id_list = []
total = 0

search_for_value = 0
iterations = 0

iterations_label = Label(window, text='Iterations: ' + str(iterations), bg='black', fg='white')
iterations_label.place(x=720, y=25)
linear_search_button = Button(window, text='Linear Search', command=lambda: linear_search(id_list, search_for_value))
linear_search_button.place(x=50, y=175)
binary_search_button = Button(window, text='Binary Search', command=lambda: binary_search(id_list, search_for_value))
binary_search_button.place(x=50, y=205)

window.mainloop()
