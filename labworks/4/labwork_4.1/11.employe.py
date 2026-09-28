def employee_info(**data):
    if "name" not in data:
        print("Name is missing")
    elif "department" not in data:
        print("Department is missing")
    elif "salary" not in data:
        print("Salary is missing")
    else:
        print("All details are given")

    print(data)

employee_info(name="Ravi", salary=30000)