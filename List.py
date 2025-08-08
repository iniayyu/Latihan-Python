# kumpulan data number
data_angka = [1,2,3]
print(data_angka)

# kumpulan data string
data_string = ["ayu", "lala", "lili"]
print(data_string)

# kumpulan data boolean
data_boolean = [True, False, True, False]
print(data_boolean)

# kumpulan campuran
data_campuran =[1, "lala", 2, "ayyu"]
print(data_campuran)

# cara membuat list alternatif
data_range = range(0,10,2)
print(data_range)
data_list = list(data_range)
print(data_list)

# membuat list pakai for loop, list comperhesion
list_pake_for = [i**2 for i in range(0,10)]
print(list_pake_for)

# list pake for pake if
list_pake_for_if = [i for i in range(0,10) if i != 5]
print(list_pake_for_if)

list_pake_for_if = [i for i in range(0,10) if i%2 == 0]
print(list_pake_for_if)

list_pake_for_if = [i**2 for i in range(0,10) if i%2 != 0]
print(list_pake_for_if)

