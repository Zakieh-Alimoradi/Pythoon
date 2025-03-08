def binary(n):
    if n == 0:
        return "0"
    binary = ""
    while n > 0:
        binary = str(n % 2) + binary
        n = n // 2
    return binary

number = int(input("Please enter an integer number: "))
binaryy = binary(number)
print("Binary:", binaryy)