class TugasTidakDitemukanError(Exception):
    pass

class NugasSS:
    def __init__(self):
        self.tugas = []

    def tambah_tugas(self, tugas_baru):
        if not tugas_baru.strip():
            raise ValueError("Tugas tidak boleh kosong.")
        self.tugas.append(tugas_baru)
        print("Tugas berhasil ditambahkan!")

    def hapus_tugas(self, nomor):
        try:
            index = int(nomor) - 1
            if index < 0 or index >= len(self.tugas):
                raise TugasTidakDitemukanError(f"Error: Tugas dengan nomor {nomor} tidak ditemukan.")
            del self.tugas[index]
            print("Tugas berhasil dihapus!")
        except ValueError:
            print("Input tidak valid. Masukkan angka yang benar.")
        except TugasTidakDitemukanError as e:
            print(e)

    def tampilkan_tugas(self):
        if not self.tugas:
            print("Daftar tugas kosong.")
        else:
            print("Daftar Tugas:")
            for i, tugas in enumerate(self.tugas, 1):
                print(f"{i}. {tugas}")

def main():
    nugas = NugasSS()

    while True:
        print("\nPilih aksi:")
        print("1. Tambah tugas")
        print("2. Hapus tugas")
        print("3. Tampilkan daftar tugas")
        print("4. Keluar")

        pilihan = input("Masukkan pilihan (1/2/3/4): ")

        try:
            if pilihan == "1":
                tugas_baru = input("Masukkan tugas yang ingin ditambahkan: ")
                nugas.tambah_tugas(tugas_baru)
            elif pilihan == "2":
                nomor = input("Masukkan nomor tugas yang ingin dihapus: ")
                nugas.hapus_tugas(nomor)
            elif pilihan == "3":
                nugas.tampilkan_tugas()
            elif pilihan == "4":
                print("Keluar dari program.")
                break
            else:
                print("Pilihan tidak valid. Masukkan angka 1-4.")
        except ValueError as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    main()