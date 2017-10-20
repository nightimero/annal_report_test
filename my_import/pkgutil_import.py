# -*- coding:utf-8 -*-
"""
author: tim chow<jordan23nbastar@yeah.net>
createtime: 2015-09-02 16:00
"""
# todo: how it works 2017-10-20


import pkgutil
import logging
import sys
import zipimport


def find_modules(*a, **kw):
    """ the function is used to find all modules and packages under the specific paths
    """
    for module_loader, name, _ in pkgutil.iter_modules(*a, **kw):
        if name in sys.modules:
            yield sys.modules[name]
            continue
        try:
            if isinstance(module_loader, pkgutil.ImpImporter):
                yield module_loader.find_module(name).load_module(name)
            elif isinstance(module_loader, zipimport.zipimporter):
                yield module_loader.load_module(name)
            logging.debug("succeed to import module:%s", name)
        except Exception as exc:
            logging.warn("failed to import module:%s, because:%s",
                    name, str(exc))

if __name__ == "__main__":
    import unittest
    import tempfile
    import re

    class TestFindModule(unittest.TestCase):
        def setUp(self):
            self.modules_and_packages = {t[1] for t in
                pkgutil.iter_modules()}

        def runTest(self):
            with tempfile.TemporaryFile() as tmperr:
                sys.stderr, _tmperr = tmperr, sys.stderr
                with tempfile.TemporaryFile() as tmpout:
                    sys.stdout, _tmpout = tmpout, sys.stdout
                    imported_modules = [m.__name__ for m in find_modules()]
                    sys.stdout = _tmpout
                tmperr.seek(0)
                failed_import = []
                for line in tmperr:
                    m = re.search("failed to import module:(?P<module>\w+),", line)
                    if m:
                        failed_import.append(m.group("module"))
                sys.stderr = _tmperr
                imported_modules = set(imported_modules + failed_import)
            self.assertTrue(self.modules_and_packages.issubset(
                imported_modules))
    unittest.main()
