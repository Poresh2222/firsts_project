from tkinter import *  # Импорт самого модуля, в котором ведётся вся работа
from tkinter import messagebox
import pickle  # Для возможности сохранять сохранять в txt

class Window:  # Родительское, стартовое окно
    def __init__(self, width, height, title="Car Rent Program", resizeble=(False, False), icon=r"Images/IMG_2520.ico"):
        self.root = Tk()  # Присвоения "Корня" к окну, с верху параматры которые будут переданы всем дочерним окнам, с низу параметры окна
        self.root.title(title)
        self.root.geometry(f"{width}x{height}")
        self.root.resizable(resizeble[0], resizeble[1])
        self.root.iconbitmap(icon)

    def run(self):  # Функция запуска
        self.root.mainloop()  # Команда запуска

    def draw_labels(self):  # Функция отрисовки всего в окне, запускается из main
        self.logo_image = PhotoImage(file=r"Images/IMG_1010.png")  #
        self.label = Label(self.root, image=self.logo_image)
        self.label.place(relx=0, rely=0)
        Label(self.root, text="The Best rent company", font="Consolas 30", bg="#db1f12").place(relx=0.12, rely=0.3)
        Button(self.root, width=30, height=5, text="Our's car's", relief=GROOVE, bd=8, bg="#db1f12",
                   activebackground="#000000", command=self.our_window).place(relx=0.07, rely=0.4)
        Button(self.root, width=30, height=5, text="Rent Places", relief=GROOVE, bd=8, bg="#db1f12",
                   activebackground="#000000", command=self.ren_window).place(relx=0.55, rely=0.4)
        Button(self.root, width=30, height=5, text="Rent Now", relief=GROOVE, bd=8, bg="#db1f12",
                   activebackground="#000000", command=self.cre_window).place(relx=0.07, rely=0.6)
        Button(self.root, width=30, height=5, text="Registration/Enter", relief=GROOVE, bd=8, bg="#db1f12",
                   activebackground="#000000", command=self.reg_window).place(relx=0.55, rely=0.6)
        Button(self.root, width=30, height=5, text="Quit", relief=GROOVE, bd=8, bg="#db1f12",
                   activebackground="#000000", command=self.root.destroy).place(relx=0.3, rely=0.8)

    def our_window(self):  # До конца блока - функции открытия других окон
        WindowOur(self.root, 1000, 1000).run()

    def ren_window(self):
        WindowRen(self.root, 500, 500).run()

    def reg_window(self):
        WindowReg(self.root, 500, 800).run()

    def cre_window(self):
        WindowCreate(self.root, 1000, 700).run()


class WindowOur(Window):  # Первое дочернее окно, со всеми переданными командами
    def __init__(self, parent, width, height, title="Our's car's", resizeble=(False, False), icon=r"Images/IMG_2520.ico"):
        self.root = Toplevel(parent)  # Что бы не отрисовывалось в этом окне
        self.root.title(title)
        self.root.geometry(f"{width}x{height}")
        self.root.resizable(resizeble[0], resizeble[1])
        self.root.iconbitmap(icon)
    # Крепление фоток
        Label(self.root, text="Our's car's", font="Consolas 30", bg="#db1f12").place(relx=0.375, rely=0)
        self.auto1_image = PhotoImage(file=r"Images/IMG_1002.png")
        self.auto2_image = PhotoImage(file=r"Images/IMG_1001.png")
        self.auto3_image = PhotoImage(file=r"Images/IMG_1003.png")
        self.auto4_image = PhotoImage(file=r"Images/IMG_1004.png")
        Label(self.root, image=self.auto1_image).place(relx=0, rely=0.1)
        Label(self.root, image=self.auto2_image).place(relx=0.5, rely=0.1)
        Label(self.root, image=self.auto3_image).place(relx=0, rely=0.5)
        Label(self.root, image=self.auto4_image).place(relx=0.5, rely=0.5)
        Button(self.root, width=30, height=5, text="Quit", relief=GROOVE, bd=8, bg="#db1f12",
               activebackground="#000000", command=self.root.destroy).place(relx=0.375, rely=0.9)


class WindowRen(Window):  # Дочернее окошко, самое простое )
    def __init__(self, parent, width, height, title="Rent Places", resizeble=(False, False), icon=r"Images/IMG_2520.ico"):
        self.root = Toplevel(parent)
        self.root.title(title)
        self.root.geometry(f"{width}x{height}")
        self.root.resizable(resizeble[0], resizeble[1])
        self.root.iconbitmap(icon)
    #
        Label(self.root, text="Wroclaw:", font="Consolas 30", bg="#db1f12").place(relx=0, rely=0)
        Label(self.root, text="Sliczna 26 - +48000000000", font="Consolas 15").place(relx=0, rely=0.1)
        Label(self.root, text="Klimasa 33 - +48000000000", font="Consolas 15").place(relx=0, rely=0.15)
        Label(self.root, text="Warsaw:", font="Consolas 30", bg="#db1f12").place(relx=0, rely=0.2)
        Label(self.root, text="Sliczna 26 - +48000000000", font="Consolas 15").place(relx=0, rely=0.3)
        Label(self.root, text="Klimasa 33 - +48000000000", font="Consolas 15").place(relx=0, rely=0.35)
        Label(self.root, text="Lodz:", font="Consolas 30", bg="#db1f12").place(relx=0, rely=0.4)
        Label(self.root, text="Sliczna 26 - +48000000000", font="Consolas 15").place(relx=0, rely=0.5)
        Label(self.root, text="Klimasa 33 - +48000000000", font="Consolas 15").place(relx=0, rely=0.55)
        Button(self.root, width=30, height=5, text="Back", relief=GROOVE, bd=8, bg="#db1f12",
               activebackground="#000000", command=self.root.destroy).place(relx=0.27, rely=0.8)


class WindowReg(Window):  # Окно регистрации, тут все наложено без прикрепления функцией
    def __init__(self, parent, width, height, title="Registration/Enter", resizeble=(False, False), icon=r"Images/IMG_2520.ico"):
        self.root = Toplevel(parent)
        self.root.title(title)
        self.root.geometry(f"{width}x{height}")
        self.root.resizable(resizeble[0], resizeble[1])
        self.root.iconbitmap(icon)
        self.registration_log = Entry(self.root, width=30, )
        self.registration_log.place(relx=0.3, rely=0.125)
        self.registration_pass = Entry(self.root, width=30, show="*")
        self.registration_pass.place(relx=0.3, rely=0.2)
        self.registration_pass1 = Entry(self.root, width=30, show="*")
        self.registration_pass1.place(relx=0.3, rely=0.275)
    # Без функции
        Label(self.root, text="Registration/Enter", font="Consolas 30", bg="#db1f12").place(relx=0.1, rely=0)
        Label(self.root, text="Enter login", font="Consolas 20").place(relx=0.315, rely=0.075)
        Label(self.root, text="Enter password", font="Consolas 20").place(relx=0.27, rely=0.15)
        Label(self.root, text="Repeat password", font="Consolas 20").place(relx=0.25, rely=0.225)
        Button(self.root, width=13, height=1, text="I'm have acc", relief=GROOVE, bd=8, bg="#db1f12",
               activebackground="#000000", command=self.login).place(relx=0.38, rely=0.375)
        Button(self.root, width=13, height=1, text="Create", relief=GROOVE, bd=8, bg="#db1f12",
               activebackground="#000000", command=self.save).place(relx=0.38, rely=0.325)
        Button(self.root, width=20, height=2, text="Back", relief=GROOVE, bd=8, bg="#db1f12",
               activebackground="#000000", command=self.root.destroy).place(relx=0.325, rely=0.9)

    def save(self):  # Создание пустого словаря, вкладывание в него из Entry, 1) сохранение, закрытие
        login_pass_save = {}
        login_pass_save[self.registration_log.get()] = self.registration_pass.get()
        login_txt = open("login.txt", "wb")
        pickle.dump(login_pass_save, login_txt)
        login_txt.close()
        self.login()

    def login(self):  # Открывающаяся часть экрана для "Входа"
        Label(self.root, text="Enter in acc", font="Consolas 20").place(relx=0.285, rely=0.425)
        Label(self.root, text="Enter login", font="Consolas 20").place(relx=0.3, rely=0.475)
        self.enter_login = Entry(self.root, width=30, )
        self.enter_login.place(relx=0.3, rely=0.525)
        Label(self.root, text="Enter password", font="Consolas 20").place(relx=0.25, rely=0.55)
        self.enter_pass = Entry(self.root, width=30, show="*")
        self.enter_pass.place(relx=0.3, rely=0.6)
        Button(self.root, width=13, height=1, text="Enter", relief=GROOVE, bd=8, bg="#db1f12",
               activebackground="#000000", command=self.log_pass).place(relx=0.38, rely=0.65)

    def log_pass(self):  # Функция проверки правильности входа
        login_txt = open("login.txt", "rb")
        login_load = pickle.load(login_txt)
        login_txt.close()
        if self.enter_login.get() in login_load:
            if self.enter_pass.get() == login_load[self.enter_login.get()]:
                messagebox.showinfo("Enter in system", "Correct pass and login")
            else:
                messagebox.showerror("Error", "Try again")
        else:
            messagebox.showerror("Error", "Try again")


class WindowCreate(Window):  # Самое тяжелое окно
    def __init__(self, parent, width, height, title="Rent now", resizeble=(False, False), icon=r"Images/IMG_2520.ico"):
        self.root = Toplevel(parent)
        self.root.title(title)
        self.root.geometry(f"{width}x{height}")
        self.root.resizable(resizeble[0], resizeble[1])
        self.root.iconbitmap(icon)
        self.enter_login = Entry(self.root, width=30, )
        self.enter_login.place(relx=0.05, rely=0.2)
        self.enter_pass = Entry(self.root, width=30, show="*")
        self.enter_pass.place(relx=0.05, rely=0.3)
        self.choise = IntVar(value=0)
        self.choise1 = IntVar(value=0)
        self.choise2 = IntVar(value=0)

        Label(self.root, text="Rent menu", font="Consolas 40", bg="#db1f12").place(relx=0.375, rely=0)
        Label(self.root, text="Login", font="Consolas 20").place(relx=0.1, rely=0.125)
        Label(self.root, text="Password", font="Consolas 20").place(relx=0.0755, rely=0.24)
        Label(self.root, text="If you want rent a car\nYou need enter in acc",
              font="Consolas 10").place(relx=0.06, rely=0.02)
        Button(self.root, width=10, height=1, text="Enter", relief=GROOVE, bd=8, bg="#db1f12",
               activebackground="#000000", command=self.log_pass).place(relx=0.09, rely=0.375)
        Button(self.root, width=10, height=1, text="Our's car's", relief=GROOVE, bd=8, bg="#db1f12",
               activebackground="#000000", command=self.our_window).place(relx=0.09, rely=0.45)
        Button(self.root, width=15, height=2, text="Back", relief=GROOVE, bd=8, bg="#db1f12",
               activebackground="#000000", command=self.root.destroy).place(relx=0.075, rely=0.875)

    def our_window(self):  # Возможность открытия 2-го окна отсюда
        WindowOur(self.root, 1000, 1000).run()

    def log_pass(self):  # Проверка логина и пароля из того же txt
        login_txt = open("login.txt", "rb")
        login_load = pickle.load(login_txt)
        login_txt.close()
        if self.enter_login.get() in login_load:
            if self.enter_pass.get() == login_load[self.enter_login.get()]:
                self.draw_labels1()
                messagebox.showinfo("Enter in system", "Correct pass and login")
            else:
                messagebox.showerror("Error", "Try again")
        else:
            messagebox.showerror("Error", "Try again")

    def draw_labels1(self):  # Отрисовка вариантов
        Label(self.root, text="Choose option:", font="Consolas 30").place(relx=0.5, rely=0.125)
        Label(self.root, text="1. Select car:", font="Consolas 15").place(relx=0.3, rely=0.2)
        Radiobutton(self.root, text="Ford Mustang", font="Consolas 10", variable=self.choise,
                    value=0).place(relx=0.3, rely=0.25)
        Radiobutton(self.root, text="Dodge Charger", font="Consolas 10", variable=self.choise,
                    value=1).place(relx=0.3, rely=0.28)
        Label(self.root, text="2. Select town:", font="Consolas 15").place(relx=0.3, rely=0.35)
        Radiobutton(self.root, text="Warsaw", font="Consolas 10", variable=self.choise1,
                    value=0).place(relx=0.3, rely=0.4)
        Radiobutton(self.root, text="Wroclaw", font="Consolas 10", variable=self.choise1,
                    value=1).place(relx=0.3, rely=0.43)
        Radiobutton(self.root, text="Lodz", font="Consolas 10", variable=self.choise1,
                    value=2).place(relx=0.3, rely=0.46)
        Label(self.root, text="3. Time:", font="Consolas 15").place(relx=0.3, rely=0.53)
        Radiobutton(self.root, text="24h", font="Consolas 10", variable=self.choise2,
                    value=0).place(relx=0.3, rely=0.58)
        Radiobutton(self.root, text="48h", font="Consolas 10", variable=self.choise2,
                    value=1).place(relx=0.3, rely=0.61)
        Radiobutton(self.root, text="Weekend", font="Consolas 10", variable=self.choise2,
                    value=2).place(relx=0.3, rely=0.64)
        Radiobutton(self.root, text="Mouth", font="Consolas 10", variable=self.choise2,
                    value=3).place(relx=0.3, rely=0.67)
        Button(self.root, width=10, height=1, text="Calculation", relief=GROOVE, bd=8, bg="#db1f12",
               activebackground="#000000", command=self.calculation).place(relx=0.09, rely=0.525)
        Button(self.root, width=10, height=1, text="Calculation", relief=GROOVE, bd=8, bg="#db1f12",
               activebackground="#000000", command=self.draw_labels2).place(relx=0.09, rely=0.525)

    def draw_labels2(self):  # Отрисовка Результата
        Label(self.root, text=('Prise is: {}    ').format(self.calculation()), font="Consolas 15").place(relx=0.6, rely=0.67)

    def calculation(self):  # Подсчёт зависяйщий от выбранных параметров
        choise = self.choise.get()
        choise1 = self.choise1.get()
        choise2 = self.choise2.get()
        if choise == 0:
            car = 100
        else:
            car = 200
        if choise1 == 0:
            town = 1.5
        elif choise1 == 1:
            town = 1.25
        else:
            town = 1
        if choise2 == 0:
            time = 1
        elif choise2 == 1:
            time = 2
        elif choise2 == 2:
            time = 2.5
        else:
            time = 20
        res = car * town * time
        return res
