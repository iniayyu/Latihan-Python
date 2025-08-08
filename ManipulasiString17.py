# 1. Menyambung String
nama_pertama = "wahyu"
nama_kedua = "setia"
nama_ketiga = "wardani"
nama_lengkap = nama_pertama + " " + nama_kedua + " " + nama_ketiga
print(nama_lengkap)

# 2. Menghitung panjang string
panjang = len(nama_lengkap)
print(panjang)

# 3. Operator Untuk string
a = "a"
status =  a in nama_lengkap
print( a + " ada di " + nama_lengkap + " = " + str((status)))

a = "a"
status =  a not in nama_lengkap
print( a + " tidak ada di " + nama_lengkap + " = " + str((status)))

print("a" * 5)

print("index ke-0 : " + nama_lengkap[0])
print("index ke-0 : " + nama_lengkap[8])
print("index ke-(-1) : " + nama_lengkap[-1])
print("index ke-[0,2,4,6,8,10] : " + nama_lengkap[0:10:2])

# Paling kecil
print("paling kecil :" + min(nama_lengkap))
print("paling besar :" + max(nama_lengkap))

# 4. Operator Dalam Bentuk Method
data = "wahyu setia wardani"
jumlah = data.count("a")
print(" jumlah a pada data " + data + " = " + str(jumlah))

# 5. upper
salam = "bro!"
print("normal = " + salam)
salam = salam.upper()
print("upper = " + salam)
salam = salam.lower()
print("lower = " + salam)

# Penggabungan
pisah = ['aku' , 'sayang' , 'kamu']
gabungan = ','. join(pisah)
print(pisah)
print(gabungan)

gabungan = ' '. join(pisah)
print(gabungan)

gabungan = ' ya '. join(pisah)
print(gabungan)

gabungan = "akuyasayangyakamu"
print(gabungan.split('ya'))

# Alokasi Karakter
kanan = "kanan".rjust(10)
print("'"+kanan+"'")

kiri = "kiri".ljust(10)
print("'"+kiri+"'")

tengah = "tengah".center(10, "-")
print("'"+tengah+"'")

#  Kebalikannya
kanan = kanan.strip()
print("'"+kanan+"'")
