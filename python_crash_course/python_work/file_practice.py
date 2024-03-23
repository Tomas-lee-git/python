from pathlib import Path

path = Path("txt_files/learning_python.txt")
contents = path.read_text()
# print(f"learning_python.txt has {len(contents.splitlines())} lines.")
for line in contents.splitlines():
    # print(f"line content is {line}")
    ...

# print("==============")
for line in contents.splitlines():
    line_replace_with_c = line.replace("Python", "C")
    # print(f"line content is {line_replace_with_c}")

names = ""
while True:
    name = input("Please input your name: ")
    print("You can input 'quit' or 'q' to stop it!")
    if name == "quit" or name == "q":
        break
    else:
        names += f"{name.title()}\n"

guest_path = Path("./txt_files/guest.txt")
guest_path.write_text(names)
