from tkinter import *
from tkinter import messagebox
import json
import os
from notes import notes


def registration_successfully_completed():
    btn.destroy()
    global folder_name
    lbl = Label(root, text='Приветствуем вас {}, авторизация успешно пройдена!!'.format(txt.get()))
    lbl.grid(column=0, row=0)
    folder_name = txt.get()
    txt.delete('0', END)
    txt.destroy()
    try:
        os.mkdir(f'{folder_name}')
        label = Label(root, text='Под вашим никнеймом предыдущих заметок не обнаружено')
        label.grid(column=0, row=2)
        button = Button(root, text="Создать новую заметку!", command=go_in_notes)
        button.grid(column=0, row=3)
    except:
        found_old_files(folder_name)


def go_in_notes():
    notes(folder_name)


def found_old_files(entered_text):
    otvet = []
    row = 1
    try:
        for filename in os.listdir(f'{entered_text}'):
            with open(os.path.join(f'{entered_text}', filename), 'r') as file:
                text = file.read()
                found_files = (filename, 'с текстом:', text)
                otvet.append(found_files)
        label = Label(root, text='Под вашим никнеймом обнаружены следующие файлы:')
        label.grid(column=0, row=1)
        for i in range(len(otvet)):
            row += 1
            label = Label(root, text=f'{otvet[i][0]}' + ':' + ' ' + f'{otvet[i][2]}')
            label.grid(column=0, row=row)
        button = Button(root, text="Создать новую заметку!", command=go_in_notes)
        button.grid(column=0, row=row + 1)
    except:
        return False


def user_registration():
    data = json.dumps(txt.get(), ensure_ascii=False)
    data = json.loads(str(data))

    with open('data.json', 'r') as filik:
        dict_data = json.load(filik)
        dict_data[f'{txt.get()}'] = ['авторизация успешно пройдена']

    with open('data.json', 'w') as file:
        json.dump(dict_data, file, ensure_ascii=False, indent=3)
    registration_successfully_completed()


def check_for_saved_users():
    with open('data.json', 'r') as file:
        a = file.read()
        a = json.loads(a)
        check = 0
        for element in a:
            if element == txt.get():
                registration_successfully_completed()
                break
            if element != txt.get():
                check += 1
                if check == len(a):
                    user_registration()


root = Tk()
root.title('Авторизация в заметки')
root.geometry('450x450')

menu_bar = Menu(root)
file_menu = Menu(menu_bar)

messagebox.showinfo('Информация',
                    'Привет, вам нужно будет ввести ваш персональный никнейм, это нужно для предоставления именно ваших заметок!')
lbl = Label(root, text='Введите свой никнейм!')
lbl.grid(column=0, row=0)
txt = Entry(root, width=15)
txt.grid(column=1, row=0)
txt.focus()
btn = Button(root, text="ОК!", command=check_for_saved_users)
btn.grid(column=2, row=2)

root.config(menu=menu_bar)
root.mainloop()
