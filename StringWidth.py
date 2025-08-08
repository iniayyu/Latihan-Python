#  Data 
data_nama = "wahyu setia"
data_umur = 18
data_tinggi = 150.1
data_sepatu = 38

data_string = f"nama = {data_nama}, umur = {data_umur}, tinggi = {data_tinggi}, sepatu = {data_sepatu}"
print(5*"="+"data string"+5*"=")
print(data_string)

# string multiline
data_string = f""" 
nama = {data_nama}
umur = {data_umur}
tinggi = {data_tinggi}
"""
print(5*"="+"data string"+5*"=")
print(data_string)

# mengatur lebar
data_string = f""" 
nama = {data_nama:>5}
umur = {data_umur:>5}
tinggi = {data_tinggi:>5}
"""
print(5*"="+"data string"+5*"=")
print(data_string)

