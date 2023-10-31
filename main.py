def encode(password):
    encoded = ""
    for digit in password:
        new_digit = (int(digit) + 3) % 10
        encode += str(new_digit)
        return encode

def main():
    while True:
        print("Menu")
        print("-------------")
        print("1. Encode")
        print("2. Decode")
        print("3. Quit")
        option = input("Please enter an option:")

    if option == 1:
        encoded_pass = encode(input("Please enter a password to encode: "))
    if option == 2:
        encoded_pass = decode(encoded_pass)
        print(f'The encoded password is {encoded_pass}, and the original password is {decode(encoded_pass)}')
    if option == 3:
        break

if __name__ == "__main__":
    main()

