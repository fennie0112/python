print("Pattern 1:")
for i in range(1, 6):
    for j in range(1, 6):
        print("*", end=" ")
    print()


print("_________________________________")
print("Pattern 2:")
for i in range(1, 6):
    for j in range(1, i+1):
        print("*", end=" ")
    print()

print("_________________________________")
print("Pattern 3:")
for i in range(1, 6):
    for j in range(1, i+1):
        print(i, end=" ")
    print()

print("_________________________________")
print("Pattern 4:")
for i in range(1, 6):
    for j in range(1, i+1):
        print(j, end=" ")
    print()


print("_________________________________")
k = 0
print("Pattern 5:")
for i in range(1, 6):
    for j in range(1, i+1):
        print(k, end=" ")
        k += 1
    print()


print("_________________________________")
print("Pattern 6:")
for i in range(1, 6):
    for j in range(1, i+1):
        if j % 2 == 0:
            print(0, end=" ")
        else:
            print(1, end=" ")
    print()


print("_________________________________")
print("Pattern 7:")
for i in range(1, 6):
    for j in range(1, i+1):
        if i % 2 == 0:
            print(0, end=" ")
        else:
            print(1, end=" ")
    print()



print("_________________________________")
print("Pattern 8:")
k = 1
for i in range(1, 6):
    for j in range(1, i+1):
        if i % 2 != 0:
            print(k, end=" ")
            k += 1
        else:
            print("*", end=" ")
    print()



print("_________________________________")
print("Pattern 9:")
k = 1
for i in range(0, 6):
    for j in range(0, i+1):
        if i==j:
            print("0", end=" ")
        else:
            print(i, end=" ")
    print()



print("_________________________________")
print("Pattern 10:")
for i in range(0, 6):
    k = 0
    for j in range(0, i+1):
            print(5-k, end=" ")
            k += 1
    print()


print("_________________________________")
print("Pattern 11:")
for i in range(5,0,-1):
    for j in range(i,6):
            print(j, end=" ")
    print()


print("_________________________________")
print("Pattern 12:")
for i in range(1,6):
    for j in range(1,i+1):
            print(i, end=" ")
    print()
for i in range(4,0,-1):
    for j in range(i,0,-1):
            print(i, end=" ")
    print()




