# Open file in write mode
file = open("names.txt", "w")

print("Enter 5 names:")


for i in range(5):
    name = input()
    file.write(name + "\n")

file.close()


file = open("names.txt", "r")

print("\nNames stored in file:")


for line in file:
    print(line.strip())

file.close()