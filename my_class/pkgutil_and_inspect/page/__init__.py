# -*- coding:utf-8 -*-
age = 12
classes = []


def deractor(cls):
    classes.append((cls.__module__, cls))
    return cls

import dialog_page
