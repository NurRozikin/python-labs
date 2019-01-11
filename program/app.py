# Program Management Kontak

import function_program

# List of dictionary
daftar_kontak = []
daftar_kontak.append({"nama":"kien","email":"nur.rozikien@gmail.com","telepon":"123"})

# Menu program
while True:
    print("# Menu")
    print("1. Daftar Kontak")
    print("2. Tambah Kontak")
    print("3. Hapus Kontak")
    print("4. Cari Kontak")

    menu = input("Pilih menu : ")

    if menu == "0":
        break
    elif menu == "1":
        print(function_program.display_kontak(daftar_kontak))
    elif menu == "2":
        daftar_kontak.append(function_program.new_kontak())
        print(function_program.display_kontak(daftar_kontak))
    elif menu == "3":
        function_program.hapus_kontak(daftar_kontak)
    elif menu == "4":
        function_program.cari_kontak(daftar_kontak)
print("Program selesai berjalan, sampai jumpa")