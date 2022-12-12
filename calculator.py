from tkinter import *
from tkinter import ttk


class PurchaseAndPreparation(ttk.Frame):
    """Калькулятор прибыли реализации товара"""
    def __init__(self, master):
        super().__init__(master)
        self.master = master
        self.grid()
        self.create_widgets()

    def create_widgets(self):
        self.button1 = Button(self, text='первая')
        self.button1.grid(column=1, row=1)
        self.button2 = Button(self, text='вторая')
        self.button2.grid(column=2, row=2)
        self.button3 = Button(self, text='третья')
        self.button3.grid(column=0, row=3)
        self.button4 = Button(self, text='четвертая')
        self.button4.grid(column=3, row=4)



if __name__ == '__main__':
    window = Tk()
    window.title('Калькулятор прибыли')
    window.geometry('1024x768')

    menu = Menu(window)
    menu_item = Menu(menu, tearoff=0)
    menu_item.add_command(label='Загрузить')
    menu_item.add_command(label='Сохранить')
    menu_item.add_separator()
    menu_item.add_command(label='Выход')
    menu.add_cascade(label='Главное', menu=menu_item)
    window.config(menu=menu)

    tab_control = ttk.Notebook(window)
    pur_and_prep = PurchaseAndPreparation(tab_control)
    tab_control.add(pur_and_prep, text='Закупка и хранение')
    pur_and_prep.columnconfigure(index=0, weight=2)
    pur_and_prep.columnconfigure(index=1, weight=3)
    pur_and_prep.columnconfigure(index=2, weight=3)
    pur_and_prep.columnconfigure(index=3, weight=2)

    tab_control.pack(expand=1, fill='both')
    window.mainloop()
