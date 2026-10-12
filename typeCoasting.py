#typeCoasting adalah mengubah tipedata ke tipe data lain
#biasanya kita kesulitan untuk coding yang menerima input, kadang jika kita meminta input integer
#user mengetikan string yang membuat program menjadi error


contoh = "17"
print(type(contoh)) #<class 'str'> tipe data str

contoh = 17
print(type(contoh)) #<class 'int'> tipe data int

contoh = 1.6
print(type(contoh)) #<class 'float'> tipe data float

#garis
garis = 55 
print("=" * garis)

#untuk output pertama tidak bisa dijumlahkan, karena bersifat string.
#output kedua bisa dijumlahkan karena dikonversi menjadi integer telebih dahulu
#pada bagian print int lalu variable bisa dijumlahkan.
print("tipe data string dijumlahkan")
a = "10"
b = "5"
print(a + b)
print(int(a)+int(b))

#garis
garis = 55 
print("=" * garis)

print("tipe data string dan integer ketika digabungkan")
a = 15
b = "10"
# print(a + b) #pasti error
print(a+int(b)) #25
#garis
garis = 55 
print("=" * garis)
print("mengubah integer menjadi string")

a = 10
b = 15
print(a + b) #25
print(str(a)+str(b)) #1015
#garis
garis = 55 
print("=" * garis)
print("studi kasus Float")

harga = 15.5
print(float(harga) + 2) #17.5
#garis
garis = 55 
print("=" * garis)
print("coba-coba")

nama = "Wildan"
umur = 24
print("Halo namaku adalah " + nama + " sekarang aku berusia " + str(umur) + " tahun")
'''Halo namaku adalah Wildan sekarang aku berusia 24tahun'''
#garis
garis = 55 
print("=" * garis)
print("Studi kasus boolean")
print(bool(5)) #True
print(bool(0))  #false
print(bool("hallo")) #true
print(bool("")) #false
#garis
garis = 55 
print("=" * garis)
print("coba-coba")
harga = "15000"
tambah = "5000"
total_harga = int(harga) + int(tambah) + 5000
print(total_harga)
#garis
garis = 55 
print("=" * garis)
print("coba-coba lagi")

harga = "15000"
total_harga = int(harga) + 5000
print("Total harga: " + str(total_harga))
#garis
garis = 55 
print("=" * garis)
print("Terakhir janji gua sumpah ")

panjang = "8"
lebar = "5"
luas = int(panjang) * int(lebar)
print("Luas persegi panjang: " + str(luas))










