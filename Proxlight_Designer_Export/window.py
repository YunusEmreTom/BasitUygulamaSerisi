from tkinter import *
from pencere import *
from tkinter import messagebox
username = "yunusemretom@gmail.com"
password = "1234567890"

def kontol():
    kullanici_d=kullanici.get()
    sifre_d = sifre.get()
    if kullanici_d == username and sifre_d == password:
        print("uygundur")
        window.destroy()
        
        pencere_F()
        
    else:
        messagebox.showerror(title="HATA", message="kullanıcı adı veya şifre hatalıdır.")
        print("kullanıcı adı veya şifre hatalıdır.")
    

window = Tk()
window.title("Basit uygulama serisi")
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

background_img = PhotoImage(file = f"Proxlight_Designer_Export/background.png")
background = canvas.create_image(
    300.0, 200.0,
    image=background_img)

entry0_img = PhotoImage(file = f"Proxlight_Designer_Export/img_textBox0.png")
entry0_bg = canvas.create_image(
    383.0, 132.0,
    image = entry0_img)

kullanici = Entry(
    bd = 0,
    bg = "#6ea2d2",
    highlightthickness = 0)

kullanici.place(
    x = 297.0, y = 117,
    width = 172.0,
    height = 28)

entry1_img = PhotoImage(file = f"Proxlight_Designer_Export/img_textBox1.png")
entry1_bg = canvas.create_image(
    383.0, 180.0,
    image = entry1_img)

sifre = Entry(
    bd = 0,
    bg = "#6ea2d2",
    highlightthickness = 0,show="*")

sifre.place(
    x = 297.0, y = 165,
    width = 172.0,
    height = 28)

img0 = PhotoImage(file = f"Proxlight_Designer_Export/img0.png")
b0 = Button(
    image = img0,
    borderwidth = 0,
    highlightthickness = 0,
    command = kontol,
    relief = "flat")

b0.place(
    x = 407, y = 213,
    width = 64,
    height = 31)

window.resizable(False, False)
window.mainloop()
