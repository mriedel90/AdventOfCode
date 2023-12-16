my_string = "Hello, World! Hello, Universe!"
substring = "Hello"

last_index = my_string.rfind(substring)

if last_index != -1:
    print(f"The last index of '{substring}' is: {last_index}")
else:
    print(f"'{substring}' not found in the string.")