from tkinter import *
import sqlite3


db = sqlite3.connect("sifreler.sqlite")

im = db.cursor()


def btn_clicked() -> None:
    kull = entry0.get()
    Sif = entry1.get()
    kontrol = """
    SELECT * FROM kullanicilar Where username = ? AND password = ?

    """

    im.execute(kontrol, (kull,Sif))

    data = im.fetchone()

    if data:
        print("hoşgeldiniz")

    else:
        print("hatalı değer")


window = Tk()

window.geometry("600x400")
window.configure(bg="#ffffff")
canvas = Canvas(
    window,
    bg="#ffffff",
    height=400,
    width=600,
    bd=0,
    highlightthickness=0,
    relief="ridge")
canvas.place(x=0, y=0)

background_img = PhotoImage(file="background.png")
background = canvas.create_image(
    300.00000000000006, 200.00000000000006,
    image=background_img)

entry0_img = PhotoImage(
    file="img_textBox0.png")
entry0_bg = canvas.create_image(
    312.5, 212.5,
    image=entry0_img)

entry0 = Entry(
    bd=0,
    bg="#f5f5f5",
    highlightthickness=0)

entry0.place(
    x=248.0, y=200.0,
    width=129.0,
    height=23)

entry1_img = PhotoImage(
    file="img_textBox1.png")
entry1_bg = canvas.create_image(
    312.5, 255.5,
    image=entry1_img)

entry1 = Entry(
    bd=0,
    bg="#f5f5f5",
    highlightthickness=0)

entry1.place(
    x=248.0, y=243.0,
    width=129.0,
    height=23)

img0 = PhotoImage(file="img0.png")
b0 = Button(
    image=img0,
    borderwidth=0,
    highlightthickness=0,
    command=btn_clicked,
    relief="flat")

b0.place(
    x=319.0, y=281.0,
    width=67,
    height=23)

window.resizable(False, False)
window.mainloop()
