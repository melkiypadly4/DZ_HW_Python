from random import randint
 
lo, hi = 3, 8
data = [randint(1, 10) for _ in range(20)]
print("Original array:", data, sep='\n')
indexes = [i for i, v in enumerate(data) if lo <= v <= hi]
print("Indexes:", indexes, sep='\n')
result = []
i = len(indexes)
while i :
    i -= 1
    result.append(data.pop(indexes[i]))
print("Remaining elements:", data, sep='\n')
print("Required elements:", result, sep='\n')