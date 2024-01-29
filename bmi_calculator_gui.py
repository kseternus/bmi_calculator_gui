import tkinter as tk
from tkinter import ttk


def calculate_bmi(*args):
    height = slider_m.get() / 100
    weight = int(weight_value_label['text'])
    bmi = weight / (height ** 2)
    output_str.set(f'{bmi:.1f}')
    value_label.configure(text=get_current_value())
    if bmi < 15.9:
        classification['text'] = 'Severe Thinness'
        classification.config(foreground='#8b0000')
    elif (bmi > 16) and (bmi < 16.9):
        classification['text'] = 'Moderate Thinness'
        classification.config(foreground='#e64747')
    elif (bmi > 17) and (bmi < 18.4):
        classification['text'] = 'Mild Thinness'
        classification.config(foreground='#e6e22e')
    elif (bmi > 18.5) and (bmi < 24.9):
        classification['text'] = 'Normal'
        classification.config(foreground='#ffffff')
    elif (bmi > 25) and (bmi < 29.9):
        classification['text'] = 'Overweight'
        classification.config(foreground='#e6e22e')
    elif (bmi > 30) and (bmi < 34.9):
        classification['text'] = 'Obese Class I'
        classification.config(foreground='#e09c3b')
    elif (bmi > 35) and (bmi < 40):
        classification['text'] = 'Obese Class II'
        classification.config(foreground='#e64747')
    elif bmi > 40.1:
        classification['text'] = 'Obese Class III'
        classification.config(foreground='#8b0000')


def add():
    if weight_value_label['text'] < 300:
        weight_value_label['text'] += 1
    else:
        pass
    calculate_bmi()


def subtract():
    if weight_value_label['text'] > 30:
        weight_value_label['text'] -= 1
    else:
        pass
    calculate_bmi()


def get_current_value():
    return f'{current_value.get():.1f}'


window = tk.Tk()
window.title('BMI calculator')
window.geometry('450x450')
window.resizable(False, False)
window.config(bg='#137a63')

output_str = tk.StringVar()
output_window = tk.Label(master=window,
                         font='Futura 80 bold',
                         textvariable=output_str,
                         foreground='#ffffff',
                         background='#137a63')
output_window.pack(pady=20)

classification = tk.Label(master=window,
                          font='Futura 18 bold',
                          text='Normal',
                          foreground='#ffffff',
                          background='#137a63')
classification.pack()

input_window_weight = tk.Frame(master=window, background='#137a63')
weight_value_label = tk.Label(master=input_window_weight,
                              font='Futura 30',
                              text=75,
                              foreground='#ffffff',
                              background='#137a63')
weight_label = tk.Label(master=input_window_weight,
                        font='Futura 30',
                        text='kg',
                        foreground='#ffffff',
                        background='#137a63')
plus = tk.Button(master=input_window_weight,
                 font='Futura 20',
                 command=add,
                 text='+',
                 bd=0,
                 foreground='#ffffff',
                 background='#3078d7',
                 width=2)
minus = tk.Button(master=input_window_weight,
                  font='Futura 20',
                  command=subtract,
                  text='-', bd=0,
                  foreground='#ffffff',
                  background='#3078d7',
                  width=2)
minus.pack(side='left', padx=35)
weight_value_label.pack(side='left', padx=5)
weight_label.pack(side='left')
plus.pack(side='left', padx=35)
input_window_weight.pack(pady=30)

current_value = tk.DoubleVar()
slider_m = ttk.Scale(master=window,
                     from_=120,
                     to=230,
                     length=300,
                     command=calculate_bmi,
                     variable=current_value,
                     orient='horizontal')
slider_m.pack(pady=10)
slider_m.set(175)

input_window_height = tk.Frame(master=window, background='#137a63')
value_label = ttk.Label(master=input_window_height,
                        text=get_current_value(),
                        font='Futura 30',
                        foreground='#ffffff',
                        background='#137a63')
height_label = tk.Label(master=input_window_height,
                        font='Futura 30',
                        text='cm',
                        foreground='#ffffff',
                        background='#137a63')
value_label.pack(side='left')
height_label.pack(side='left')
input_window_height.pack()

window.mainloop()
