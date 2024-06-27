input_text = input("Enter string on english language: ")
count_t = 0

for char in input_text:
    if char == "t":
        count_t += 1
print(f"The number of letters \"t\" in the line \"{input_text}\" is - {count_t}\nWith use cycle 'for'.")

print(f"The number of letters \"t\" in the line \"{input_text}\" is - {input_text.lower().count("t")}\nWith use class 'string' function.")

input()