def find_position(numbers, new_number):
    for i in range(len(numbers)):
        if new_number <= numbers[i]:
            return i

    return len(numbers)


numbers = [1, 3, 5, 7, 9]

print("Sorted list:", numbers)

new_number = int(input("Enter new number: "))

position = find_position(numbers, new_number)

print("Position for insertion:", position)

numbers.insert(position, new_number)

print("New list:", numbers)
