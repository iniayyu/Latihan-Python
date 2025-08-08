# operator dictionary
data_dict = {
    'cup':'cupcup',
    'tong':'tongtong',
    'dung':'dudung'
}

# panjang dictionary
lendict = len(data_dict)
print(f"Panjang dictionary : {lendict}")

# mengecek key exist atau tidak
key = 'cup'
check = key in data_dict
print(f'apakah {key} ada di data_dict: {check}')

# mengakses value (read) dengan get
print(data_dict["cup"])
print(data_dict.get("cup"))
print(data_dict.get("kis","key tidak ditemukan")) #dengan message box

# mengupdate
data_dict["cup"] = "ucup si ganteng"
print(data_dict)
data_dict["sep"] = "asep si kasep"
print(data_dict) 

data_dict.update({"cup":"ucup sururcup"})
print(data_dict)
data_dict.update({"ayy":"ayyu yu yu"})
print(data_dict)

# mendelete data 
del data_dict["cup"]
print(data_dict)