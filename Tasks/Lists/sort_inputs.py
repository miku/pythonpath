
user_input = input("some numbers: ")
data = user_input.split()
print(sorted(list(map(int, data))))