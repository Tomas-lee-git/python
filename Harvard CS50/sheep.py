"""
    1.
        1).range(n)函数:
            n: 数字 n，指定 list 的长度为0，内容为：0-n，不包括 n;
            return: list [0,……,n-1];

    2. generators:
        1). keyword: yield
            i. if logic wait too long, program would be "killed", no response;
            ii. use yield, can generate a little bit of data at a time not all at once;
            iii. return vs yield:
                a. in loop logic, return will do something once and quit logic;
                b. in loop logic, yield will not quit, do one iteration and yield a result;
            iii. yield is asynchronous;
    
    3. for in loop:
        1). for element in list;
        2). for key in dict;
        3). for single_str in str;
"""


def main():
    n = int(input("What's n? "))

    for s in sheep(n):  # yield will make this line be execute again and again
        print("==start==")
        print(s)
        print("==end==")


def sheep(
    n,
):  # if function inside has keyword "yield", this function will execute many times, not once;
    # flock = []
    # for i in range(n):
    #     flock.append("🐑" * (i + 1))
    # return flock

    for i in range(n):
        yield "🐑" * (i + 1)
        print("hello")


if __name__ == "__main__":
    main()
