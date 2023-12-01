import random
import sqlite3

import tkinter as tk
from tkinter import *
from tkinter import messagebox


def AddStudent(name, surname, group, form_of_ed):
    if (name.get() != 'Имя' and surname.get() != 'Фамилия' and group.get() != 'Номер группы' and form_of_ed != 'Форма обучения'and form_of_ed != ''):
        try:
            if((not name.get().isalpha()) or (not surname.get().isalpha()) or (not group.get().isdigit()) or (len(group.get()) != 6)
            or name.get()[0].islower() or surname.get()[0].islower()):
                raise ValueError
            connection = sqlite3.connect('students.db')
            cursor = connection.cursor()
            cursor.execute('INSERT INTO Students (name, surname, group_numb, form) VALUES (?, ?, ?, ?)', (name.get(),
                       surname.get(), group.get(), form_of_ed))
            connection.commit()
            connection.close()
            name.delete(0, 'end')
            surname.delete(0, 'end')
            group.delete(0, 'end')
            tk.messagebox.showinfo("Уведомление","Студент успешно добавлен в базу данных")
        except ValueError:
            tk.messagebox.showerror("Ошибка!", "Проверьте корректность ввода данных")
        except sqlite3.IntegrityError:
            tk.messagebox.showerror("Ошибка!", "Проверьте корректность ввода данных")
    else:
        tk.messagebox.showerror("Ошибка!"," Необходимо ввести данные студента!")


def GenerateGroupLeader(menu_item):
    try:
        group = menu_item['text']
        connection = sqlite3.connect('students.db')
        cursor = connection.cursor()
        cursor.execute('''SELECT name, surname FROM Students WHERE group_numb = ? AND form = ?''', (group, 'Бюджетная'))
        full_names = cursor.fetchall()
        full_name = random.choice(full_names)
        name_mass = str(full_name).split("'")
        connection.close()
        tk.messagebox.showinfo("Результат генерации", "Старостой группы " + group + " будет следующий студент: "
                           + str(name_mass[1]) + " " + str(name_mass[3]))
    except IndexError:
        tk.messagebox.showerror("Ошибка!", "Выберите номер группы!")


def set_menu_text(menu, text):
    menu['text'] = text


class MyApp(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self._frame = None
        self.go_to_new_frame(MainPage)

    def go_to_new_frame(self, frame_to_go):
        new_frame = frame_to_go(self)
        if self._frame is not None:
            self._frame.destroy()
        self._frame = new_frame
        self._frame.pack(padx = 100, pady = 150)


class MainPage(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        tk.Frame.config(self, bg='white')
        tk.Frame.config(master, bg='white')
        tk.Button(self, text="Добавить потенциального старосту группы", font=("Bodoni MT Black", 15), fg='white', bg='blue',
                      command=lambda: master.go_to_new_frame(EditWindow)).pack(padx=0, pady=50)
        tk.Button(self, text="Выбрать старосту", font=("Bodoni MT Black", 15), fg='white',
                  bg='blue', command=lambda: GenerateGroupLeader(menu_btn)).pack(padx=100, pady=0)
        menu_btn = tk.Menubutton(self, text='Номер группы')
        menu = Menu(menu_btn)
        connection = sqlite3.connect('students.db')
        cursor = connection.cursor()
        cursor.execute('''
        SELECT group_numb FROM Students
        ''')
        groups_numb = cursor.fetchall()
        connection.close()
        group_numbers = []
        for group in groups_numb:
            flag = False
            for entered_groups in group_numbers:
                if group == entered_groups:
                    flag = True
                    break
            if(flag == False):
                group_numbers.append(group)
                menu.add_cascade(label=group, command=lambda group=group: set_menu_text(menu_btn, group))
        menu_btn['menu'] = menu
        menu_btn.pack()


class EditWindow(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        tk.Frame.config(self, bg='white')
        tk.Frame.config(master, bg='white')
        name = tk.Entry(self, fg='grey', width=50)
        name.insert(0, 'Имя')
        name.pack()
        surname = tk.Entry(self, fg='grey', width=50)
        surname.insert(0, 'Фамилия')
        surname.pack()
        group = tk.Entry(self, fg='grey', width=50)
        group.insert(0, 'Номер группы')
        group.pack()
        form_of_ed = tk.Menubutton(self, text='Форма обучения')
        menu = Menu(form_of_ed)
        menu.add_command(label='Платная', command= lambda: set_menu_text(form_of_ed, 'Платная'))
        menu.add_command(label='Бюджетная', command= lambda: set_menu_text(form_of_ed, 'Бюджетная'))
        form_of_ed['menu'] = menu
        form_of_ed.pack()
        tk.Button(self, text="Добавить студента", font=("Bodoni MT Black", 15), fg='white', bg='blue',
                  command=lambda: AddStudent(name, surname, group, form_of_ed['text'])
                  ).pack(padx=0, pady=0)
        tk.Button(self, text="Вернуться на страницу генерации старосты", font=("Bodoni MT Black", 15), fg='white', bg='blue',
                  command=lambda: master.go_to_new_frame(MainPage)).pack(padx=0, pady=50)


my_app = MyApp()
my_app.mainloop()
