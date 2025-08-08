import datetime as dt

print("silahkan masukan tanggal, bulan dan tahun lahir anda")
tanggal = int(input("tanggal \t:"))
bulan = int(input("bulan \t\t:"))
tahun = int(input("tanggal \t:"))

tanggal_lahir = dt.date(tahun,bulan,tanggal)

hari_ini = dt.date.today()
print(f"hari ini tanggal :{hari_ini}")
umur_hari = hari_ini - tanggal_lahir
umur_tahun = umur_hari.days // 365
umur_bulan_sisa = (umur_hari.days % 365) // 30
print(f"tangal lahir anda adalah :{tanggal_lahir:%A}")
print(f"umur anda adalah : {umur_tahun} tahun, {umur_bulan_sisa} bulan")