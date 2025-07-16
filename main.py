import random
import string
def generate_password(min_length, numbers=True, special_characters=True):
    letters = string.ascii_letters
    digits = string.digits
    special = string.punctuation

    characters = letters
    if numbers:
        characters += digits
    if special_characters:
        characters += special

    pwd = ""
    meets_criteria = False
    has_number = False
    has_special = False

    while not meets_criteria or len(pwd) < min_length:
        new_char = random.choice(characters)
        pwd += new_char
        if new_char in digits:
            has_number = True
        if new_char in special:
            has_special = True

        meets_criteria = True
        if numbers:
            meets_criteria = has_number
        if special_characters:
            meets_criteria = has_special and meets_criteria

    return pwd
min_length = int(input("Enter minimum password length: "))
has_numbers = input("Include numbers? (yes/no): ").strip().lower() == 'y'
has_special = input("Include special characters? (yes/no): ").strip().lower() == 'y'
print(generate_password(min_length, has_numbers, has_special))
# The following code was previously used for password generation but has been refactored.
# It is commented out to avoid confusion with the new implementation.



# import random
# import string

# def generate_password(min_length, numbers = True, special_characters = True):
#     letters = string.ascii_letters
#     digits = string.digits
#     special = string.punctuation

#     characters = letters
#     if numbers:
#         characters += digits
#     if special_characters:
#         characters += special

#     pwd = ""
#     meets_criteria = False
#     has_number = False
#     has_special = False

#     while not meets_criteria or len(pwd) < min_length:
#         new_char = random.choice(characters)
#         pwd += new_char
#         if new_char in digits:
#             has_number = True
#         if new_char in special:
#             has_special = True

#         meets_criteria = True
#         if numbers:
#             meets_criteria = has_number
#         if special_characters:
#             meets_criteria = has_special and meets_criteria

#     return pwd
# min_length = int(input("Enter minimum password length: "))
# has_numbers = input("Include numbers? (yes/no): ").strip().lower() == 'y'
# has_special = input("Include special characters? (yes/no): ").strip().lower() == 'y'


# print(generate_password(12, has_numbers, has_special))
