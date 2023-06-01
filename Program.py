import sqlite3
import tkinter as tk
from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox
from tkinter import ttk
import datetime
class Login:
    def __init__(self):
        self.window = tk.Tk()
        self.logowanie()
        self.show_login()


    def logowanie(self):
        description = tk.Label(self.window, text="Uzupełnij dane logowania").grid(row=0, column=3)
        self.usernameLabel = tk.Label(self.window, text="User Name").grid(row=2, column=1)
        self.username = StringVar()
        self.usernameEntry= tk.Entry(self.window, textvariable=self.username).grid(row=2, column=3)

        self.passwordLabel = tk.Label(self.window, text="Password").grid(row=3, column=1)
        self.password = StringVar()
        self.passwordEntry = Entry(self.window, textvariable=self.password, show='*').grid(row=3, column=3)

        self.loginButton = tk.Button(self.window, text="Zaloguj", command=lambda:[self.validateLogin(),]).grid(row=4, column=3)
        self.exitbutton = tk.Button(self.window, text="Zakończ program", command=lambda: [self.window.destroy() ]).grid(row=5,
                                                                                                                 column=3)

        self.show_login()

    def validateLogin(self):

        if self.username.get() == "admin" and self.password.get() == "admin":
            self.window.destroy()
            win = Window()

        else:
            win = Errors().error_login()



    def show_login(self):
        self.window.title("Logowanie do bazy danych")
        self.window.geometry('250x150')
        self.window.mainloop()


class Window:


    def __init__(self):
        self.window = tk.Tk()
        self.label()
        self.menu()

    def label(self):
        description = tk.Label(self.window, text= "MENU GŁÓWNE", padx=150, pady=20).pack()
        self.ok = tk.Button(self.window, text="Dodaj przesyłke",command=lambda:[self.window.destroy(),Dodaj_przesylke()], width=30,).pack()
        self.ok2 = tk.Button(self.window, text="Wyszukaj przesyłke",command=lambda:[self.window.destroy(),search()],width=30,).pack()
        self.ok3 = tk.Button(self.window, text="Dodaj Pracownika", width=30, command=lambda:[self.window.destroy(),dodaj_pracownika() ]).pack()
        self.ok4 =tk.Button(self.window, text='Wyszukaj Pracownika', width=30, command=lambda:[self.window.destroy(),wyszukaj_pracownika()]).pack()
        self.ok4 = tk.Button(self.window, text="Wersja \n Informacje dodatkowe", width=30,command=lambda: [self.window.destroy(), InfoUpdate()]).pack()
        self.ok5 = tk.Button(self.window, text="Wyloguj", width=30,command=lambda:[self.window.destroy(),Login()] ).pack()
        self.ok6 = tk.Button(self.window, text="Zakończ program",command=lambda:self.quit(), width=30,).pack()


    def menu(self):
        self.show()

    def show(self):
        self.window.title('Baza danych przesyłek kurierskich')
        self.window.geometry('300x300')
        self.window.mainloop()

    def quit(self):
        self.msgBox = tk.messagebox.askquestion('Zakończ program', 'Czy chcesz zakończyć program?', icon='warning' )
        if self.msgBox == 'yes':
            self.window.destroy()

        else:
            tk.messagebox.showinfo('Powrot', 'Wracasz do aplikacji')



class Dodaj_przesylke:
    def __init__(self):
        self.window = tk.Tk()
        self.dodaj()
        self.variable = tk.StringVar()
        self.show()

        #warianty

    def refresh(self):
        self.IDENTYFIKATORY_LIST = []
        conn = sqlite3.connect('data.sqlite')
        cur = conn.cursor()
        self.n = cur.execute("SELECT nr_id,nazwisko FROM pracownicy WHERE stanowisko='Kurier'")
        rows = cur.fetchall()
        for row in rows:
            self.IDENTYFIKATORY_LIST.append(row)


    def dodaj(self):
        self.refresh()
        self.label = tk.Label(self.window, text="Uzuepłnij dane aby dodać przesyłke", padx=150, pady=20)
        self.label.pack()

        description = tk.Label(self.window, text="Nr przesyłki").pack()
        self.nr_przesylki = tk.StringVar()
        self.nr_przesylki = tk.Entry(self.window, width=10, )
        self.nr_przesylki.pack()

        description = tk.Label(self.window, text='Gabaryt').pack()
        GABARYTY = [
            "A",
            "B",
            "C",
            "Niestandardowy"
        ]

        self.gabaryt_choose = StringVar(self.window)
        self.gabaryt_choose.set(GABARYTY[0])
        w = ttk.Combobox(self.window, values=GABARYTY).pack()

        self.description = tk.Label(self.window, text="imie odbiorcy").pack()
        self.name = tk.Entry(self.window, width=40, )
        self.name.pack()

        self.description = tk.Label(self.window, text="nazwisko odbiorcy").pack()
        self.surname = tk.Entry(self.window, width=40, )
        self.surname.pack()

        self.description = tk.Label(self.window, text="miasto").pack()
        self.miasto = tk.Entry(self.window, width=40, )
        self.miasto.pack()

        self.description = tk.Label(self.window, text="ulica").pack()
        self.adres = tk.Entry(self.window, width=40, )
        self.adres.pack()

        self.description = tk.Label(self.window, text="numer domu").pack()
        self.nr_dom = tk.Entry(self.window, width=40)
        self.nr_dom.pack()

        self.description = tk.Label(self.window, text="numer mieszkania").pack()
        self.nr_miesz = tk.Entry(self.window, width=40)
        self.nr_miesz.pack()

        self.description = tk.Label(self.window, text="kod_pocztowy").pack()
        self.kod_pocztowy = tk.Entry(self.window, width=20, )
        self.kod_pocztowy.pack()

        description = tk.Label(self.window, text="Informacje dodatkowe").pack()
        self.other = tk.Entry(self.window, width=80, )
        self.other.pack()
        description = tk.Label(self.window, text='Status przesyłki').pack()
        OPTIONS = [
            "Doręczona",
            "Odmowa przyjęcia",
            "Niedoręczona",
            "W trakcie doręczenia"
        ]
        self.status_przesylki_choose = StringVar(self.window)
        self.status_przesylki_choose.set(OPTIONS[0])
        w = ttk.Combobox(self.window, values=OPTIONS).pack()

        description = tk.Label(self.window, text='Kurier przypisany do paczki').pack()

        self.nr_id_kuriera_choose = StringVar(self.window)
        self.nr_id_kuriera_choose.set(self.IDENTYFIKATORY_LIST[0])
        w = ttk.Combobox(self.window, values=self.IDENTYFIKATORY_LIST).pack()

        self.dodaj = tk.Button(self.window, text="Dodaj przesyłke", width=20, command=lambda: self.dodaj_msg()).pack()
        self.wróc = tk.Button(self.window, text="Wróć do menu", width=20, command=lambda: [self.window.destroy(), Window()]).pack()



    def dodaj_msg(self):
        self.msgBox = tk.messagebox.askquestion('Uwaga!','Czy na pewno chcesz dodać przesyłke?', icon='warning')
        if self.msgBox == 'yes':
            self.savedata()

        else:
            tk.messagebox.showinfo('Uwaga','Przesyłka nie została zapisana')

        self.show()
    def savedata(self):
        rows = [self.nr_przesylki.get(), self.name.get(), self.surname.get(), self.miasto.get(),
                         self.adres.get(), self.nr_dom.get(),
                          self.kod_pocztowy.get(),
                         ]

        for row in rows:
            if row == "":
                Errors().error_add()
                break

            else:
                conn = sqlite3.connect('data.sqlite')
                c = conn.cursor()

                customerData = [(self.nr_przesylki.get(),self.gabaryt_choose.get(),self.name.get(), self.surname.get(), self.miasto.get(), self.adres.get(), self.nr_dom.get(),
                                 self.nr_miesz.get(), self.kod_pocztowy.get(), self.other.get(), self.status_przesylki_choose.get(),self.nr_id_kuriera_choose.get())]
                for element in customerData:
                    c.execute("INSERT INTO przesylki VALUES (?,?,?,?,?,?,?,?,?,?,?,?) ", element)

                conn.commit()
                c.close()
                conn.close()
                tk.messagebox.showinfo(title="Informacja", message='Udało się dodać przesyłke',)
                break


    def show(self):
        self.window.title("Dodaj przesyłke")
        self.window.mainloop()


class search:
    def __init__(self):
        self.window = tk.Tk()
        self.find_gui()
        self.find_in_database()
        self.show()



    def find_gui(self):
        #pole do wyszukiwania
        self.description = tk.Label(self.window, text="Wpisz numer przesyłki do wyszukania").pack()
        self.find_entry = tk.Entry(self.window, width=40)
        self.find_entry.pack()

        #przycisk
        self.find_button = tk.Button(self.window, text="Szukaj", command=lambda:[self.find_in_database(), self.data_base()]).pack()
        quitbutton2 = tk.Button(self.window, text="Wyjdź do menu",
                                command=lambda: [self.window.destroy(), Window()]).pack()

        self.show()

    def find_in_database(self):
        if self.find_entry.get() == "":
            Errors().error_find()

        else:


            conn = sqlite3.connect('data.sqlite')
            cur = conn.cursor()
            cur.execute("SELECT * FROM przesylki WHERE nr_przesylki=?", (self.find_entry.get(),))
            rows = cur.fetchall()
            for row in rows:

                self.nr_przesylki_out = row[0]
                self.gabaryty_out = row[1]
                self.name_out = row[2]
                self.surname_out = row[3]
                self.miasto_out = row[4]
                self.ulica_out = row[5]
                self.nr_dom_out = row[6]
                self.nr_miesz_out = row[7]
                self.kod_pocztowy_out = row[8]
                self.other_out = row[9]
                self.status_przesylki_choose_out = row[10]
                self.nr_id_kuriera_out = row[11]


    def data_base(self):
        self.window2 = tk.Tk()
        description = tk.Label(self.window2, text='Informacje o przesyłce', padx=150, pady=20).pack()
        description = tk.Label(self.window2, text=(f"Nr przesyłki: {self.nr_przesylki_out}"), padx=150, pady=5).pack()
        description = tk.Label(self.window2, text=(f"Nr przesyłki: {self.gabaryty_out}"), padx=150, pady=5).pack()
        description = tk.Label(self.window2, text=(f"Imie odbiorcy: {self.name_out}"), padx=150, pady=5).pack()
        description = tk.Label(self.window2, text=(f"Nazwisko odbiorcy: {self.surname_out}"), padx=150, pady=5).pack()
        description = tk.Label(self.window2, text=(f"Miasto odbiorcy: {self.miasto_out}"), padx=150, pady=5).pack()
        description = tk.Label(self.window2, text=(f"Ulica odbiorcy:: {self.ulica_out}"), padx=150, pady=5).pack()
        description = tk.Label(self.window2, text=(f"Nr domu odbiorcy:, {self.nr_dom_out}"), padx=150, pady=5).pack()
        description = tk.Label(self.window2, text=(f"Nr mieszkania odbiorcy: {self.nr_miesz_out}"), padx=150, pady=5).pack()
        description = tk.Label(self.window2, text=(f"Kod pocztowy: {self.kod_pocztowy_out}"), padx=150, pady=5).pack()
        description = tk.Label(self.window2, text=(f"Informacje dodatkowe: {self.other_out}"), padx=150, pady=5).pack()
        description = tk.Label(self.window2, text=(f"Status przesyłki: {self.status_przesylki_choose_out}"), padx=150, pady=5).pack()
        description = tk.Label(self.window2, text=(f"Kurier obsługujący przesyłke: {self.nr_id_kuriera_out}"), padx=150,
                               pady=5).pack()

        quitbutton = tk.Button(self.window2, text="Wyszukaj kolejną przesyłke", command=lambda:[self.window2.destroy()]).pack()
        quitbutton2 = tk.Button(self.window2, text="Wyjdź do menu", command=lambda:[self.window.destroy(), self.window2.destroy(), Window()]).pack()

        self.show2()

    def show(self):
        self.window.title("Wyszukiwarka przesyłek")
        self.window.mainloop()
    def show2(self):
        self.window2.title("Informacje o przesyłce")
        self.window2.mainloop()

class dodaj_pracownika:
    def __init__(self):
        self.window =tk.Tk()
        self.window_gui()
        self.show()

    def window_gui(self):



        self.description= tk.Label(self.window, text="Imie").pack()
        self.name = tk.Entry(self.window, width=40, )
        self.name.pack()


        self.description = tk.Label(self.window, text="Nazwisko").pack()
        self.surname = tk.Entry(self.window, width=40, )
        self.surname.pack()
        self.description = tk.Label(self.window, text="Stanowisko").pack()
        n = tk.StringVar()
        self.stanowisko_list = ttk.Combobox(self.window, width=27, textvariable=n)
        self.stanowisko_list['values'] = ('Kurier',
                                     'Konsultant',
                                     'Kurier Paczkomaty',
                                     'Kierownik Magazynu')

        self.stanowisko_list.pack()
        self.stanowisko_list.current(1)

        self.description = tk.Label(self.window, text="Ulica").pack()
        self.adres_ulica = tk.Entry(self.window, width=40, )
        self.adres_ulica.pack()

        self.description = tk.Label(self.window, text="Nr_domu").pack()
        self.nr_domu = tk.Entry(self.window, width=40, )
        self.nr_domu.pack()

        self.description = tk.Label(self.window, text="Miasto").pack()
        self.miasto = tk.Entry(self.window, width=40, )
        self.miasto.pack()

        self.description = tk.Label(self.window, text="Pesel").pack()
        self.pesel = tk.Entry(self.window, width=40, )
        self.pesel.pack()


        self.nrid = StringVar()
        self.description = tk.Label(self.window, text="Nr_Identyfikatora [MAX 8 ZNAKOW]").pack()
        self.nr_id_entry=tk.Entry(self.window, textvariable=self.nrid)
        self.nr_id_entry.pack()


        self.dodaj = tk.Button(self.window, text="Dodaj pracownika", width=20, command=lambda:self.check_len()).pack()
        self.wróc = tk.Button(self.window, text="Wróć do menu", width=20,
                              command=lambda: [self.window.destroy(), Window()]).pack()




    def check_len(self):
        text = len(self.nrid.get())
        if text > 8 or text == 0:
            Errors().error_format()

        else:
            self.dodaj_msg()

    def dodaj_msg(self):
        self.msgBox = tk.messagebox.askquestion('Uwaga!','Czy na pewno chcesz dodać pracownika?', icon='warning')
        if self.msgBox == 'yes':
            self.save_pracownicy()

        else:
            tk.messagebox.showinfo('Uwaga','Pracownik nie został dodany')

        self.show()

    def save_pracownicy(self):
        rows = [self.name.get(), self.surname.get(),self.stanowisko_list.get(),
                self.adres_ulica.get(),self.nr_domu.get(),self.miasto.get(),self.pesel.get(),self.nr_id_entry.get(),
                         ]

        for row in rows:
            if row == "":
                Errors().error_add()
                break

            else:
                conn = sqlite3.connect('data.sqlite')
                c = conn.cursor()

                customerData = [(self.name.get(), self.surname.get(),self.stanowisko_list.get(),
                self.adres_ulica.get(),self.nr_domu.get(),self.miasto.get(),self.pesel.get(),self.nr_id_entry.get())]
                for element in customerData:
                    c.execute("INSERT INTO pracownicy VALUES (?,?,?,?,?,?,?,?) ", element)

                conn.commit()
                c.close()
                conn.close()
                tk.messagebox.showinfo(title="Informacja", message='Udało się dodać pracownika',)
                break

    def show(self):

        self.window.title('Dodaj Pracownika')
        self.window.mainloop()

class wyszukaj_pracownika:
    def __init__(self):
        self.window = tk.Tk()
        self.window_gui()
        self.show()

    def window_gui(self):

        description = tk.Label(self.window, text='Podaj numer identyfikatora pracownika').pack()
        self.numer_id_check= tk.Entry(self.window, )
        self.numer_id_check.pack()
        self.find_button = tk.Button(self.window, text="Szukaj",
                                     command=lambda: [self.find_in_database_pracownik(), self.data_base()]).pack()
        quitbutton2 = tk.Button(self.window, text="Wyjdź do menu",
                                command=lambda: [self.window.destroy(), Window()]).pack()

        self.show()

    def find_in_database_pracownik(self):
        if self.numer_id_check.get() == "":
            Errors().error_found()

        else:


            conn = sqlite3.connect('data.sqlite')
            cur = conn.cursor()
            cur.execute("SELECT * FROM pracownicy WHERE nr_id=?", (self.numer_id_check.get(),))
            rows = cur.fetchall()
            for row in rows:
                self.name_out = row[0]
                self.surname_out = row[1]
                self.stanowisko_out = row[2]
                self.adres_ulica_out = row[3]
                self.nr_domu_out = row[4]
                self.miasto_out = row[5]
                self.pesel_out = row[6]
                self.nr_id_out = row[7]



    def data_base(self):
        self.window2 = tk.Tk()
        description = tk.Label(self.window2, text='Informacje o pracowniku', padx=150, pady=20).pack()
        description = tk.Label(self.window2, text=(f"Imie: {self.name_out}"), padx=150, pady=5).pack()
        description = tk.Label(self.window2, text=(f"Nazwisko: {self.surname_out}"), padx=150, pady=5).pack()
        description = tk.Label(self.window2, text=(f"Stanowisko: {self.stanowisko_out}"), padx=150, pady=5).pack()
        description = tk.Label(self.window2, text=(f"Ulica: {self.adres_ulica_out}"), padx=150, pady=5).pack()
        description = tk.Label(self.window2, text=(f"Nr Domu:: {self.nr_domu_out}"), padx=150, pady=5).pack()
        description = tk.Label(self.window2, text=(f"Miasto:, {self.miasto_out}"), padx=150, pady=5).pack()
        description = tk.Label(self.window2, text=(f"Pesel: {self.pesel_out}"), padx=150, pady=5).pack()
        description = tk.Label(self.window2, text=(f"Nr ID: {self.nr_id_out}"), padx=150, pady=5).pack()


        quitbutton = tk.Button(self.window2, text="Wyszukaj kolejnego Pracownika", command=lambda:[self.window2.destroy()]).pack()
        quitbutton2 = tk.Button(self.window2, text="Wyjdź do menu", command=lambda:[self.window.destroy(), self.window2.destroy(), Window()]).pack()

        self.show2()


    def show(self):
        self.window.title("Wyszukiwarka pracowników")
        self.window.geometry('300x200')
        self.window.mainloop()

    def show2(self):
        self.window2.title("Informacje o pracowniku")
        self.window2.mainloop()









class InfoUpdate:
    def __init__(self):
        self.window =tk.Tk()
        self.info_gui()
        self.show()
    def info_gui(self):
        self.dzien = datetime.date.today()

        description = tk.Label(self.window, text=f"Wersja na dzień {self.dzien}: v1.0.0 ", padx=60,pady=0).pack()
        description = tk.Label(self.window, text="Autor: Daniel Siedlecki ",padx=60, pady=40).pack()
        wroc = tk.Button(self.window, text="Wróć do menu", width=20,command=lambda: [self.window.destroy(), Window()], padx=20, pady=0).pack()
        self.show()

    def show(self):
        self.window.geometry('400x200')
        self.window.title('Informacje')
        self.window.mainloop()

class Errors:
    def __init__(self):
        self.window = tk.Tk()

    def error_add(self):
        self.label = tk.Label(self.window, text="Uzupełnij wymagane pola", padx=60, pady=0).pack()
        self.button = tk.Button(self.window, text="Ok", command=lambda:self.window.destroy(), padx=50, pady=0).pack()
        self.show()

    def error_login(self):
        self.label = tk.Label(self.window, text="Błędne dane logowania", padx=60, pady=0).pack()
        self.button_quit = tk.Button(self.window, text="Ok", command=lambda:self.window.destroy(), padx=50, pady=0).pack()
        self.show()
    def error_find(self):
        self.label = tk.Label(self.window, text="Wpisz numer przesyłki", padx=60, pady=0).pack()
        self.button_quit = tk.Button(self.window, text="Ok", command=lambda:self.window.destroy(), padx=50, pady=0).pack()
        self.show()
    def error_found(self):
        self.label = tk.Label(self.window, text="Błędne dane", padx=60, pady=0).pack()
        self.button_quit = tk.Button(self.window, text="Ok", command=lambda:self.window.destroy(), padx=50, pady=0).pack()
        self.show()
    def error_format(self):
        self.label = tk.Label(self.window, text="Niepoprawny format sprawdź ilość znaków", padx=60, pady=0).pack()
        self.button_quit = tk.Button(self.window, text="Ok", command=lambda:self.window.destroy(), padx=50, pady=0).pack()
        self.show()
    def show(self):
        self.window.title("Błędne dane")
        self.window.geometry("300x50")
        self.window.mainloop()



win = Login()