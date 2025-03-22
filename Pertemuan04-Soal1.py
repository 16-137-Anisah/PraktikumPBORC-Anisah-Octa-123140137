def ngitung_kuadrat():
    while True:
        try:
            x = float(input("Masukkan angka: "))
            
            if x < 0:
                print("Input tidak valid. Harap masukkan angka positif.")
            elif x == 0:
                print("Akar kuadrat dari nol tidak diperbolehkan.")
            else:
                print(f"Akar kuadrat dari {x} adalah {x ** 0.5}")
                break
        except ValueError:
            print("Input tidak valid. Harap masukkan angka yang valid.")

ngitung_kuadrat()
