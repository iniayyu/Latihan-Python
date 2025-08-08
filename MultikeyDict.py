import datetime

mahasiswa1 = {
    'nama':'ayyu',
    'nim':'2412500916',
    'sks_lulus': 134,
    'beasiswa':'False',
    'lahir':datetime.datetime(2025,7,19) 
}
mahasiswa2 = {
    'nama':'lala',
    'nim':'2412588916',
    'sks_lulus':104,
    'beasiswa':'False',
    'lahir':datetime.datetime(2012,4,19) 
}
mahasiswa3 = {
    'nama':'lulu',
    'nim':'2412504316',
    'sks_lulus':130,
    'beasiswa':'False',
    'lahir':datetime.datetime(2024,7,22) 
}

data_mahasiswa = {
    'MAH001': mahasiswa1,
    'MAH002': mahasiswa2,
    'MAH003': mahasiswa3
}

print(f"{'KEY':<6} {'Nama':<17} {'SKS':<3} {'Beasiswa':<9} {'Lahir':<10}")
print("="*50)

for mahasiswa in data_mahasiswa:
    KEY = mahasiswa 
    NIM = data_mahasiswa[KEY]['nim']
    SKS = data_mahasiswa[KEY]['sks_lulus']
    NAMA = data_mahasiswa[KEY]['nama']
    BEASISWA = data_mahasiswa[KEY]['beasiswa']
    LAHIR = data_mahasiswa[KEY]['lahir'].strftime("%x")

    print(f"{'KEY':<6} {'Nama':<17} {'SKS':<3} {'Beasiswa':<9} {'Lahir':<10}")