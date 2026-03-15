students = [
    { "name" : "HAZAL" , "age" : 29, "Grades" : [100,90,90] },
    { "name" : "YİĞİT" , "age" : 35, "Grades" : [80,50,90] },
    { "name" : "SOMEBODY" , "age" : 98, "Grades" : [10,9,0] }
]

avarage = (students[0]["Grades"][0]*0.3)+(students[0]["Grades"][1]*0.2)+(students[0]["Grades"][2]*0.5)
print(avarage)

students.append({
    "name" : "Ali", "age" : 22, "Grades": [20,30,40]
})


name = input("Öğrenci adi")
age = int(input("Öğrenci yasi")) 
g1 = int(input("Öğrenci vize puani")) 
g2 = int(input("Öğrenci quiz puani")) 
g3 = int(input("Öğrenci final puani")) 

students.append({
    "name" : name, "age" : age, "Grades" : [g1,g2,g3]
})

print(students)

students.pop(2)
print(students)
