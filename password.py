import random
import string

def generate_password(length=12, use_upper=True, use_lower=True, use_digits=True, use_symbols=True):
    chars = ''
    if use_upper:
        chars += string.ascii_uppercase
    if use_lower:
        chars += string.ascii_lowercase
    if use_digits:
        chars += string.digits
    if use_symbols:
        chars += string.punctuation
    if not chars:
        return "Error: No character types selected!"

    password = ''.join(random.choice(chars) for _ in range(length))
    return password

def get_user_choices():
    length = int(input("\nEnter length of the password: "))
    use_upper = input("Want to include uppercase letters? (y/n): ").lower() == 'y'
    use_lower = input("Want lowercase letters? (y/n): ").lower() == 'y'
    use_digits = input("Want to include numbers? (y/n): ").lower() == 'y'
    use_symbols = input("Want to include special characters? (y/n): ").lower() == 'y'
    return length, use_upper, use_lower, use_digits, use_symbols

print("=" * 40)
print("     Secure Password Generator")
print("=" * 40)

while True:
    length, u, l, d, s = get_user_choices()
    print("\nGenerated Password:")
    print(f">>> {generate_password(length, u, l, d, s)}")
    again = input("\nWould you like to generate another password? (y/n): ").lower()
    if again != 'y':
        print("\nThank you for using Password Generator!")
        break
