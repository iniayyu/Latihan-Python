# contoh 1
def say_hello(nama = "cantik"):
    print(f"halo {nama}")
    
say_hello("ayyu")
say_hello() 

# contoh 2
def sapa_dia(nama, pesan = "apa kabar"):
    print(f"hai {nama}, {pesan}")
    
sapa_dia("ayyu", "hai cantikk")
sapa_dia("ayyu")

#contoh 3
def hitung_pangkat(angka, pangkat = 2):
    hasil = angka**pangkat
    return(hasil) 

print(hitung_pangkat(3,7))
hasil = hitung_pangkat(pangkat = 8, angka=9)
print(hasil)

# contoh 4
def fungsi(input1=1,input2=2,input3=3,input4=4):
    hasil = input1 + input2 + input3 + input4
    return hasil

print(fungsi())
print(fungsi(input3=10))

bilangan = (5 % 3 ** 2) + (3 + 2 * 2) * (4 - 2) 
print(bilangan)