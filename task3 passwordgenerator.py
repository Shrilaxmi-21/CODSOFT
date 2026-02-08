import random
import string
print("PASSWORD GENERATOR")

while True:
    length = int(input("\nEnter password length: "))
    print("\nChoose what to include in password:")
    print("1. Uppercase letters")
    print("2. Lowercase letters")
    print("3. Numbers")
    print("4. Symbols")

    use_upper = input("Include Uppercase? (y/n): ")
    use_lower = input("Include Lowercase? (y/n): ")
    use_numbers = input("Include Numbers? (y/n): ")
    use_symbols = input("Include Symbols? (y/n): ")

    characters = ""
    if use_upper.lower() == 'y':
        characters += string.ascii_uppercase

    if use_lower.lower() == 'y':
        characters += string.ascii_lowercase

    if use_numbers.lower() == 'y':
        characters += string.digits

    if use_symbols.lower() == 'y':
        characters += string.punctuation
    if characters == "":
        print("\nYou must select at least one character type!")
        continue
    password = ""

    for i in range(length):
        password += random.choice(characters)

    print("\nGenerated Password:")
    print(password)
    again = input("\nGenerate another password? (y/n): ")

    if again.lower() != 'y':
        print("\nThank you for using Password Generator!")
        break