>>> gorengan = ['bakwan','cireng','tahu isi','tempe goreng','ubi goreng']
>>> for g in gorengan:
    print(g)
    print(len(g))

bakwan
6
cireng
6
tahu isi
8
tempe goreng
12
ubi goreng
10

>>> bakwan = 'bakwan'
>>> for i in bakwan:
    print(i)

    
b
a
k
w
a
n

>>> gorengan = ['bakwan','cireng','tahu isi','tempe goreng','ubi goreng']
>>> buah = ['semangka','jeruk','apel','anggur']
>>> 
>>> sayur = ['kangkung','wortel','tomat','kentang']
>>> Daftar_belanja = [gorengan,buah,sayur]
>>> for subDaftarBelanja in Daftar_belanja:
    print(subDaftarBelanja)
    for komponen in subDaftarBelanja:
        print(komponen)

        
['bakwan', 'cireng', 'tahu isi', 'tempe goreng', 'ubi goreng']
bakwan
cireng
tahu isi
tempe goreng
ubi goreng
['semangka', 'jeruk', 'apel', 'anggur']
semangka
jeruk
apel
anggur
['kangkung', 'wortel', 'tomat', 'kentang']
kangkung
wortel
tomat
kentang
