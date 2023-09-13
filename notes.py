from tkinter import *
from tkinter import messagebox
from tkinter.filedialog import askopenfile
import os, os.path


def notes(folder_name):
    file_name = NONE

    def new_file():
        text.delete('1.0', END)

    def save():
        global txt, entered_text, lbl, btn
        entered_text = text.get('1.0', END)
        text.pack_forget()
        lbl = Label(root, text='Как вы хотите назвать сохраняемый файл?')
        lbl.grid(column=0, row=0)
        txt = Entry(root, width=15)
        txt.grid(column=1, row=0)
        txt.focus()
        btn = Button(root, text="ОК!", command=save_file)
        btn.grid(column=2, row=2)

    def save_file():
        named_file = txt.get()
        folder = folder_name
        expans = 'txt'
        try:
            save = open(os.path.join(folder, named_file + '.' + expans), 'a')
            save.write("{}".format(entered_text))
            messagebox.showinfo('Информация', 'Файл успешно сохранен')
        except:
            messagebox.showerror("Ошибка!", "Не удалось сохранить файл!")
        root.destroy()

    def open_file():
        global file_name
        inp = askopenfile(mode='r')
        if inp is None:
            return
            file_name = inp.name
        data = inp.read()
        text.delete('1.0', END)
        text.insert('1.0', data)

    root = Tk()
    root.title("Заметки")
    root.geometry("500x500")

    text = Text(root, width=500, height=500)
    text.focus()
    text.pack()

    menu_bar = Menu(root)
    file_menu = Menu(menu_bar)

    file_menu.add_command(label="Новый файл", command=new_file)
    file_menu.add_command(label="Открыть", command=open_file)
    file_menu.add_command(label="Coxpaнить", command=save)
    menu_bar.add_cascade(label="Файл", menu=file_menu)

    root.config(menu=menu_bar)
    root.mainloop()
