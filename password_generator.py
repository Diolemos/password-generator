import random

class Password_generator():
    def __init__(self) -> None:
        self.LETTERS = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
        self.NUMBERS = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        self.SYMBOLS = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
        
    def generate_password(self,num_of_letters=5,num_of_numbers=3,number_of_symbols=3):
            letters = random.choices(self.LETTERS, k=num_of_letters)
            print(letters)
            # for _ in range(int(num_of_letters)):
            #      random_letter = random.choice(self.LETTERS)
            #      letters.append(random_letter)
            numbers = random.choices(self.NUMBERS,k=num_of_numbers)       
            print(numbers)
            # for _ in range(int(num_of_numbers)):
            #     random_number = random.choice(self.NUMBERS)
            #     numbers.append(random_number)
            symbols = random.choices(self.SYMBOLS, k=number_of_symbols)
            print(symbols)
            # for _ in range(int(number_of_symbols)):
            #     random_symbol = []
            #     random_symbol = random.choice(self.SYMBOLS)
            #     symbols.append(random_symbol)
            password = letters + numbers + symbols
            random.shuffle(password)
            # print(password)
            return password      