from tkinter import *
from datetime import datetime


def saat_f():
    def dongu():
        
        suan = datetime.now()
        hour = suan.hour
        minute = suan.minute
        saat_D= str(hour)+":"+str(minute)
        print(saat_D)
        canvas.itemconfig(saat,text=saat_D)
        window.after(1000,dongu)

    window = Tk()
    window.title("Saat")
    window.geometry("600x800")
    window.configure(bg = "#ffffff")
    canvas = Canvas(
        window,
        bg = "#ffffff",
        height = 800,
        width = 600,
        bd = 0,
        highlightthickness = 0,
        relief = "ridge")
    canvas.place(x = 0, y = 0)

    background_img = PhotoImage(file = f"Giris/Saat_background.png")
    background = canvas.create_image(
        300.0, 400.0,
        image=background_img)

    saat = canvas.create_text(
        190.0, 269.0,
        text = "00:00",
        fill = "#ffffff",
        font = ("IrishGrover-Regular", int(90.0)))

    dongu()

    window.resizable(False, False)
    window.mainloop()
