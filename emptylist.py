
numbers = []


for i in range(5):
    num = int(input("Enter a number: "))
    numbers.append(num)


print("List:", numbers)


largest = max(numbers)

print("Largest number in the list is:", largest)