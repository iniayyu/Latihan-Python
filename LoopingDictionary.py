teman_teman = {
    'cup':'ucup',
    'tong':'otong',
    'dung':'dudung',
    'sep':'asep',
    'cuy':'ucuy'
}

# looping yg keluar key nya
for teman in teman_teman:
    print(teman)
    
# opetaros untuk mengambil item
keys = teman_teman.keys()
print(keys)

for key in teman_teman.keys():
    print(teman_teman.get(key))
    
value = teman_teman.values()
print(value)

for value in teman_teman.values():
    print(value)
    
items = teman_teman.items()
print(items)

for item in teman_teman.items():
    print(item)
    
for key,value in teman_teman.items():
    print(f"key = {key}, value = {value}")