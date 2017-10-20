# -*- coding:utf-8 -*-
import page
import pkgutil
import inspect
modules = pkgutil.iter_modules(page.__path__, page.__name__+".",)
# iter也是不行的。
# todo：如何将一个generator变成iterable
# modules = iter(pkgutil.iter_modules(page.__path__, page.__name__+".",))
modules_name = [x[1] for x in modules if x[2] is False]
# 因为modules是个generator，尴尬了，第二次就是空的了。
modules = pkgutil.iter_modules(page.__path__, page.__name__+".",)
modules_name_short = [x[1].replace("page.", "") for x in modules if x[2] is False]

print modules_name
print modules_name_short
modules_import = []
for x in modules_name:
    modules_import.append(__import__(x, globals(), locals(), x.replace("page.", "")))
print modules_import
print modules_import[0].A().__class__

classes = []
for x in modules_import:
    classes.append((x.__name__.replace("page.", ""), (inspect.getmembers(x, inspect.isclass))))
print classes

