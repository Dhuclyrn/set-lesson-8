a = int(input("Input for set1 "))
a2 = int(input("Input for set1 "))
a3 = int(input("Input for set1 "))
a4 = int(input("Input for set1 "))
b = int(input("input for set2 "))
b2 = int(input("input for set2 "))
b3 = int(input("input for set2 "))
b4 = int(input("input for set2 "))

set1 = {a,a2,a3,a4}
set2 = {b,b2,b3,b4}

print("Union")
print(set1 | set2)

print("Intersection")
print(set1.intersection(set2))

print("difference")
print(set1.difference(set2))

print("symmetric_difference")
print(set1.symmetric_difference(set2))


