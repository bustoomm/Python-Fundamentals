# Penggunaan Method pada Sting
# Method capitalize, untuk merubah awalan kalimat menjadi kapital
from ast import NameConstant
from sqlite3 import apilevel


kalimat = "aku dari jakarta"
x = kalimat.capitalize ()
print (x)

# Method casefold, untuk merubah semua awalan dan huruf menjadi kecil
teks = "Aku Dari Jakarta"
y = teks.casefold
print (y)

# Method center, untuk memindahkan posisi teks ke tengah
kata = "apple"
z = kata.center
print (z)

# Method count, untuk mencari tau banyaknya string yang muncul
kaljang = "aku mempunyai mobil bmw, aku juga mempunyai pajero"
v = kaljang.count ("aku")
print (v)

# Method endswith, untuk mencari karakter khusus pada diakhir string
klmt = "Today i watch python course."
b = klmt.endswith(".")
print (b)

# Method find, untuk mencari posisi string
rsnn = "hai, how are you?"
n = rsnn.find("how")
print (n)