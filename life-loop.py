import time
def main():

 print("Reminder to drink your daily water!")
 print("")
  person = input (" Do you consider yourself a sedentary person ,Moderate activity person or a sportsman?)
 weigth = float(input("What is your weigth? " ))

 reminder = 5

 while reminder > 0:
    print("drink water!")
    time.sleep(10)
    reminder = reminder - 1






if __name__ == "__main__":
    main()
