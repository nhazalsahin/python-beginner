# Urunler = {
#     "k500": {
#         "marka" : "iphone",
#         "fiyat" : 4500,
#         "model" : "5s"
#     },
#     "k280" : {
#         "marka" : "samsung",
#         "fiyat" : 3000,
#         "model" : "y6"
#     },
#     "k700" : {
#         "marka" : "honor",
#         "fiyat" : 2500,
#         "model" : "f5"
#     }
# }

urunler = {}
urunKod = input("Urun kodu girin:")
urunMarka = input("Urun markasini girin:")
urunFiyat = input("Urun modelini girin:")
urunModel = input("Urun fiyatini girin:")

urunler[urunKod] = {
    "Marka" : urunMarka,
    "Fiyat" : urunFiyat,
    "Model" : urunModel
}


urunKod = input("Urun kodu girin:")
urunMarka = input("Urun markasini girin:")
urunFiyat = input("Urun modelini girin:")
urunModel = input("Urun fiyatini girin:")

urunler.update({    
    urunKod: {
    "Marka" : urunMarka,
    "Fiyat" : urunFiyat,
    "Model" : urunModel
    }
   })



urunKod = input("Urun kodu girin:")
urunMarka = input("Urun markasini girin:")
urunFiyat = input("Urun modelini girin:")
urunModel = input("Urun fiyatini girin:")

urunler.update({    
    urunKod: {
    "Marka" : urunMarka,
    "Fiyat" : urunFiyat,
    "Model" : urunModel
    }
   })

print(urunler)


kod = input("Bilgilerini Öğrenmek istediğiniz Ürünün Urun Kodunu Girin : ")
ozellikler = urunler[kod]
print(ozellikler)