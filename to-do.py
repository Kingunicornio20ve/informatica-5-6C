def main():
    tasks = []
    while True:
        print(f"You have {len(tasks)} tasks to do. ")
        print(tasks)
        command = input("What do you want to do? (add,complete, change task to position 1, or stop): ").lower()
        if command == "add":
            new_task = input("Enter a new task: ")
            tasks.append(new_task)
        elif command == "change task to position 1":
            changed_task = input("Enter task: ")
            tasks.insert(0, changed_task)
            tasks.remove(changed_task)
        elif command == "stop":
            break

if __name__ == "__main__":
    main()
