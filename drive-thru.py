def main():
    welcome()
    choice = int(input("Select your order:"))
    get_item(choice)


def welcome():
    menu = ["Cheesburger","Fries","Soda","Ice cream","Cookie"]

    print(f"Welcome to the restaurant!")
    print("Here's the menu :")
    for i in range(len(menu)):
        print(f"{i+1}. {menu[i]}")

def get_item(order):
    if order == 1:
        print("🍔")
    elif order == 2:
        print("🍟")
    elif order == 3:
        print("🥤")
    elif order == 4:
        print("🍦")
    elif order == 5:
        print("🍪")
    else:
        print("Sorry that is not in the menu.")



if __name__ == "__main__":
    main()
