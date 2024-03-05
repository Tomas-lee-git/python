"""
    ImportError:
        cannot import name 'mean' from partially initialized module 'statistics' (most likely due to a circular import)
        出现这个 bug，是因为我开始的时候把这个文件命名成了“statistics.py”，和 module 的名字相同，搞成循环引用，然后GG了😂

    statistics：
        mean：accept a list parameter, return an average value

"""


def main():
    get_average([1, 2, 3])


def get_average(list):
    from statistics import mean

    average = mean(list)
    print(average)
    return average


main()
