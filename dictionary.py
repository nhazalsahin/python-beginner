# # key-value(sehir-plaka)

# sehirler = ["istanbul", "ankara"]
# plakalar = [34,6]
# # ***********************************************************************************************
# plakalar = {"istanbul" : 34, "ankara" : 6}   #print(plakalar[sehirler.index("istanbul")]) bununla aynı işi görür
# print(type(plakalar))
# print(plakalar["istanbul"])
# print(plakalar["ankara"])

# # ****dictionary list'e eleman ekleme****
# plakalar["ordu"] = 52
# print(plakalar)
# #*****************************************

kullanicilar = {
    "Hazal Şahin" : {
        "age" : 29,
        "e-Posta" : "nhazalsahin@gmail.com",
        "meslek" : ["yazilim","fizyoterapist"]
    },
    "Yigit Gün" : {
        "age" : 35,
        "e-Posta" : "ygtgn@gmail.com",
        "meslek" : ["iç mimar","insan kaynaklari"]
    }
}
# print(kullanicilar["Hazal Şahin"]["age"])
# print(kullanicilar["Hazal Şahin"]["meslek"][0])
print(kullanicilar["Yigit Gün"]["e-Posta"])

