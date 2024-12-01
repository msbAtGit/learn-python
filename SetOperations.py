
"""
In the exercise below, use the given lists to print out a set containing
all the participants from event A which did not attend event B.
a = ["Jake", "John", "Eric"]
b = ["John", "Jill"]

"""
a = set(["Jake", "John", "Eric"])
b = set(["John", "Jill"])

print(b.difference(a))

#Other Set opertions learnt

#union
print("Union")
print(a.union(b))

#intersection
print("Intersection")
print(a.intersection(b))

# Symmetric difference i.e {a - b} union {b - a }
print("Symmetric Difference")
print(a.symmetric_difference(b))
