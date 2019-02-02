# Belajar Break
# Untuk menghentikan pengulangan

#contoh di For-Loop
for i in range(1, 100):
    if i % 50 == 0:
        break
    print(i)

#contoh di While-Loop
while True:
    data = input("Data : ")
    if data == "x":
        break
    print(data)