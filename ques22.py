my_list = [1, 2, 3, 2, 4, 3, 5]

seen = set()
duplicates = set()

for i in my_list:
    if i in seen:
        duplicates.add(i)
    else:
        seen.add(i)

print("Duplicates:", duplicates)