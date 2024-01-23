import random
import string


def password_maker(length=12):
    char = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(char) for _ in range(length))
    return password


if __name__ == "__main__":
    desired_length = int(input("Please enter the desired length of the password: "))

    if desired_length <= 0:
        print("Error: Password length should be more than 0 charaters.")
    else:
        generated_password = password_maker(desired_length)
        print(f"Here Is Your Randomly Generated Password: {generated_password}")
        print("Thank you :)")