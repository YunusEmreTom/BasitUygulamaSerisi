from tkinter import *
from Saat import *
from tkinter import messagebox

username = "yunus emre"
password = "tom"

def kontrol():
    kullanici_adi = kullanici_adi_V.get()
    sifre = sifre_V.get()
    if kullanici_adi == username and sifre == password:
        print("oldu")
        window.destroy()
        saat_f()
    else:
        messagebox.showwarning("Uyarı","Kullanıcı adı veya şifre hatalıdır.")
        print("kullanıcı adı veya şifre hatalıdır.")

window = Tk()
window.title("Giris Sayfası")
window.geometry("600x400")
window.configure(bg = "#ffffff")
canvas = Canvas(
    window,
    bg = "#ffffff",
    height = 400,
    width = 600,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge")
canvas.place(x = 0, y = 0)

background_img = PhotoImage(file = f"Giris/background.png")
background = canvas.create_image(
    300.0, 200.0,
    image=background_img)

entry0_img = PhotoImage(file = f"Giris/img_textBox0.png")
entry0_bg = canvas.create_image(
    312.5, 212.5,
    image = entry0_img)

kullanici_adi_V = Entry(
    bd = 0,
    bg = "#f5f5f5",
    highlightthickness = 0)

kullanici_adi_V.place(
    x = 248.0, y = 200,
    width = 129.0,
    height = 23)

entry1_img = PhotoImage(file = f"Giris/img_textBox1.png")
entry1_bg = canvas.create_image(
    312.5, 255.5,
    image = entry1_img)

sifre_V = Entry(
    bd = 0,
    bg = "#f5f5f5",
    highlightthickness = 0,show="*")

sifre_V.place(
    x = 248.0, y = 243,
    width = 129.0,
    height = 23)

img0 = PhotoImage(file = f"Giris/img0.png")
b0 = Button(
    image = img0,
    borderwidth = 0,
    highlightthickness = 0,
    command = kontrol,
    relief = "flat")

b0.place(
    x = 319, y = 281,
    width = 67,
    height = 23)

window.resizable(False, False)
window.mainloop()
