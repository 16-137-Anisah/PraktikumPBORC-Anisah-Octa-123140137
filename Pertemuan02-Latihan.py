class Kendaraan:
    def __init__(self, jenis, kecepatan_maksimum):
        self.jenis = jenis
        self.kecepatan_maksimum = kecepatan_maksimum
    
    def info_kendaraan(self):
        return f"Jenis Kendaraan: {self.jenis}, Kecepatan Maksimum: {self.kecepatan_maksimum} km/jam"
    
    def bergerak(self):
        return f"Kendaraan {self.jenis} sedang bergerak."

class Mobil(Kendaraan):
    def __init__(self, jenis, kecepatan_maksimum, merk, jumlah_pintu):
        super().__init__(jenis, kecepatan_maksimum)
        self.merk = merk
        self.jumlah_pintu = jumlah_pintu
    
    def info_mobil(self):
        return f"Mobil: {self.merk}, Jenis: {self.jenis}, Kecepatan Maksimum: {self.kecepatan_maksimum} km/jam, Pintu: {self.jumlah_pintu}"
    
    def bunyikan_klakson(self):
        return "Beep! Beep!"

class MobilSport(Mobil):
    def __init__(self, jenis, kecepatan_maksimum, merk, jumlah_pintu, tenaga_kuda, harga):
        super().__init__(jenis, kecepatan_maksimum, merk, jumlah_pintu)
        self.__tenaga_kuda = tenaga_kuda
        self.__harga = harga
    
    def get_tenaga_kuda(self):
        return self.__tenaga_kuda
    
    def set_tenaga_kuda(self, value):
        if value > 0:
            self.__tenaga_kuda = value
        else:
            print("Tenaga kuda harus lebih dari 0!")
    
    def get_harga(self):
        return self.__harga
    
    def set_harga(self, value):
        if value > 0:
            self.__harga = value
        else:
            print("Harga harus lebih dari 0!")
    
    def info_mobil_sport(self):
        return f"Mobil Sport: {self.merk}, Jenis: {self.jenis}, Kecepatan Maksimum: {self.kecepatan_maksimum} km/jam, Pintu: {self.jumlah_pintu}, Tenaga Kuda: {self.__tenaga_kuda} HP, Harga: {self.__harga} juta"
    
    def mode_balap(self):
        return f"{self.merk} masuk ke mode balap!"

mobil_sport = MobilSport("Kuda??", 350, "bombomkar", 2, 700, 15000)
print(mobil_sport.info_mobil_sport())
print(mobil_sport.mode_balap())
print("Tenaga Kuda:", mobil_sport.get_tenaga_kuda(), "HP")
mobil_sport.set_tenaga_kuda(750)
print("Tenaga Kuda setelah diubah:", mobil_sport.get_tenaga_kuda(), "HP")
print("Harga:", mobil_sport.get_harga(), "ribu")
mobil_sport.set_harga(16000)
print("Harga setelah diubah:", mobil_sport.get_harga(), "kuadriliun")
