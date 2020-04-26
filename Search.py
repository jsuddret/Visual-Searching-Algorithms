from tkinter import *
from tkinter import ttk
from math import sqrt
import tkinter
import random
import time


def search_complete():
    for identification_number in range(1, len(id_list)):
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
            return


def jump_search(values, search_for):
    global iterations
    iterations = 0
    low = 0
    interval = int(sqrt(len(values)))
    for index in range(0, len(values), interval):
        iterations += 1
        if values[index] < search_for:
            canvas.itemconfig(id_list[index], fill='blue')
            canvas.update()
            time.sleep(0.01)
            low = index
        elif values[index] == search_for:
            return index
        else:
            search_complete()
            break
    new = low
    for val in values[low:]:
        if new == search_for:
            canvas.itemconfig(id_list[val], fill='blue')
            canvas.update()
            time.sleep(0.01)

            return new
    search_complete()
    return


def fibonacci_search(values, search_for):
    global iterations
    iterations = 0
    fib_minus_2 = 0
    fib_minus_1 = 1
    fib = fib_minus_1 + fib_minus_2
    while fib < len(values):
        iterations += 1
        canvas.itemconfig(id_list[fib], fill='blue')
        canvas.update()
        time.sleep(0.01)
        fib_minus_2 = fib_minus_1
        fib_minus_1 = fib
        fib = fib_minus_1 + fib_minus_2
    index = -1
    while fib > 1:
        iterations += 1
        i = min(index + fib_minus_2, len(values) - 1)
        canvas.itemconfig(id_list[i], fill='blue')
        canvas.update()
        time.sleep(0.01)
        if values[i] < search_for:
            fib = fib_minus_1
            fib_minus_1 = fib_minus_2
            fib_minus_2 = fib - fib_minus_1
            index = i
        elif values[i] > search_for:
            fib = fib_minus_2
            fib_minus_1 -= fib_minus_2
            fib_minus_2 = fib - fib_minus_1
        else:
            search_complete()
            return
    if fib_minus_1 and index < len(values) - 1 and values[index + 1] == search_for:
        return index + 1
    return


def exponential_search(values, search_for):
    global iterations
    iterations = 0
    if values[0] == search_for:
        return 0
    index = 1
    while index < len(values) and values[index] <= search_for:
        iterations += 1
        canvas.itemconfig(id_list[index], fill='blue')
        canvas.update()
        time.sleep(0.01)
        index = index * 2
    return binary_search(values[:min(index, len(values))], search_for)


def interpolation_search(values, search_for):
    global iterations
    iterations = 0
    low = 0
    high = len(values) - 1
    while low <= high and values[low] <= search_for <= values[high]:
        index = low + int(((float(high - low) / (values[high] - values[low])) * (search_for - values[low])))
        iterations += 1
        if values[index] == search_for:
            search_complete()
            return index
        if values[index] < search_for:
            canvas.itemconfig(id_list[index], fill='blue')
            canvas.update()
            time.sleep(0.01)
            low = index + 1
        else:
            canvas.itemconfig(id_list[index], fill='blue')
            canvas.update()
            time.sleep(0.01)
            high = index - 1
    return -1


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
        if user_value <= 4200:
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
        else:
            prompt.configure(fg='red')
    except ValueError:
        prompt.configure(fg='red')


window = Tk()
win_w = 1512
win_h = 1044
window.config(bg='black')

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
jump_search_button = Button(window, text='Jump Search', command=lambda: jump_search(id_list, search_for_value))
jump_search_button.place(x=50, y=235)
fibonacci_search_button = Button(window, text='Fibonacci Search',
                                 command=lambda: fibonacci_search(id_list, search_for_value))
fibonacci_search_button.place(x=50, y=265)
exponential_search_button = Button(window, text='Exponential Search',
                                   command=lambda: exponential_search(id_list, search_for_value))
exponential_search_button.place(x=50, y=295)
interpolation_search_button = Button(window, text='Interpolation Search',
                                     command=lambda: interpolation_search(id_list, search_for_value))
interpolation_search_button.place(x=50, y=325)

window.mainloop()
