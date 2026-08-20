def main():
 transistors = 17.8
 years = int(input("number of years:"))
 current_year = 2026

 if (current_year + years) >= 2030:
  print("The law is not valid.")
 else:
  years /= 2
  transistors *= (2**(years))
  print(f"the trasistors prediction: {transistors}")

if __name__ == "__main__":
    main()
