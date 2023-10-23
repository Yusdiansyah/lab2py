# input nilai variabel
a=input("Masukan nilai a:")
b=input("Masukan nilai b:")

# cetak nilai variabel
print("variabel a=",a)
print("variabel b=",b)

# cetak hasil operasi kedua variabel dengan string format
print("Hasil penggabung {}&{}={}".format(a,b,a+b))

# konversi nilai variabel
a=int(a)
b=int(b)
print("Hasil penjumlahan {}+{}={}".format(a,b,a+b))
print("Hasil pembagian {}/{}={}".format(a,b,a/b))