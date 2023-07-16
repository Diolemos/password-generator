from password_generator import Password_generator

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

generator = Password_generator()

password = generator.generate_password(num_of_letters=nr_letters,num_of_numbers=nr_numbers,number_of_symbols=nr_symbols)

#print(password)
print(f"Your password is:\n{password}")
