"""
    对同一个 variable 进行边界判断时，and 可以省略掉
        if score <= 100 and score >= 90:
        if 90 <= score <=100:
"""

score = int(input("What's your score? "))

# 版本1

# 90-100, A
if score <= 100 and score >= 90:
    print("Score: A")
# 80-89, B
elif score < 90 and score >= 80:
    print("Score: B")
# 70-79, C
elif score < 80 and score >= 70:
    print("Score: C")
# 60-69, D
elif score < 70 and score >= 60:
    print("Score: D")
# 60 以下, E
else :
    print("Score: E")

# 版本2

# 90-100, A
if 90 <= score <=100:
    print("Score: A")
# 80-89, B
elif 80 <= score < 90:
    print("Score: B")
# 70-79, C
elif 70 <= score < 80:
    print("Score: C")
# 60-69, D
elif 60 <= score < 70:
    print("Score: D")
# 60 以下, E
else :
    print("Score: E")


# 版本3

# 90-100, A
if 90 <= score:
    print("Score: A")
# 80-89, B
elif 80 <= score:
    print("Score: B")
# 70-79, C
elif 70 <= score:
    print("Score: C")
# 60-69, D
elif 60 <= score:
    print("Score: D")
# 60 以下, E
else :
    print("Score: E")
