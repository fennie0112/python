student = {
    "name": "Fennie",
    "age": 17,
    "grade": "A"
}

print(student.keys())
print(student.values())
student["city"] = "Rajkot"
student["age"] = 18
del student["grade"]
print(student)