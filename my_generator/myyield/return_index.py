# -*- coding:utf-8 -*-
# todo: https://www.zhihu.com/question/24807364


text ="hello ni hao"
# def index_words(text):
#     result = []
#     if text:
#         result.append(0)
#     for index,letter in enumerate(text,1):
#         # print index,letter
#         if letter ==' ':
#             result.append(index)
#     return result


# print index_words(text)


def index_words(text):
    result = []
    if text:
        yield 0
    for index,letter in enumerate(text,1):
        # print index,letter
        if letter ==' ':
            yield index


print [i for i in index_words(text)]
print sum(index_words(text))