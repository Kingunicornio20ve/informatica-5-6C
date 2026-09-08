import time
def main():

 print("Reminder to drink your daily water!")
 print("")
 person = input (" Do you consider yourself a sedentary person ,Moderate activity person or a sportsman?).strip().lower()
 weigth = float(input("What is your weigth? " ))

 if person == "sedentary":
  total = weigth * 30

 elif person == "moderate":
  total = weigth * 35
 elif person == "sportsman":
  total = weigth * 40

  print(f"you need to drink {total} ml every day ")
  


 else:
  print("that is not an option")



 reminder = 5

 while reminder > 0:
    print("drink water!")
    time.sleep(2)
    reminder = reminder - 1






if __name__ == "__main__":
    main()
