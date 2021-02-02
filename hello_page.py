import os
import tkinter as tk
from tkinter import messagebox

win = tk.Tk()


def hello_page():
    win.title('Экзаменационная программа')
    win.geometry("400x770")
    win.config(bg='#99CCFF')
    tk.Label(win, text='Вас приветсвует экзаменационная программа для мамы!').grid(row=0, column=0, columnspan=2,
                                                                                   stick="we")

    # Заполняем поле Фамилия
    tk.Label(win, text='Фамилия').grid(row=1, column=0, stick="we")
    second_name_entry = tk.Entry(win)
    second_name_entry.grid(row=2, column=1, stick="we")

    # Заполняем поле Имя
    tk.Label(win, text='Имя').grid(row=2, column=0, stick="we")
    first_name_entry = tk.Entry(win)
    first_name_entry.grid(row=1, column=1, stick="we")

    def register_user():
        first_name = first_name_entry.get()
        second_name = second_name_entry.get()
        if len(first_name) > 0 and len(second_name) > 0:
            directory = 'students/'
            filename = f"{first_name}_{second_name}"
            file_path = os.path.join(directory, filename)
            file = open(file_path, "w")
            file.write(first_name + "\n")
            file.write(second_name + "\n")
            file.close()
        else:
            messagebox.showerror("ОШИБКА!", "Введите Фамилию и Имя!")

    # Кнопка для начала опроса
    # По нажатию кнопки сохраняем информацию о текущем пользователе и создаем файл
    tk.Button(win,
              text="Старт",
              command=register_user).grid(
        row=3,
        column=0,
        columnspan=2)

    win.grid_rowconfigure(0, minsize=200)
    win.grid_rowconfigure(3, minsize=200)


hello_page()
win.mainloop()
