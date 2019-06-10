# _*_ coding:utf-8 _*_
"""
author:Bevishe
date:2019-06-04
"""

# def goodBye(f):
#     def f2():
#         print("goodBye")
#         return f()
#     return f2
#
#
# @goodBye
# def hello():
#     print("hello")
#
# hello()
def goodBye(f):
    def f2():
        print("goodBye")
        return f()

    return f2


def hello():
    print("hello")


hello = goodBye(hello)
hello()