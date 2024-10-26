def continuous_input():
    while True:
        user_input = input("Enter a word (or 'exit' to quit): ")
        if user_input.lower() == "exit":
            break
        print(user_input)

continuous_input()