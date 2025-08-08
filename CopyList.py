# teknik menduplikat list
a = ["ayyu", "lala", "donat", "gege"]
print(f"a = {a}")

b = a
print(f"b = {b}")

# merubah member dari a
a[1] = "qiah"
b.sort()
print(f"a = {a}")
print(f"b = {b}")

# address dari kedua list a dan b
print(f"address a = {hex(id(a))}")
print(f"address b = {hex(id(b))}")

# menduplikasi list dengan copy
print("membuat list c dengan a.copy()")
c = a.copy()

print(f"address a = {hex(id(a))}")
print(f"address b = {hex(id(b))}")
print(f"address c = {hex(id(c))}")

print(f"a = {a}")
print(f"b = {b}")
print(f"c = {c}")

print("kita ubah data 0")
c[0] = "rose"

print(f"a = {a}")
print(f"b = {b}")
print(f"c = {c}")

print("kita ubah data 1")
c[1] = "mawar"

print(f"a = {a}")
print(f"b = {b}")
print(f"c = {c}")