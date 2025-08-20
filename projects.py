# print("welocome projects")
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

# 6.simple quiz application
# questions ={
#     "1.what are the python data types?" :{
#     "options": ["a) int", "b) str", "c) list","d) all of the above"],
#     "answer": "d"},

#     "2.what is the output of 2 + 2?" :{
#     "options": ["a) 3", "b) 4", "c) 5","d) 6"], 
#     "answer":"b"},

#     "3.What are the python generators?" :{
#     "options": ["a) functions that return an iterator", "b) functions that return a list", "c) functions that return a dictionary", "d) none of the above"],
#     "answer": "a"},

#     "4.python is a compiled language?" :{
#     "options": ["a) True", "b) False", "c) sometimes", "d) never"],
#     "answer": "b"},

#     "5.python is a case sensitive language?" :{
#     "options":["a) True", "b) False", "c) sometimes","d)never"],
#     "answer": "a"}

# }
# print("Welcome to the Python Quiz!🎉")

# def quiz():
#     score = 0
#     for question, q_data in questions.items():
#         print(question)
#         for option in q_data["options"]:
#             print(option)
#         answer = input("Enter your answer (a/b/c/d): ").lower()
#         if answer == q_data["answer"]:
#             print("Correct!✅\n")
#             score += 1
#         else:
#             print(f"Wrong! The correct answer is {q_data['answer']}❌.\n")
    
#     print(f"Your final score is {score}/{len(questions)}.")
#     if score >=3:
#        print("Congratulations! You passed the quiz!🎉")
#     elif score == 2:
#        print("You are almost there! Keep trying!💪")
#     elif score==5:
#          print("Wow! You are a Python expert!🏆")
#     else:
#          print("Better luck next time! Keep learning!📚")


# quiz()
# print("Thank you for playing the quiz!🙏")

# 7.Contack book(Text-file based)📖
# Contact Book (Text File Based)

# FILE = "contacts.txt"


# def add_contact():
#     name = input("Enter name: ")
#     phone = input("Enter phone number: ")
#     email = input("Enter email: ")

#     with open(FILE, "a") as f:
#         f.write(f"{name},{phone},{email}\n")
#     print("✅ Contact saved!\n")


# def view_contacts():
#     try:
#         with open(FILE, "r") as f:
#             lines = f.readlines()
#             if not lines:
#                 print("No contacts found.\n")
#                 return
#             print("\n--- Contact List ---")
#             for i, line in enumerate(lines, start=1):
#                 name, phone, email = line.strip().split(",")
#                 print(f"{i}. {name} | {phone} | {email}")
#             print()
#     except FileNotFoundError:
#         print("No contacts found.\n")


# def search_contact():
#     keyword = input("Enter name or phone to search: ").lower()
#     found = False
#     try:
#         with open(FILE, "r") as f:
#             for line in f:
#                 name, phone, email = line.strip().split(",")
#                 if keyword in name.lower() or keyword in phone:
#                     print(f"Found: {name} | {phone} | {email}")
#                     found = True
#         if not found:
#             print("No matching contact found.\n")
#     except FileNotFoundError:
#         print("No contacts found.\n")


# def delete_contact():
#     search = input("Enter name of contact to delete: ").lower()
#     updated_contacts = []
#     deleted = False

#     try:
#         with open(FILE, "r") as f:
#             for line in f:
#                 name, phone, email = line.strip().split(",")
#                 if search != name.lower():
#                     updated_contacts.append(line)
#                 else:
#                     deleted = True

#         with open(FILE, "w") as f:
#             f.writelines(updated_contacts)

#         if deleted:
#             print("✅ Contact deleted.\n")
#         else:
#             print("No contact found with that name.\n")

#     except FileNotFoundError:
#         print("No contacts to delete.\n")


# # --- Main Menu ---
# while True:
#     print("==== Contact Book ====")
#     print("1. Add Contact")
#     print("2. View Contacts")
#     print("3. Search Contact")
#     print("4. Delete Contact")
#     print("5. Exit")

#     choice = input("Enter your choice(1-5): ")

#     if choice == "1":
#         add_contact()
#     elif choice == "2":
#         view_contacts()
#     elif choice == "3":
#         search_contact()
#     elif choice == "4":
#         delete_contact()
#     elif choice == "5":
#         print("Goodbye! 👋")
#         break
#     else:
#         print("Invalid choice. Try again.\n")

# 8.Contact Book (Dictionary based)📖
# contacts = {}

# while True:
#     print("\n📘 Contact Book")
#     print("1. Add Contact")
#     print("2. View Contacts")
#     print("3. Exit")

#     choice = input("Choose an option (1-3): ")

#     if choice == "1":
#         name = input("Enter name: ")
#         phone = input("Enter phone number: ")
#         email = input("Enter email: ")
#         contacts[name] = ["phone": phone, "email": email]
#         print(f"✅ {name} added!")
    
#     elif choice == "2":
#         if contacts:
#             print("\n--- Contact List ---")
#             for name, phone in contacts.items():
#                 print(f"{name}: {phone}")
#         else:
#             print("📭 No contacts found.")
    
#     elif choice == "3":
#         print("👋 Goodbye!")
#         break
    
#     else:
#         print("❌ Invalid choice. Try again.")


# 9.Digital Clock with date&day🕒
# import tkinter as tk
# from time import strftime
# def time():
#     current_time=strftime('%H:%M:%S %p')
#     label_time.config(text=current_time)

#     current_date = strftime('%A, %d %B %Y')   
#     label_date.config(text=current_date)
#     label_time.after(1000, time)

# root = tk.Tk()
# root.title("⏰ Digital Clock")

# label_time = tk.Label(root, font=("Arial", 50, "bold"), background="black", foreground="light pink")
# label_time.pack(anchor="center")

# label_date = tk.Label(root, font=("Arial", 20), background="black", foreground="white")
# label_date.pack(anchor="center")

# time()  
# root.mainloop()







