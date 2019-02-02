# Belajar Set
# Sama kaya List dan Tuple, cuma ga bisa save data yg sama harus unik.
# perbedaan yg lain hasilnya pada saat di print selalu acak

# list => []
# tuple => ()
# set => {}

nama = {"eko","joko","eko","andi"}
nama.add("kien")
for data in nama:
    print(data)
nama.remove("andi")
print(nama)