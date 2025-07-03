A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}

# 1. Join A and B
print("Union of A and B:", A.union(B))

# 2. Intersection of A and B
print("Intersection of A and B:", A.intersection(B))

# 3. Is A subset of B?
print("Is A subset of B?", A.issubset(B))

# 4. Are A and B disjoint?
print("Are A and B disjoint?", A.isdisjoint(B))

# 5. Join A with B and B with A
A.update(B)
print("A after joining with B:", A)

B.update(A)
print("B after joining with A:", B)

# 6. Symmetric difference between A and B (should be empty now since both are the same)
print("Symmetric difference A ^ B:", A.symmetric_difference(B))

# 7. Delete the sets completely
del A
del B
