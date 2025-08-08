# index 
data = ["lala", "ayyu", "lili", "kinan"]
data_0 = data[0]
print(f"data pertama (index 0 adalah {data_0})")

data_terakhir = data[-1]
print(f"data terakhir adalah {data_terakhir}")

data_ayyu = data[-3]
print(f"data ayyu = {data_ayyu}")

# panjang data
panjang_data = len(data)
print(f"panjang data = {panjang_data}")

# menambahkan item pada list
print(f"data sebelum ditambah = \n{data}")

data.insert(1,"donat")
print(f"data sesudah ditambah = \n{data}")

# menambah di akhir list
data.append("gege")
print(f"data ditambah lagi =\n{data}")

# menambahkan list dengan list
data_baru =["hgp", "rendy", "fathan"]
data.extend(data_baru)
print(f"data gabungan =\n{data}")

# merubah data
# merubah data ke 2 menjadi michael
data[2] = "michael"
print(f"data rubah = {data}")

# meremove data
data.remove("michael")
print(f"data remove = \n{data}")

# meremove data paling belakang
data_akhir = data.pop()
print(f"data akhir = \n{data}")
print(data_akhir)