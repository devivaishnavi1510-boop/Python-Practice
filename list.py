
numbers = [10, 20, 30, 40, 50]


print("Original List:", numbers)


print("First element:", numbers[0])
print("Third element:", numbers[2])


numbers.append(60)


numbers.remove(20)


print("Updated List:", numbers)


print("List elements:")
for num in numbers:
    print(num)


total = sum(numbers)
print("Sum of elements:", total)