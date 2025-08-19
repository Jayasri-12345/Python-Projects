print("welocome projects")
#1.NUmber Guessing Game🎲

# import random
# number=random.randint(1, 50)
# attempts=0
# while True:
#     guess=int(input("Guess the number(1-50): "))
#     attempts+=1
#     if guess < number:
#         print("Too low!Try again.👇")
#     elif guess > number:
#         print("Too high!Try again.👆")
#     else:
#         print(f"Congratulations! You guessed the number {number} in {attempts} attempts.")
#         break


# 2.simple Calculator🧮

# num1= float(input("Enter first number: "))
# num2 = float(input("Enter second number: "))
# operation=input("Enter operation(+,-,*,/,**,%):")
# if operation =="+":
#     print(f"result: {num1 + num2}")
# elif operation =="-":
#     print(f"resut:{num1-num2}")
# elif operation =="*":
#     print(f"result: {num1 * num2}")
# elif operation =="/":
#     if num2 != 0:
#         print(f"Result: {num1 / num2}")
#     else:
#         print("Cannot divide by zero.")

# elif operation =="**":
#     print(f"result: {num1 ** num2}")
# elif operation =="%":
#     print(f"result: {num1 % num2}")
# else:
#     print("Invalid operation. Please try again.")


# 3.Rock,Paper,scissors Game🎮

# import random
# options = ["rock", "paper", "scissors"]
# while True:
#     user_choice = input("Enter rock, paper, scissors or 'quit' to exit: ").lower()
#     if user_choice == "exit":
#         print("Thanks for playing!🙏")
#         break
#     computer_choice = random.choice(options)
#     print(f"Computer chose: {computer_choice}")
#     if user_choice == computer_choice:
#         print("It's a tie!🤝")
#     elif (user_choice == "rock" and computer_choice == "scissors") or \
#          (user_choice == "paper" and computer_choice == "rock") or \
#          (user_choice == "scissors" and computer_choice == "paper"):
#         print("You win!🏆")
#     else:
#         print("You lose!😢")


# 4.Password Generator🔐
# import random
# import string

# def generate_password(length=8):
#     characters = string.ascii_letters + string.digits + string.punctuation
#     password = ''.join(random.choice(characters) for _ in range(length))
#     return password

# length = int(input("Enter password length: "))
# print("Generated Password:", generate_password(length))


# 5.BMI Calculator⚖️
# weight = float(input("Enter your weight (kg): "))
# height = float(input("Enter your height (m): "))

# bmi = weight / (height ** 2)
# print(f"Your BMI is: {bmi:.2f}")

# if bmi < 18.5:
#     print("You are underweight.")
# elif 18.5 <= bmi < 24.9:
#     print("You have a normal weight.")
# elif 25 <= bmi < 29.9:
#     print("You are overweight.")
# else:
#     print("You are obese.")

