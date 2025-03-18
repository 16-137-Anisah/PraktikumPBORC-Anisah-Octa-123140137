import random

class Father:
    def __init__(self, goldar):
        self.goldar = goldar

class Mother:
    def __init__(self, goldar):
        self.goldar = goldar

class Child:
    def __init__(self, father, mother):
        self.blood_type = self.determine_blood_type(father, mother)

    def determine_blood_type(self, father, mother):
        alel_father = random.choice(father.goldar)
        alel_mother = random.choice(mother.goldar)
        return alel_father + alel_mother

    def __str__(self):
        return f"Golongan darah anak: {self.blood_type}"

father = Father(input("Masukkan genotipe ayah: "))
mother = Mother(input("Masukkan genotipe ibu: "))

child = Child(father, mother)
print(child)
