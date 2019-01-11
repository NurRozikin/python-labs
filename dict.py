# Belajar Tipe Data Dictionary
# Tempat nyimpen data seperti List

customer = {"name" :"Kien", "age" : 34, "address": "Depok"}

name = customer["name"]
age = customer["age"]
address = customer["address"]

print(f"{name} {age} {address}")

for key in customer:
    value = customer[key]
    print(f"{key} : {value}")

print("")
customer["company"]= "x"
customer['age'] = 30
del customer["address"]

for key, value in customer.items():
    print(f"{key} : {value}")

