import random
import string

def password_generator(length):
    password_char = []
    password_char.append(random.choice(string.ascii_lowercase))
    password_char.append(random.choice(string.ascii_uppercase))
    password_char.append(random.choice(string.digits))
    password_char.append(random.choice(string.punctuation))

    
    all_char = string.ascii_lowercase + string.ascii_uppercase + string.digits + string.punctuation
    password_char.extend(random.choice(all_char))
    random.shuffle(password_char)

    password = "".join(random.choice(password_char) for i in range(length))
    return password

print()

def main():

    
    try:
        length = int(input("Enter the length of password: "))

        print()

        if length <= 0 :
            print("Length must be a 'positive number'")
    
        if length < 4:
            print("Length must be atleast of 4 digits to contain 4 different characters")
        if length >= 4:
            print("Valid length to generate the password.")
            print()
            print("Your New Password: ")
            new_password = password_generator(length)
            print(new_password)
            print()
    except ValueError as ve:
        print(f"invald input, {ve}")
    
if __name__ == "__main__":
    main()
          




            

