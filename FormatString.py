# format string

# contoh generik
nama= "ayyu"
format_str = f"hello {nama}"
print(format_str)

# angka
angka = 2006.6
format_str = f"angka = {angka}"
print(format_str)

# boolean
boolean = True
format_str = f"boolean = {boolean}"
print(format_str)

# bilangan bulat
angka = 15
format_str = f"bil bulat = {angka:d}"
print(format_str)

# bilangan ribuan
angka = 2000000
format_str = f"jutaan {angka:,}"
print(format_str)

angka = 2006.6452
format_str = f"desimal = {angka:.2f}"
print(format_str)

# menampilkan leading zero
angka = 2006.645297
format_str = f"desimal = {angka:010.3f}"
print(format_str)

# menampilkan tanda + atau -
angka_minus = -10
angka_plus = +10.123
format_minus = f"minus = {angka_minus:+d}"
format_plus = f"plus = {angka_plus:+.2f}"

print(format_plus)
print(format_minus)

# memformat persen
persentase = 0.045
format_persen = f"persen = {persentase:.2%}"
print(format_persen)

# melakukan operasi aritmatika
harga = 10000
jumlah = 5

format_string = f"harga total = Rp. {harga*jumlah:,}"
print(format_string)

# format angka lain
angka = 225
format_binary = f"binary = {bin(angka)}"
format_octal = f"octal = {oct(angka)}"
format_hex = f"hex = {hex(angka)}"

print(format_binary)
print(format_octal)
print(format_hex) 