
try:
    while True:
        user_input = input(">>> ")
        print("ah, I see ...")
        if user_input == "q":
            break
except KeyboardInterrupt:
    print("bye")