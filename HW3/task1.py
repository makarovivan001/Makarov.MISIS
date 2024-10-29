classes = {7: [], 8: [], 9: []}
students = [
    "7 Ivanov",
    "8 Petrov",
    "9 Sidorov",
    "7 Grigoryev",
    "7 Sergeev",
    "8 Yakovlev"
]
for el in students:
    class_number, surname = el.split()
    class_number = int(class_number)
    classes[class_number].append(surname)

for class_number in range(7, 10): 
    for surname in classes[class_number]:
        print(class_number, surname)