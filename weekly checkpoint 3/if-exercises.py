def main():
    num1 = float(input("Enter the first number : "))
    num2 = float(input("Enter the second number : "))
    operation = input("Enter the operation (add / multiply / subtract / division) : ")

    if operation == "add":
        result = num1 + num2
        print(result)
    elif operation == "multiply":
        result = num1 * num2
        print(result)
    elif operation == "subtract":
        result = num1 - num2
        print(result)
    elif operation == "division":
        result = num1 / num2
        print(result)
    else:
        print("invalid operation ")


if __name__ == "__main__":
    main()
