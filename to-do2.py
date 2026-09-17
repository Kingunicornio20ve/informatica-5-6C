def main():
    #fruits = ["apple", "banana","cherry"]
   # print("banana" in fruits)

   tasks = []

   while True:
       print(f"tasks to do: {len(tasks)}")
       print(tasks)

       new_task = input("Enter task: ").capitalize().strip()
       if new_task == "Exit":
           break
       elif new_task not in tasks:
           tasks.append(new_task)
       elif new_task in task:
           del_confirm = input(f"Did you completed {new_task}? (y/n):").lower().stip()
           if del_confirm == "y":
            tasks.remove(new_task)
           else:
            continue





if __name__ == "__main__":
    main()
