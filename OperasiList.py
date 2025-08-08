data_angka = [1,4,5,5,2,7,4,8,7,9,4,7,3]
print(f"data angka sama dengan \n{data_angka}")

# count data
jumlah_data_4 = data_angka.count(4)
jumlah_data_7 = data_angka.count(7)
jumlah_data_1 = data_angka.count(1)

print(f"jumlah data 4 = {jumlah_data_4}")
print(f"jumlah data 7 = {jumlah_data_7}")
print(f"jumlah data 1 = {jumlah_data_1}")

# ambil posisi data (index)
data = ["ayyu", "citra", "sofie", "eri"]
print(f"data = {data}")

index_ayyu = data.index("ayyu")
index_eri = data.index("eri")

print(f"index si ayyu = {index_ayyu}")
print(f"index si eri = {index_eri}")


# mengurutkan list
print(f"data angka sebelum sort = \n{data_angka}")
data_angka.sort()
print(f"data setelah sort = \n{data_angka}")

print(f"data = {data}")
data.sort()
print(f"data sort = {data}")

# balik list nya
data_angka.reverse()
data.reverse()
print(f"data di reserve = \n{data_angka} \n{data}")