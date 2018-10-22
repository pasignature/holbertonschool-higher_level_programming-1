#!/usr/bin/python3
"""UnitTest Module Rectangle"""

import unittest
import pep8
from models import rectangle
from models.rectangle import Rectangle as r
from models.base import Base as b


class TestBase(unittest.TestCase):
    """Class Test Rectangle"""

    def tearDown(self):
        """Tear Down"""

        b._Base__nb_objects = 0
        self.assertEqual(b._Base__nb_objects, 0)

    def test_pep8(self):
        """Test Pep8"""

        pep8style = pep8.StyleGuide(quiet=True)
        result1 = pep8style.check_files(['models/rectangle.py'])
        result2 = pep8style.check_files(['tests/test_rectangle.py'])
        self.assertEqual(result1.total_errors, 0)
        self.assertEqual(result2.total_errors, 0)

    def test_attr_method_presence(self):
        """Test Attribute Method Presence"""

        r_list = dir(r)
        self.assertIn("_Base__nb_objects", r_list)
        self.assertIn("__init__", r_list)
        self.assertIn("to_json_string", r_list)
        self.assertIn("save_to_file", r_list)
        self.assertIn("from_json_string", r_list)
        self.assertIn("create", r_list)
        self.assertIn("load_from_file", r_list)
        self.assertIn("width", r_list)
        self.assertIn("height", r_list)
        self.assertIn("x", r_list)
        self.assertIn("y", r_list)
        self.assertIn("area", r_list)
        self.assertIn("display", r_list)
        self.assertIn("__str__", r_list)
        self.assertIn("update", r_list)
        self.assertIn("to_dictionary", r_list)

        r1_list = dir(r(1, 1))
        self.assertIn("_Rectangle__width", r1_list)
        self.assertIn("_Rectangle__height", r1_list)
        self.assertIn("_Rectangle__x", r1_list)
        self.assertIn("_Rectangle__y", r1_list)
        self.assertIn("id", r1_list)

        self.assertEqual(b._Base__nb_objects, 1)

    def test_docstring(self):
        """Test Docstring"""

        self.assertIsNot(rectangle.__doc__, None)
        self.assertIsNot(r.__doc__, None)
        self.assertIsNot(r.__init__.__doc__, None)
        self.assertIsNot(r.to_json_string.__doc__, None)
        self.assertIsNot(r.save_to_file.__doc__, None)
        self.assertIsNot(r.from_json_string.__doc__, None)
        self.assertIsNot(r.create.__doc__, None)
        self.assertIsNot(r.load_from_file.__doc__, None)
        self.assertIsNot(r.width.__doc__, None)
        self.assertIsNot(r.height.__doc__, None)
        self.assertIsNot(r.x.__doc__, None)
        self.assertIsNot(r.y.__doc__, None)

    def test_instance(self):
        """Test Instance"""

        r1 = r(1, 1)
        self.assertEqual(r._Base__nb_objects, 1)

        with self.assertRaises(ValueError):
            r(-1, 1, 1, 1)
        with self.assertRaises(ValueError):
            r(0, 1, 1, 1)
        with self.assertRaises(TypeError):
            r("A", 1, 1, 1)
        with self.assertRaises(TypeError):
            r(1.1, 1, 1, 1)
        with self.assertRaises(TypeError):
            r(None, 1, 1, 1)
        with self.assertRaises(TypeError):
            r(True, 1, 1, 1)
        with self.assertRaises(TypeError):
            r(False, 1, 1, 1)

        self.assertEqual(b._Base__nb_objects, 1)

        with self.assertRaises(ValueError):
            r(1, -1, 1, 1)
        with self.assertRaises(ValueError):
            r(1, 0, 1, 1)
        with self.assertRaises(TypeError):
            r(1, "A", 1, 1)
        with self.assertRaises(TypeError):
            r(1, 1.1, 1, 1)
        with self.assertRaises(TypeError):
            r(1, None, 1, 1)
        with self.assertRaises(TypeError):
            r(1, True, 1, 1)
        with self.assertRaises(TypeError):
            r(1, False, 1, 1)

        self.assertEqual(b._Base__nb_objects, 1)

        with self.assertRaises(ValueError):
            r(1, 1, -1, 1)
        with self.assertRaises(TypeError):
            r(1, 1, "A", 1)
        with self.assertRaises(TypeError):
            r(1, 1, 1.1, 1)
        with self.assertRaises(TypeError):
            r(1, 1, None, 1)
        with self.assertRaises(TypeError):
            r(1, 1, True, 1)
        with self.assertRaises(TypeError):
            r(1, 1, False, 1)

        self.assertEqual(b._Base__nb_objects, 1)

        with self.assertRaises(ValueError):
            r(1, 1, 1, -1)
        with self.assertRaises(TypeError):
            r(1, 1, 1, "A")
        with self.assertRaises(TypeError):
            r(1, 1, 1, 1.1)
        with self.assertRaises(TypeError):
            r(1, 1, 1, None)
        with self.assertRaises(TypeError):
            r(1, 1, 1, True)
        with self.assertRaises(TypeError):
            r(1, 1, 1, False)

        self.assertEqual(b._Base__nb_objects, 1)

if __name__ == '__main__':
    unittest.main()
