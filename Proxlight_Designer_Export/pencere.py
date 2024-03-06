from tkinter import *
import datetime

def pencere_F():
        
    def whiledongusu():

        a = datetime.datetime.now()
        hour = a.hour
        minute = a.minute
        toplu = str(hour)+":"+str(minute)
        canvas.itemconfig(text, text=toplu)
        print(toplu)
        saat.after(1000, whiledongusu)
        
    saat = Tk()

    saat.geometry("744x800")
    saat.configure(bg = "#ffffff")
    canvas = Canvas(
        saat,
        bg = "#ffffff",
        height = 800,
        width = 744,
        bd = 0,
        highlightthickness = 0,
        relief = "ridge")
    canvas.place(x = 0, y = 0)

    background_img = PhotoImage(file = f"Proxlight_Designer_Export/arkaplan.png")
    background = canvas.create_image(
        400.0, 400.0,
        image=background_img)

    text = canvas.create_text(
        590, 400,
        text = "00:00",
        fill = "#ffffff",
        font = ("None", int(90.0)))
    whiledongusu()

    saat.resizable(False, False)
    saat.mainloop()

