a,b,c =3,9,7
numbers = 9,8,5,3,2,4

sayi1 = int(input("Lutfen bir sayi giriniz"))
sayi2 = int(input("Lutfen bir sayi giriniz"))
carpim = sayi1*sayi2
print("Çarpim sonucu: ",carpim)
toplam = a+b+c
print("toplam sonucu: ",toplam)

fark = carpim-toplam
print("fark sonucu: ",fark)

kalansiz=c//a
print("kalansiz bölüm sonucu: ",kalansiz)

mod=(a+b+c)%5
print("mod sonucu: ",mod)

kuvvet = a**b
print("kuvvet sonucu: ",kuvvet)

a,*b,c = numbers
kup= c**3
print("kup sonucu: ",kup)
print(b[0]+b[1]+b[2]+b[3])



