import random

print("Password Generator")

characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*().,:"

number_of_passwords = input("Amount of passwords to generate: ")
number_of_passwords = int(number_of_passwords)

password_length = input("Length of password: ")
password_length = int(password_length)

print("\n Passwords generated:")

for pwd in range(number_of_passwords):
    passwords = ""
    for c in range(password_length):
        passwords += random.choice(characters)
    print(passwords)
