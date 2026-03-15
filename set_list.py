fruits = {"apple","banana","orange"}
#set listelerinde indexe ulaşılamaz,sıralanamaz
# fruits.add("cherry") #tek meyve eklenebilir
fruits.update(["peach", "grape"])
fruits.remove("apple")
fruits.discard("banana")
fruits.pop()  #herhangi bir elemanı siler.
# print(fruits)

numbers = {1,1,421,434,56,7777,7,7,45,45,22,355,6,6,421}
print(type(numbers))
print(sorted(numbers))
print(sorted(set(numbers)))
