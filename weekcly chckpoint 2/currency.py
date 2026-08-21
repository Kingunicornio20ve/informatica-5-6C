def main():
    p = float(input("What do you have left in pesos?: "))
    s = float(input("What do you have left in soles?: "))
    r = float(input("what do you have left in reais?: "))

    mxn = (p * 0.0054) + (s * 5.07) + (r * 3.28)
    usd = mxn / 17.06

    print("USD:", round(usd, 2))
    print("MXN:", round(mxn, 2))

if __name__ == "__main__":
    main()


