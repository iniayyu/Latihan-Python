# for loop
print("For Loop")
kumpulan_angka = [4,3,2,5,6,1]
for angka in kumpulan_angka:
    print(f"angka = {angka}")
    

peserta = ["ayyu","lala","donat","gege","naila"]
for nama in peserta:
    print(f"nama = {nama}")
    
# for loop dan range
print("\nFor Loop dan Range")
kumpulan_angka = [10,5,4,2,6,5]
panjang = len(kumpulan_angka)

for i in range(panjang):
    print(f"angka = {kumpulan_angka[i]}")
    
# while
print("\nwhile loop")
data = ["ayyu",1,2,3,"naila"]
[print(f"data = {i}") for i in data]
panjang = len(kumpulan_angka)
i = 0

while i < panjang :
    print(f"angka = {kumpulan_angka[i]}")
    i += 1
    
# list comperhesion
print("\nList Comperhesion")
data = ["ayyu",1,2,3,"naila"]
[print(f"data = {i}") for i in data]
angka = [10,5,4,2,6,5]
angka_kuadrat = [i**2 for i in angka]
print(angka_kuadrat)


# enumerate
print("\ndata enumerate")
data_list = ["ayyu",1,2,3,"naila"]

for index,data in enumerate(data_list):
    print(f"index = {index}, data = {data}")