class Animal:
    def make_sound(self):
        return "Suara hewan tidak diketahui"
    
    def describe(self):
        return "Ini adalah hewan di kebun binatang."

class Anjing(Animal):
    def make_sound(self):
        return "Guk! Guk!"
    
    def describe(self):
        return "Anjing adalah hewan yang biasanya setia dan suka bermain."

class Kucing(Animal):
    def make_sound(self):
        return "Meong! Meong!"
    
    def describe(self):
        return "Kucing adalah hewan yang biasanya dipelihara oleh banyak orang karna imut"

class Burung(Animal):
    def make_sound(self):
        return "Cuit! Cuit!"
    
    def describe(self):
        return "Burung adalah hewan terbang yang biasanya bersarang di atas pohon."

class Gajah(Animal):
    def make_sound(self):
        return "Hooooooooo!"
    
    def describe(self):
        return "Gajah adalah hewan darat terbesar dengan belalai panjang dan gading"

class Kambing(Animal):
    def make_sound(self):
        return "Mbeek! Mbeek!"
    
    def describe(self):
        return "Kambing adalah hewan berjenggot."

class Sapi(Animal):
    def make_sound(self):
        return "Mooo! Mooo!"
    
    def describe(self):
        return "Sapi adalah hewan ternak besar yang sering dimanfaatkan untuk susu dan daging."

# Program utama
try:
    daftar_hewan = {
        "anjing": Anjing(),
        "kucing": Kucing(),
        "burung": Burung(),
        "gajah": Gajah(),
        "kambing": Kambing(),
        "sapi": Sapi()
    }
    
    jenis = input("Masukkan jenis hewan (anjing/kucing/burung/gajah/kambing/sapi): ").strip().lower()
    if jenis in daftar_hewan:
        hewan = daftar_hewan[jenis]
        print(hewan.describe())
        print("Suaranya", hewan.make_sound())
    else:
        print("Hewan tidak ditemukan dalam daftar kebun binatang.")
except Exception as e:
    print("Terjadi kesalahan:", e)
