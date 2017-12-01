# -*- coding: utf-8 -*-
import unittest
import errno


# A simple function to illustrate
def parse_int(s):
    return int(s)


class TestConversion(unittest.TestCase):
    def test_bad_int(self):
        # self.assertRaises(KeyError, parse_int, 'N/A')
        self.assertRaises(ValueError, parse_int, 'N/A')


class TestIO(unittest.TestCase):
    def test_file_not_found(self):
        try:
            f = open('/file/not/found')
        except IOError as e:
            print e.errno
            print e
            self.assertEqual(e.errno, errno.ENOENT)

        else:
            self.fail('IOError not raised')


if __name__ == '__main__':
    unittest.main()
    parse_int('N/A')  # 执行了unittest.main之后不会执行其他代码，应该是执行了sys.exit()
