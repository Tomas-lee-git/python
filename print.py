# 不推荐使用，但是知道 print 有这么个功能

print("wow" * 3)
# 连在一起了
# wowwowwow

print("wow\n" * 3)
# 末尾多了一个空行
"""
    wow
    wow
    wow

"""
print("wow\n" * 3, end="")
# 完美解决👍
"""
    wow
    wow
    wow
"""
