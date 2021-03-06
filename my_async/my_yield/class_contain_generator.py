# -*- coding:utf-8 -*-
from collections import deque


def student(name, homeworks):
    for homework in homeworks.items():
        yield (name, homework[0], homework[1])  # 学生"生成"作业给老师


class Teacher(object):
    def __init__(self, students):
        self.students = deque(students)

    def handle(self):
        """老师处理学生作业"""
        while len(self.students):
            student = self.students.pop()
            try:
                homework = next(student)
                print('handling', homework[0], homework[1], homework[2])
            except StopIteration:
                pass
            else:
                self.students.appendleft(student)


Teacher([
    student('Student1', {'math': '1+1=2', 'cs': 'operating system', 'chinese': 'LuXun'}),
    student('Student2', {'math': '2+2=4', 'cs': 'computer graphics'}),
    student('Student3', {'math': '3+3=5', 'cs': 'compiler construction', 'chinese': 'sanzijin'})
]).handle()
