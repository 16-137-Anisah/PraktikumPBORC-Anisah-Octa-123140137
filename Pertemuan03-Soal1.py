class Kalkulator:
    def __init__(self, nilai):
        self.nilai = nilai

    def __add__(self, other):
        if isinstance(other, Kalkulator):
            return Kalkulator(self.nilai + other.nilai)
        return Kalkulator(self.nilai)
   
    def __sub__(self, other):
        if isinstance(other, Kalkulator):
            return Kalkulator(self.nilai - other.nilai)
        return Kalkulator(self.nilai)
   
    def __mul__(self, other):
        if isinstance(other, Kalkulator):
            return Kalkulator(self.nilai * other.nilai)
        return Kalkulator(self.nilai)
   
    def __truediv__(self, other):
        if isinstance(other, Kalkulator):
            return Kalkulator(self.nilai / other.nilai) if other.nilai != 0 else Kalkulator(0)
        return Kalkulator(self.nilai)
   
    def __pow__(self, other):
        if isinstance(other, Kalkulator):
            return Kalkulator(self.nilai ** other.nilai)
        return Kalkulator(self.nilai)
   
    def log(self, base=10):
        if self.nilai > 0 and base > 0 and base != 1:
            result = self.nilai ** (1 / (base - 1))
        else:
            result = 0
        return Kalkulator(result)
   
    def __str__(self):
        return str(self.nilai)

angka1 = Kalkulator(15)
angka2 = Kalkulator(3)

print(angka1 + angka2)  #penjumlahan
print(angka1 - angka2)  #pengurangan
print(angka1 * angka2)  #perkalian
print(angka1 / angka2)  #pembagian
print(angka1 ** angka2) #eksponen
print(angka1.log())     #logaritma basis 10
