students = [
    {"id": 101,  "name":"shinchan", "score":"72"},
    {"id": 102,  "name":"himawari", "score":"85"},
    {"id": 101,  "name":"kazama", "score":"99"}
]

for element in students:
    print(element["name"])

print()


print("Average score of all students:")
total = 0
for element in students:
    total =total + int(element["score"])
average = total / len(students)
print(average)
print()


students.append({"id": 104, "name":"nenechan", "score":"90"})
print("\nAfter adding nenechan:", students,end = "\n\n")
print()


print("Update score of student with ID 102 to 88:")




