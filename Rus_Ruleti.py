import random as rd
import tkinter as tk


def random():
    liste = [1,2,3,4,5,6]
    rd.shuffle(liste)
    for eleman in liste:
        if eleman == 5:
            return "Öldün"
        else: 
            return ""
def butona_tikla():
    label1.config(text=random())
    
Ekran = tk.Tk()
Ekran.geometry("300x200+400+400")
Ekran.title("Rus Ruleti.")

label = tk.Label(Ekran, text = "Aşağıdaki Butona Basınız.")
label.pack()

btn = tk.Button(Ekran, text = "Ateş!", command = butona_tikla)
btn.pack()

label1 = tk.Label(Ekran, text = "")
label1.pack()

Ekran.mainloop()