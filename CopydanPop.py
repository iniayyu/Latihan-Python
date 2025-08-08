# copy dicitionary
teman_teman = {
    'cup':'ucup',
    'tong':'otong',
    'dung':'dudung',
    'sep':'asep',
    'cuy':'ucuy'
}

friends = teman_teman.copy()

print(f"teman-teman : {teman_teman}\n")
print(f"friends : {friends}\n")

teman_teman["cup"]='ucup si ucup'
print(f"teman-teman : {teman_teman}\n")
print(f"friends : {friends}\n")

# pop dictionary (berdasarkan key)
dataAsep = friends.pop('sep')
print(f"data asep = {dataAsep}\n")
print(f"friends = {friends}\n")

# popitem dictionary (yang terakhir saja)
dataTerakhir = friends.popitem()
print(f"data terakhir = {dataTerakhir}\n")
print(f"friends = {friends}\n")