number = int(input("Enter a number: "))
binary = bin(number)[2:]
zeros = binary.count("0")
ones = binary.count("1")
print(f"\nBinary of {number} is: {binary}")
print(f"Number of 1s: {ones}")
print(f"Number of 0s: {zeros}")