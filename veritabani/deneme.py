import sqlite3


db = sqlite3.connect("sifreler.sqlite")

im = db.cursor()

create_tablo = """

CREATE TABLE IF NOT EXISTS kullanicilar (username,password)

"""
im.execute(create_tablo)
veriler = [
    ("yunusemre","123456"),
    ("ahmet","5688"),
    ("tom","deneme")
]


for i in veriler:
    im.execute("""
               INSERT INTO kullanicilar VALUES (?,?)""",i)


db.commit()


kull = input("Kullanıcı adınızı giriniz: ") 
Sif = input("Şifrenizi giriniz: ")

kontrol = """
    SELECT * FROM kullanicilar Where username = ? AND password = ?

"""

im.execute(kontrol, (kull,Sif))

data = im.fetchone()

if data:
    print("hoşgeldiniz")

else:
    print("hatalı değer")