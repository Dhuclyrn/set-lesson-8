import time
import random
numbers = []
for i in range(15):
    numbers.append(random.randint(1,5))
print(type(numbers))
time.sleep(0.5)
print(numbers)
time.sleep(0.5)


sample_set = set(numbers)
time.sleep(0.5)
print(type(sample_set))
time.sleep(0.5)
print(sample_set)
time.sleep(0.5)


if 100 in sample_set:
    print("yeigh")
else:
    print("neigh")

mySet = set([])
mySet.add(100)
mySet.add(200)
mySet.add(300)
mySet.add(400)
mySet.add(500)
time.sleep(0.5)
print(mySet)

mySet.remove(200)
time.sleep(0.5)
print(mySet)

#mySet.remove(700)
#time.sleep(0.5)
#print(mySet)

#remove will throw error, if the element isnt present in the set

mySet.discard(700)
time.sleep(0.5)
print(mySet)

#Discard wont throw error, even if the umber doesnt exist in the set

#Set operations
#1) Union
#2) Intersection
#3) Difference
#4) Symmetric Difference

a = {1,2,3,4,5}
b = {4,5,6,7,8}
print("union of two sets")
print(a.union(b))
print(a | b)

time.sleep(0.5)

print("intersection of two sets")
print(a.intersection(b))
print(a & b)

time.sleep(0.5)

print("difference of a and b")
print(a.difference(b))
print(a-b)

time.sleep(0.5)

print("difference of b and a")
print(b.difference(a))
print(b-a)


time.sleep(0.5)

print("symmetric difference")
print(a.symmetric_difference(b))
print(a^b)