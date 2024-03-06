import tkinter as tk
arayüz = tk.Tk()
arayüz.title("Şifre")
arayüz.geometry("400x200")
a1 = "yunus emre"
a2 = "tom"

kullanici = tk.Label(text="KULLANICI ADI:")
kullanici.place(x=20,y=10)

y= tk.StringVar()
kullanici_girisi = tk.Entry(textvariable=y)
kullanici_girisi.place(x=130,y=10)

kullanici = tk.Label(text="Şifre GİRİSİ:")
kullanici.place(x=20,y=35)

x= tk.StringVar()
kullanici_girisi = tk.Entry(textvariable=x)
kullanici_girisi.place(x=130,y=30)

doğru_yanlis = tk.Label(text="", font="Verdana 10 bold")
doğru_yanlis.place(x=100,y=95)
def giris_komut():
	kullan = y.get()
	sif = x.get()
	if kullan == a1 and sif == a2:
		print("doğru")
		doğru_yanlis.config(text="DOĞRU",fg="green")
	else:
		doğru_yanlis.config(text="YANLIŞ",fg="red")	
giris = tk.Button(text="Giris",command=giris_komut)
giris.place(x=150,y=55)

arayüz.mainloop()