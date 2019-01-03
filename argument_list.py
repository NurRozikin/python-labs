# Belajar Argument List

def jumlahkan(x, *list_angka):
    total = 0
    for angka in list_angka:
        total = total + angka
    print(f"Total {list_angka} = {total}")

jumlahkan(10,10,10)