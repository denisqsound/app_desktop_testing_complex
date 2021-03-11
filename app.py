import json
import tkinter as tk
from tkinter import messagebox

import config

with open('question.json', encoding="utf8") as f:
    data = json.load(f)

# Вычитываем все вопросы и ответы с файла
questions = [v for v in data[0].values()]
answers = [v for v in data[1].values()]
right_answers = [int(v) for v in data[2].values()]

# Текущий вопрос
current_question_index = 0

# Ответы пользователя
user_answer = []


class User:
    # def __init__(self, name):
    def __init__(self):
        # self.name = name
        self.score = 0
        self.level = 0

    def update_score(self, amount=1):
        self.score += amount

    def set_name(self, new_name):
        self.name = new_name

    def show_score(self):
        return self.score

    def update_level(self, amount):
        self.level += amount


class MainQuizApp():

    def __init__(self):
        self.questions = questions
        self.answers = answers
        self.right_answers = right_answers
        self.root = tk.Tk()
        self.user = User()
        self._build_gui()

        # Индекс вопроса и вариантов ответа
        self.current_question_index = 0

        # Это будет экран с регистрацией
        # self.top = tk.Toplevel()

        # Переменная в которой запоминается выбор пользователя
        self.user_answer = tk.IntVar()
        self.user_answer.set(228)

        self.root.mainloop()

    # Получить вопрос
    def get_question(self):
        print(
            f"CURRENT QUESTION : {self.questions[self.current_question_index]}"
        )
        return self.questions[self.current_question_index]

    # Получить варианты ответа
    def get_options(self):
        return self.answers[self.current_question_index]

    # Отрисовать кнопки с вариантами ответа
    def _make_options(self, options_list):
        for option, index in zip(options_list, range(len(options_list))):
            self.option_buttons.append(
                tk.Radiobutton(
                    self.middle_frame,
                    text=option,
                    value=index + 1,
                    variable=self.user_answer
                )
            )
            # print(f"OPTION BUTTONS: {self.option_buttons}")
            self.option_buttons[-1].grid(row=index + 1)

    def get_current_answer(self):
        # Получаем ЦИФРУ правильного ответа
        index_right_answer = self.right_answers[self.current_question_index]
        # Получаем БУКВЕННЫЙ ОТВЕТ по ЦИФРЕ
        return self.answers[self.current_question_index][index_right_answer]

    # Правильно ли пользователь ответил на вопрос?
    def is_answer_correct(self):
        print(f"USER ANSWER : {self.user_answer.get()}")
        print(
            f"СРАВНИВАЕТСЯ {self.get_current_answer()} c {self.get_options()[self.user_answer.get() - 1]}"
        )
        return self.get_current_answer() == self.get_options()[
            self.user_answer.get() - 1]

    def _update_question(self, question):
        self.questions_label.config(text=question)

    def start(self):
        print("START PROGRAMM")

        # TODO тут кнопку эту нужно удалять с экрана
        self.start_button.grid_forget()
        # self.start_button.destroy()

        # Отключаем кнопку
        # self.start_button = tk.Button(
        #     self.side_box,
        #     text="Начать тестирование",
        #     state="disable",
        #     padx=5,
        #     pady=5
        # )
        # self.start_button.grid(row=0, column=0, stick="we")

        # Включаем кнопку

        self.submit_button = tk.Button(
            self.low_frame,
            text="Ответить",
            activeforeground=config.BACKGROUND_BUTTON,
            background=config.BACKGROUND_COLOR,
            command=self.check_and_update,
            padx=5,
            pady=5
        )
        self.submit_button.grid(row=1, column=0, stick="we")

        print(self.user.score)
        # Получить список всех вопросов
        # self.questions = qm.get_questions(self.questions_file)
        print(f"QUESTIONS : {self.questions}")

        # Получить текущий вопрос
        current_question = self.get_question()
        # print(f"CURRENT QUESTION : {current_question}")

        self._update_question(current_question)

        # Получить варианты ответа
        options = self.get_options()
        print(f"OPTIONS : {options}")

        self._make_options(options)

    def _update_options(self, options_list):
        self.user_answer.set(7)
        for option_button, option, index in zip(
                self.option_buttons, options_list, range(len(options_list))
        ):
            option_button.config(text=option, value=index + 1)

    # Выдаем те же параметры если пользователь решил перещелкнуть вопрос
    # def _same_question_and_answer(self):
    #     # Отрисовываем тот же вопрос
    #     current_question = self.get_question()
    #     self._update_question(current_question)
    #
    #     # Отрисовываем теже ответы
    #     options_list = self.get_options()
    #     for option_button, option, index in zip(self.option_buttons, options_list, range(len(options_list))):
    #         option_button.config(text=option, value=index)

    # Метод для определения правильности ответа
    def _update_answer_label(self):
        status = 'Правильный ответ' if self.is_answer_correct(
        ) else 'Неправильно'
        if status == 'Правильный ответ':
            self.user.update_score()
            print(f"ПРАВИЛЬНЫХ ОТВЕТОВ :{self.user.show_score()}")
        print(status)

        # TODO добавить дозапись в файл информации об ответе

        # Здесь лежит блок для показа правильных ответов
        # status = 'correct' if self.is_answer_correct() else 'wrong'
        # if status == 'wrong':
        #     status += ' correct answer: {}'.format(self.get_current_answer())
        # self.answer_label.config(text=status)

    # Проверка и генерация нового вопроса
    def check_and_update(self):
        try:
            self._update_answer_label()
        except IndexError:
            messagebox.showerror(
                title="ОШИБКА", message="Выберите вариант ответа"
            )
            return
        self.root.after(100, self.get_next_question)

    def _update_questions_remaining(self):
        pass

    # Получение следующего вопроса
    def get_next_question(self):
        self.current_question_index += 1

        # Если вопрос последний
        if self.current_question_index == len(self.questions):
            print("Это был последний вопрос")
            print(self.user.show_score())
            count_right_answer = len(self.right_answers)
            text = f"ВАШ РЕЗУЛЬТАТ : \n {self.user.show_score()} правильных ответов из {count_right_answer} вопросов "
            # self.questions_label.config(text=text)
            messagebox.showinfo(title="ВАШ РЕЗУЛЬТАТ", message=text)
            self.root.destroy()

        else:
            self._update_questions_remaining()
            self._update_question(self.get_question())
            self._update_options(self.get_options())

    def _build_gui(self):
        # ROW - по горизонтали (Строки)
        # COLUMN - по вертикали (Колонки)

        self.root.geometry(config.GEOMETRY)
        self.root.config(bg=config.BACKGROUND_COLOR)

        # Ширина колонки
        self.root.grid_columnconfigure(0, minsize=590)
        self.root.title("Экзаменационная программа")
        self.user_answer = tk.IntVar()

        # '''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''#
        ################################################ ФРЕЙМЫ ###############################################
        # '''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''#

        # ROW - по горизонтали (Строки)
        # COLUMN - по вертикали (Колонки)


        self.ultra_head_frame = tk.Frame(self.root, padx=5, pady=5)
        self.ultra_head_frame.grid(row=0, column=0)

        self.head_frame = tk.Frame(self.root, padx=5, pady=5)
        self.head_frame.grid(row=1, column=0)

        self.middle_frame = tk.Frame(self.root, padx=5, pady=5)
        self.middle_frame.grid(row=2, column=0)
        self.middle_frame.grid_rowconfigure(1, minsize=100)

        self.low_frame = tk.Frame(self.root, padx=5, pady=5)
        self.low_frame.grid(row=3, column=0)



        # ''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''#
        ################################################ ЛЕЙБЛЫ ################################################ 
        # ''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''#

        # self.root_label = tk.Label(self.root, text='ROOT').grid(row=0, column=0, columnspan=2, stick="we")
        # self.root_label = tk.Label(self.root, text='ROOT').grid(row=0, column=0, stick="we")


        text = 'qweqweqwe \n qweqweqwe \n qweqweqw \n qweqweqwe \n qweqweqw \n qweqweqwe \n qweqweqw \n qweqweqwe \n qweqweqw'
        self.test_label = tk.Label(self.ultra_head_frame, text='ULTRA HEAD', padx=5, pady=5)
        self.test_label.grid()

        self.test_label = tk.Label(self.head_frame, text='HEAD', padx=5, pady=5)
        self.test_label.grid()

        # self.questions_label = tk.Label(self.middle_frame, text=text, padx=5, pady=5)
        # self.questions_label.grid()


        self.low_frame = tk.Label(self.low_frame, text='SIDE BOX', padx=0, pady=0)
        self.empty_low_frame = tk.Label(self.low_frame, text='EMPTY_SIDE BOX', padx=0, pady=0)
        self.low_frame.grid()


        # ROW - по горизонтали (Строки)
        # COLUMN - по вертикали (Колонки)


        # ''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''#
        ################################################ КНОПКИ ################################################
        # ''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''#

        # Список кнопок с вариантами ответа
        self.option_buttons = []

        def udoli():
            self.empty_low_frame.grid()


        # Кнопка старт
        # self.root.grid_rowconfigure(4, minsize=200)
        self.test_button = tk.Button(
            self.middle_frame,
            text="А НУ КА",
            command=udoli,
            activeforeground=config.BACKGROUND_BUTTON,
            background=config.BACKGROUND_COLOR,
            padx=5,
            pady=5
        )
        self.test_button.grid(row=1, column=0, stick="ns")

        # Кнопка ответ
        # self.submit_button = tk.Button(
        #     self.side_box,
        #     text="Ответить",
        #     activeforeground=config.BACKGROUND_BUTTON,
        #     background=config.BACKGROUND_COLOR,
        #     command=self.check_and_update,
        #     state="disable",
        #     padx=5,
        #     pady=5
        # )
        # self.submit_button.grid(row=1, column=0, stick="we")

        # Кнопка следующий
        # self.next_button = tk.Button(self.questions_box, text="Next", padx=5, pady=5)
        # self.next_button.grid(row=3, column=0, columnspan=2, stick="we")


if __name__ == '__main__':
    MainQuizApp()
