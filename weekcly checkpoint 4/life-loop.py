import time
def main():

 print("Reminder to drink your daily water!")
 print("")
 person = input("do you consider yourself a sedentary person , Moderate activity person or a sportsman? ").strip().lower()
 weigth = float(input("What is your weigth(kg)? " ))

 if person == "sedentary":
   total = weigth * 30

 elif person == "moderate":
   total = weigth * 35

 elif person == "sportsman":
   total = weigth * 40

 else:
   print("that is not an option")

 print(f"you need to drink {total} ml every day " )
 print("timer is set for hour (8 total)" )
 print(f"drink {total/8} ml every hour " )


 reminder = 5

 while reminder > 0:
    print("drink water!")
    time.sleep(2)
    reminder = reminder - 1


if __name__ == "__main__":
    main()
