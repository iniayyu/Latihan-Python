list_buku = []
while True:
    print("\nMasukan data buku")
    judul = input("masukan judul buku\t:")
    penulis = input("masukan nama penulis\t:")

    buku_baru = [judul,penulis]
    list_buku.append(buku_baru)
    
    print("\n\n","="*10,"Data Buku","="*10)
    for index,buku in enumerate(list_buku):
        print(f"{index+1} |  {buku[0]} |   {buku[1]}")

    print("\n\n","="*20)
    isiLanjutan = input("Apakah dilanjutkan?(y/n) ")
    
    if isiLanjutan == "n":
        break
    
print("program selesai")
    

