students = {
"Hermione": "Gryffindor", #Key Hermione : Gryffindor value
"Harry": "Gryffindor", 
"Ron": "Gryffindor",
"Draco": "Slytherin"
    }
#print (students["Hermione"])
#print (students["Harry"])
#print (students["Ron"])
#print (students["Draco"])
for student in students:
    print(student) #por default iterara en las keys

for student in students:
    print(student, students[student], sep=", ") 
#Con esta sintaxis podremos imprimir ambos


