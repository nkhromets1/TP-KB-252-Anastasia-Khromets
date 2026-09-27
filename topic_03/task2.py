numbers = [5, 2, 8, 1, 3]

print("Initial list: ", numbers)

numbers.append(10)
print("After append: ", numbers)

numbers.extend([7, 9])
print("After extend: ", numbers)

numbers.insert(2, 20)
print("After insert: ", numbers)

numbers.remove(8)
print("After remove: ", numbers)

numbers.sort()
print("After sort: ", numbers)

numbers.reverse()
print("After reverse: ", numbers)

new_list = numbers.copy()
print("After copy: ", new_list)

numbers.clear()
print("After clear: ", numbers)
