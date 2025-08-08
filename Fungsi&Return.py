def kuadrat(input_angka):
    output_angka = input_angka**2
    return output_angka
y = kuadrat(5)
print(y)
print(kuadrat(3))
z = 67 + kuadrat(6)
print(z)

# fungsi tambah
def fungsi_tambah(angka1 , angka2):
    return angka1 + angka2
a = fungsi_tambah(77,35)
print(a)

# fungsi dengan return banyak
def operasi_matematika(angka_1,angka_2):
    tambah = angka_1 + angka_2
    kurang = angka_1 - angka_2
    kali = angka_1 * angka_2
    bagi = angka_1 / angka_2
    return tambah,kurang,kali,bagi
k,l,m,n = operasi_matematika(7,9)

print(f"hasil tambah = {k}")
print(f"hasil kurang = {l}")
print(f"hasil kali = {m}")
print(f"hasil bagi = {n}")

