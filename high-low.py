def main():
    def highest(a,b):
        if a > b:
            highest_num = a
        else:
            highest_num  = b
        print(f"The highest number entered is {highest_num}")

    highest(8, 2)

    num1 = int(input("Enter a number:"))
    num2 = int(input("Enter another number:"))
    highest_num(num1, num2)


    def lowest(a , b, c):
        if a < b and a < c:
            lowest_num = a
        elif b < a and b < c:
            lowest_num = b
        else:
            lowest_num = c
        print(f"The lowest number entered is {lowest_num}")

    lowest(8, 2, 5)










if __name__ == "__main__":
    main()
