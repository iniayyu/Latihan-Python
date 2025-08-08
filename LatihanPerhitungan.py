# celcius ke satuan lain
print("\nPROGRAM KONVERENSI TEMPERATUR\n")

celcius = float(input("masukan suhu dalam celcius :"))
print("suhu adalah ", celcius, 'celcius')

# reamur
reamur = (4/5) * celcius
print("suhu dalam reamur ", reamur, 'reamur')

# fahrenheit
fahrenheit = ((9/5) * celcius) + 32
print("suhu dalam fahrenheit ", fahrenheit, 'fahrenheit')

# kelvin
kelvin = celcius + 273
print("suhu dalam kelvin ", kelvin, 'kelvin')


# fahrenheit ke kelvin
fahrenheit = float(input("masukan suhudalam fahrenheit :"))
celcius = (9/5) * (fahrenheit - 32)
kelvin = (celcius + 273)
print("suhu dalam kelvin :", kelvin)

# kelvin ke fahrenheit
kelvin = float(input("masukan suhudalam kelvin :"))
celcius = kelvin - 273
fahrenheit = ((9/5) * celcius) + 32
print("suhu dalam fahrenheit :", fahrenheit)