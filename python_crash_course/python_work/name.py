message = "I told my friend:'Python is my favorite language!'"
name = "The language 'Python' is named after Monty Python, not the snake."
strength = "One of Python's strengths is its diverse and supportive community"

# upper and lower
title_message = message.title()
upper_name = name.upper()
lower_strength = strength.lower()
# print(title_message)
# print(upper_name)
# print(lower_strength)

# format str "f{variable}"
first_name = "ada"
last_name = "lovelace"
full_name = f"{first_name} {last_name}".title()
greeting_message = f"Hello, {full_name}!"
# print(greeting_message)

# /t、/n
# print("Python")
# print("\tPython")
# print("Python\n")
# print("\tPython\n")
new_and_tab = "\n\t"
# print(f"Languages:{new_and_tab}Python{new_and_tab}C{new_and_tab}JavaScript")

# remove whitespace
favorite_language = " python "
favorite_language_rstrip = favorite_language.rstrip()
# print(favorite_language_rstrip)
favorite_language_lstrip = favorite_language.lstrip()
# print(favorite_language_lstrip)
favorite_language_strip = favorite_language.strip()
# print(favorite_language_strip)

# remove prefix、suffix
nostarch_url = "https://nostarch.com.cn"
no_prefix_url = nostarch_url.removeprefix("https://")
# print(no_prefix_url)
no_suffix_url = nostarch_url.removesuffix(".cn")
# print(no_suffix_url)