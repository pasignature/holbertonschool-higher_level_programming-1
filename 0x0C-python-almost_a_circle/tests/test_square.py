#!/usr/bin/python3
"""UnitTest Module Sqaure"""

import unittest
import doctest
import pep8
from models import square
from models.square import Square as s


class TestBase(unittest.TestCase):
    """Class Test Base"""

    def test_square_class(self):
        """Test Square Class"""

        pep8style = pep8.StyleGuide(quiet=True)
        result1 = pep8style.check_files(['models/square.py'])
        result2 = pep8style.check_files(['tests/test_square.py'])
        self.assertEqual(result1.total_errors, 0)
        self.assertEqual(result2.total_errors, 0)

        s_list = dir(s)
        self.assertIn("_Base__nb_objects", s_list)
        self.assertIn("__init__", s_list)
        self.assertIn("to_json_string", s_list)
        self.assertIn("save_to_file", s_list)
        self.assertIn("from_json_string", s_list)
        self.assertIn("create", s_list)
        self.assertIn("load_from_file", s_list)
        self.assertIn("width", s_list)
        self.assertIn("height", s_list)
        self.assertIn("x", s_list)
        self.assertIn("y", s_list)
        self.assertIn("size", s_list)
        self.assertIn("area", s_list)
        self.assertIn("display", s_list)
        self.assertIn("__str__", s_list)
        self.assertIn("update", s_list)
        self.assertIn("to_dictionary", s_list)

        s1_list = dir(s(1))
        self.assertIn("_Rectangle__width", s1_list)
        self.assertIn("_Rectangle__height", s1_list)
        self.assertIn("_Rectangle__x", s1_list)
        self.assertIn("_Rectangle__y", s1_list)
        self.assertIn("id", s1_list)

        self.assertIsNot(square.__doc__, None)
        self.assertIsNot(s.__doc__, None)
        self.assertIsNot(s.__init__.__doc__, None)
        self.assertIsNot(s.to_json_string.__doc__, None)
        self.assertIsNot(s.save_to_file.__doc__, None)
        self.assertIsNot(s.from_json_string.__doc__, None)
        self.assertIsNot(s.create.__doc__, None)
        self.assertIsNot(s.load_from_file.__doc__, None)
        self.assertIsNot(s.width.__doc__, None)
        self.assertIsNot(s.height.__doc__, None)
        self.assertIsNot(s.x.__doc__, None)
        self.assertIsNot(s.y.__doc__, None)

        self.assertIsInstance(s(1), s)

if __name__ == '__main__':
    unittest.main()
