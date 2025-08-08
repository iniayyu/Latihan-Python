"""Fungsi dengan argument (input)"""

def hello_world(nama):
    """fungsi hello world"""
    print(f"selamat datang dunia wahai {nama}")

hello_world("ayyu")

# program tambah
def tambah(angka1,angka2):
    hasil = angka1 + angka2
    print(f"{angka1} + {angka2} = {hasil}")
    
tambah(10,76)
tambah(98,34)


def say_hi(list_peserta):
    data_peserta = list_peserta.copy()
    for peserta in data_peserta:
        print(f"yang terhormat {peserta}")
        
anggota = ["ayyu","donat","gege","manai"]
say_hi(anggota)