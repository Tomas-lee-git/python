# n = print("Give me two numbers, and I will add them.")
# print("Enter 'q' to quit.")
from word_count import count_number as cn

# while True:
#     first_number = input("First number: ")
#     if first_number == "q":
#         print("Programming quits successfully.")
#         break
#     second_number = input("Second number: ")
#     if second_number == "q":
#         print("Programming quits successfully.")
#         break
#     try:
#         answer = int(first_number) + int(second_number)
#     except ValueError: # ValueError invalid literal for int() with base 10: '2sdf'
#         print("Please input number.")
#     else:
#         print(f"{first_number} + {second_number} = {answer}")

file_names = ["alice.txt", "moby_dick.txt", "siddhartha.txt", 
            "little_women.txt", "old_homeless.txt"]

for file_name in file_names:
    cn(f"./txt_files/{file_name}", "bullshit")
    cn(f"./txt_files/{file_name}", "bullshit ")