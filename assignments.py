numbers = 1,2,3
x,y,z = numbers
print(x,y,z)  # x=1 y=2 z=3  değer  sayısı ile değişken sayısı eşit olmalı

numbers= 1,2,3,4,5,6,7,8,9
x,*y,z = numbers

print(x,y,z) # x ilk z son değeri alır ve y ortada kalan tüm değerleri alır
# x=1
# y=[2,3,4,5,6,7,8]
# z=9
