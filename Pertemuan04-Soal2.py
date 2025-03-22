class TaskNotFoundError(Exception):
    pass

class ToDoList:
    def __init__(self):
        self.tasks = []

    def tambah_tugas(self, tugas):
        if not tugas.strip():
            raise ValueError("Tugas tidak boleh kosong.")
        self.tasks.append(tugas)
        print("Tugas berhasil ditambahkan!")

    def hapus_tugas(self, nomor):
        try:
            index = int(nomor) - 1
            if index < 0 or index >= len(self.tasks):
                raise TaskNotFoundError(f"Error: Tugas dengan nomor {nomor} tidak ditemukan.")
            del self.tasks[index]
            print("Tugas berhasil dihapus!")
        except ValueError:
            print("Input tidak valid. Masukkan angka yang benar.")
        except TaskNotFoundError as e:
            print(e)

    def tampilkan_tugas(self):
        if not self.tasks:
            print("Daftar tugas kosong.")
        else:
            print("Daftar Tugas:")
            for i, tugas in enumerate(self.tasks, 1):
                print(f"{i}. {tugas}")

def main():
    todo_list = ToDoList()

    while True:
        print("\nPilih aksi:")
        print("1. Tambah tugas")
        print("2. Hapus tugas")
        print("3. Tampilkan daftar tugas")
        print("4. Keluar")

        pilihan = input("Masukkan pilihan (1/2/3/4): ")

        try:
            if pilihan == "1":
                tugas = input("Masukkan tugas yang ingin ditambahkan: ")
                todo_list.tambah_tugas(tugas)
            elif pilihan == "2":
                nomor = input("Masukkan nomor tugas yang ingin dihapus: ")
                todo_list.hapus_tugas(nomor)
            elif pilihan == "3":
                todo_list.tampilkan_tugas()
            elif pilihan == "4":
                print("Keluar dari program.")
                break
            else:
                print("Pilihan tidak valid. Masukkan angka 1-4.")
        except ValueError as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    main()
