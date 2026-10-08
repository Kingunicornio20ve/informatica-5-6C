def main():

    print(" Here we Convert binary numbers to decimals")
    print("")

def binary_to_decimal(binary):
    decimal = 0
    i = 0
    while len(binary)> 0:
    digit = int(binary [-1])
    decimal += digit * (2 ** i)
    binary = binary[- 1]


    numbers = int(input("Enter the binary number :"))
    result = binary_to_decimal(numbers)


















if __name__ == "__main__":
    main()
