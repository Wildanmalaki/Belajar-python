'''Function atau bisa disebut fungsi adalah sebuah blok kode yang dibuat
   untuk dipakai berulang kali, jadi kaya semacam preset yang tinggal siap digunakan.
'''

#garis
lebar = 55
print("=" * lebar)
print("WIldan sedang belajar Function hehe".center(lebar))
print("=" * lebar)

print("studi kasus")
def sapa():
    print("halo!")
    print("Saat ini saya sedang belajar function!")

sapa() #jadi tinggal manggil saja variabnelnya
sapa()
'''
output: Saat ini sedang belajar function!
'''
#garis
print("=" * lebar)
print("coba-coba".center(lebar))
print("=" * lebar)
def perkenalan():
    print("Namaku adalah Wildan Malaki")
    print("Aku lahir di Jakarta Timur")
print("Perkenalkan sebelumnya!")
perkenalan()
perkenalan()
print("Terima kasih!")

#garis 
print("=" * lebar)
print("Menambahkan Parameter pada function".center(lebar))
print("Studi kasus".center(lebar))
print("=" * lebar)

def sapa(nama):
    print("Halo, " + nama)
sapa("wildan")
sapa("ucok")

#garis 
print("=" * lebar)
print("Praktek coba".center(lebar))
print("=" * lebar)

def umur_depan(umur):
    print("Tahun depan umurku " + str(umur + 1))

print("alhamdulilah, aku diberi panjang umur..")
umur_depan(24)

#garis 
print("=" * lebar)
print("Menambahkan 2 parameter pada function")

def jumlah(a,b):
    print(a + b)

jumlah(5,10) #15

#garis 
print("=" * lebar)
print("praktik coba-coba")

def luas(panjang, lebar):
    luas_persegi = (panjang * lebar )
    print("Luas persegi panjang adalah: " + str(luas_persegi))

luas(8,5)
luas(10,3)

#garis 
print("=" * lebar)
print("menambahkan return".center(lebar))
print("=" * lebar)
'''Return berfungsi untuk mengembalikan nilai hasil dari function ke keluar'''
print("Contoh..")
def kali(a, b):
    return(a * b)

hasil = kali(1,5)
print(hasil)

#garis
print("=" * lebar)
print("Belajar return".center(lebar))
print("=" * lebar)

def tambah(a,b):
    return(a + b)

hasil_tambah = tambah(5, 10)
print(hasil_tambah)
print(hasil_tambah + 1)
print(hasil_tambah + 20)

#garis
print("=" * lebar)
print("Latihan return".center(lebar))
print("=" * lebar)

def tambah(a,b):
    return a + b

total = tambah(5,10)
print("Hasil dari function adalah:" + str(total))
print("hasil dari function dikalikan 2 adalah: " + str(total * 2))

#garis
print("=" * lebar)
print("Latihan lagi biar jago".center(lebar))
print("=" * lebar)

def luas(panjang, lebar):
    return panjang * lebar

hasil = luas(8,5)
print("Luas persegi panjang: " + str(hasil))