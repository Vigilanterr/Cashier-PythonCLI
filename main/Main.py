tasks = []

def display_menu():
    print("\n Menu:")
    print("1. Lihat")
    print("2. Tambah")
    print("3. Hapus")
    print("4. Ubah Harga")
    print("5. Hitung rata2")
    print("6. Keluar")

def lihat():
    print('\nData:')
    if not tasks:
        print("Data kosong")
        return
    i = 1
    for item in tasks:
        print(f"{i}. {item[0]}: Rp{item[1]:,}")
        i += 1

def tambah():
    nama = input("Nama HP: ")
    harga = input("Harga: Rp")
    tasks.append([nama, int(harga)])
    print(f"{nama} berhasil ditambah")

def hapus():
    if not tasks:
        print("Data kosong")
        return
    lihat()
    idx = int(input("\nNomor yang dihapus: ")) - 1
    nama = tasks[idx][0]
    tasks.pop(idx)
    print(f"{nama} berhasil dihapus")

def ubah_harga():
    if not tasks:
        print("Data kosong")
        return
    lihat()
    idx = int(input("\nNomor yang diubah: ")) - 1
    nama = tasks[idx][0]
    harga_baru = int(input(f"Harga baru {nama}: Rp"))
    tasks[idx][1] = harga_baru
    print(f"Harga {nama} jadi Rp{harga_baru:,}")

def rata_rata():
    if not tasks:
        print("Data kosong")
        return
    total = 0
    for item in tasks:
        total += item[1]
    print(f"\nRata-rata: Rp{total // len(tasks):,}")

def main():
    while True:
        display_menu()
        choice = input('Pilih menu 1-6: ')

        if choice == '1':
            lihat()
        elif choice == '2':
            tambah()
        elif choice == '3':
            hapus()
        elif choice == '4':
            ubah_harga()
        elif choice == '5':
            rata_rata()
        elif choice == '6':
            print("babai")
            break
        else:
            print("yg lain aja dah")

main()
