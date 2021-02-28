str = "AppliedCourse"

unique = {}
for i in str:
    unique[i] = unique.get(i, 0) + 1

# print(unique)

newString = ''.join(unique.keys())
print(newString)
