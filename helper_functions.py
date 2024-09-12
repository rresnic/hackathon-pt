def get_valid_input(prompt, valid):
    while True:
        user_input = input(prompt)
        if user_input in valid:
            return user_input
        else:
            print("Invalid input.")