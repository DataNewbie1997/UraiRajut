def urai(text):
    akhir =  ''                         # akhir harus '' karena nanti akan ditambahkan alphabet
    for item in range (len(text)):      # ini untuk memastikan ketika diprint sesuai dengan len(text)
        item
        for item2 in range (0,item+1):  # harus ditambah 1 agar bisa diprint sampai len(text) berakhir
            akhir = akhir + text[item2] # kalau tidak ditambah dengan kosong maka akan keprint huruf akhirnya saja
    # print('ini akhir:',akhir)
    return akhir
print(urai('Code'))
print(urai('Python'))
print(urai('Purwadhika'))

def rajut(text):
    akhir1 = ''
    index = 1 
    counter = 2
    while index <= (len(text)):
        akhir1 = akhir1 + text[index-1]
        index = index + counter
        counter = counter + 1
    return akhir1 
print(rajut('CCoCodCode'))