user_input_1 = input("Enter Text to write to the fill: ")
with open("output.txt", "w") as file:
    file.write(user_input_1 + "\n")

print("Data Successfully writen to "'output.txt')

user_input_2 = input("\nEnter additional text to append: ")
with open("output.txt", "a") as file:
    file.write(user_input_2 + "\n")

print("Data Successfully appended")

print("\nFinal content of"'output.txt')
with open("output.txt", "r") as file:
    final_content = file.read()
    print(final_content)