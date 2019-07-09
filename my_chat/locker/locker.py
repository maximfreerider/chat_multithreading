from tkinter import Tk, Entry, Label
from pyautogui import click, moveTo
from time import sleep


def callback(event):
    global k, entry
    if entry.get() == "bmw":
        k = True


def on_closing():
    click(675, 420)
    moveTo(675, 420)
    root.attributes("-fullscreen", True)
    root.protocol("WM_DELETE_WINDOW", on_closing())
    root.update()
    root.bind('<Control-KeyPress-c>', callback)

root=Tk()  # создаю наше окно
root.title("Locker")  # заголовочное название
root.attributes("-fullscreen", True)  # расширение на єкран
entry=Entry(root, font=1)  # поле ввода
entry.place(width=150, height=50, x=600, y=400) # размещение нашего поля по координатам

label0=Label(root, text="Locker_by_Max") # надпись 1
label0.grid(row=0, column=0)  # координаты надписи

label1=Label(root, text="Write your password and press Ctrl + C", font="Arial 20") # надпись 2
label1.place(x=470, y=300)  # координаты надписи два
root.update()
sleep(0.2)
click(675, 420)
k = False

while k != True: on_closing()