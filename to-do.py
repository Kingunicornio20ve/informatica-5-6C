def main():
    Tasks = []
    print("My to-do list")
    print("Type ´exit´ to close the program")

    while True:
        print("---Your Tasks ---")
        if  not Tasks:
            print("(No tasks yet)")
        else:
            for num, task in enumerate(tasks, 1):
                print(f"{num}. {task}")




if __name__ == "__main__":
    main()
