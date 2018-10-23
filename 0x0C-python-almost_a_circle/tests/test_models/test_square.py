#!/usr/bin/python3
"""UnitTest Module Sqaure"""

import unittest
import sys
import io
from models import square
from models.square import Square as s
from models.rectangle import Rectangle as r
from models.base import Base as b


class TestBase(unittest.TestCase):
    """Class Test Base"""

    def tearDown(self):
        """Tear Down"""

        b._Base__nb_objects = 0
        self.assertEqual(b._Base__nb_objects, 0)

    """
    def test_presence(self):

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

    def test_docstring(self):

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
    """

    def test_instance(self):
        """Test Instance"""

        s1 = s(1, 1)
        self.assertEqual(b._Base__nb_objects, 1)

        with self.assertRaises(ValueError):
            s(-1, 1, 1)
        with self.assertRaises(ValueError):
            s(0, 1, 1)
        with self.assertRaises(TypeError):
            s("A", 1, 1)
        with self.assertRaises(TypeError):
            s(1.1, 1, 1)
        with self.assertRaises(TypeError):
            s(None, 1, 1)
        with self.assertRaises(TypeError):
            s(True, 1, 1)
        with self.assertRaises(TypeError):
            s(False, 1, 1)

        self.assertEqual(b._Base__nb_objects, 1)

        with self.assertRaises(ValueError):
            s(1, -1, 1)
        with self.assertRaises(TypeError):
            s(1, "A", 1)
        with self.assertRaises(TypeError):
            s(1, 1.1, 1)
        with self.assertRaises(TypeError):
            s(1, None, 1)
        with self.assertRaises(TypeError):
            s(1, True, 1)
        with self.assertRaises(TypeError):
            s(1, False, 1)

        self.assertEqual(b._Base__nb_objects, 1)

        with self.assertRaises(ValueError):
            s(1, 1, -1)
        with self.assertRaises(TypeError):
            s(1, 1, "A")
        with self.assertRaises(TypeError):
            s(1, 1, 1.1)
        with self.assertRaises(TypeError):
            s(1, 1, None)
        with self.assertRaises(TypeError):
            s(1, 1, True)
        with self.assertRaises(TypeError):
            s(1, 1, False)

        self.assertEqual(b._Base__nb_objects, 1)

    def test_area(self):
        """Test Area"""

        s1 = s(1, 1, 1)
        s2 = s(4, 2, 3)
        s3 = s(56, 5, 7)

        self.assertEqual(s1.area(), 1)
        self.assertEqual(s2.area(), 16)
        self.assertEqual(s3.area(), 3136)

    def test_display(self):
        """Test Display"""

        s1 = s(1)
        s2 = s(2)
        s3 = s(3)
        s4 = s(2, 2, 1)
        s5 = s(2, 0, 1)
        s6 = s(2, 2, 2)
        s7 = s(3, 3, 3)

        god_list = ['#\n', '##\n##\n', '###\n###\n###\n',
                    '\n  ##\n  ##\n', '\n##\n##\n', '\n\n  ##\n  ##\n',
                    '\n\n\n   ###\n   ###\n   ###\n']
        obj_list = [s1, s2, s3, s4, s5, s6, s7]
        out_list = []

        for obj in obj_list:
            capture = io.StringIO()
            sys.stdout = capture
            obj.display()
            sys.stdout = sys.__stdout__
            out_list.append(capture.getvalue())

        self.assertListEqual(god_list, out_list)

    def test_str(self):
        """Test Str"""

        s1 = s(1)
        s2 = s(2, 5)
        s3 = s(2, 1)
        s4 = s(2, 1, id="HAHAHAHA")
        s5 = s(2, 0, 1)
        s6 = s(2, 2, 2)
        s7 = s(3, 3, 3, "MUHAHAHA")

        god_list = ['[Square] (1) 0/0 - 1\n',
                    '[Square] (2) 5/0 - 2\n',
                    '[Square] (3) 1/0 - 2\n',
                    '[Square] (HAHAHAHA) 1/0 - 2\n',
                    '[Square] (4) 0/1 - 2\n',
                    '[Square] (5) 2/2 - 2\n',
                    '[Square] (MUHAHAHA) 3/3 - 3\n']
        obj_list = [s1, s2, s3, s4, s5, s6, s7]
        out_list = []

        for obj in obj_list:
            capture = io.StringIO()
            sys.stdout = capture
            print(obj)
            sys.stdout = sys.__stdout__
            out_list.append(capture.getvalue())

        self.assertListEqual(god_list, out_list)

    def test_update(self):
        """Test Update"""

        s1 = s(1)
        s2 = s(2, 5)
        s3 = s(2, 1)
        s4 = s(2, 1, id="HAHAHAHA")
        s5 = s(2, 0, 1)
        s6 = s(2, 2, 2)
        s7 = s(3, 3, 3, "MUHAHAHA")

        s1.update(34, 64, 12, 64)
        with self.assertRaises(ValueError):
            s2.update(**{'id': 234, 'y': -5})
        s3.update(None, 20, 590)
        s4.update(**{'id': 234, 'height': 64})
        with self.assertRaises(TypeError):
            s5.update(98, {'width': 236, 'y': 98})
        with self.assertRaises(TypeError):
            s6.update("JJJJ", 'L')
        s7.update()

        god_list = ['[Square] (34) 12/64 - 64\n',
                    '[Square] (234) 5/0 - 2\n',
                    '[Square] (6) 590/0 - 20\n',
                    '[Square] (234) 1/0 - 2\n',
                    '[Square] (98) 0/1 - 2\n',
                    '[Square] (JJJJ) 2/2 - 2\n',
                    '[Square] (MUHAHAHA) 3/3 - 3\n']
        obj_list = [s1, s2, s3, s4, s5, s6, s7]
        out_list = []

        for obj in obj_list:
            capture = io.StringIO()
            sys.stdout = capture
            print(obj)
            sys.stdout = sys.__stdout__
            out_list.append(capture.getvalue())

        self.assertListEqual(god_list, out_list)

    def test_to_dictionary(self):
        """Test To Dictionary"""

        s1 = s(1, 1)
        s2 = s(1, 2, 5)
        s3 = s(2, 1)
        s4 = s(2, 1, id="HAHAHAHA")
        s5 = s(2, 2, 0, 1)
        s6 = s(2, 2, 2, 2)
        s7 = s(3, 3, 3, "MUHAHAHA")

        d1 = {'id': 1, 'size': 1, 'x': 1, 'y': 0}
        d2 = {'id': 2, 'size': 1, 'x': 2, 'y': 5}
        d3 = {'id': 3, 'size': 2, 'x': 1, 'y': 0}
        d4 = {'id': 'HAHAHAHA', 'size': 2, 'x': 1, 'y': 0}
        d5 = {'id': 1, 'size': 2, 'x': 2, 'y': 0}
        d6 = {'id': 2, 'size': 2, 'x': 2, 'y': 2}
        d7 = {'id': 'MUHAHAHA', 'size': 3, 'x': 3, 'y': 3}

        self.assertDictEqual(s1.to_dictionary(), d1)
        self.assertDictEqual(s2.to_dictionary(), d2)
        self.assertDictEqual(s3.to_dictionary(), d3)
        self.assertDictEqual(s4.to_dictionary(), d4)
        self.assertDictEqual(s5.to_dictionary(), d5)
        self.assertDictEqual(s6.to_dictionary(), d6)
        self.assertDictEqual(s7.to_dictionary(), d7)

        s6.update(**{'id': "WUT", "x": 999, "size": 23})
        d6 = {'id': 'WUT', 'size': 23, 'x': 999, 'y': 2}
        self.assertDictEqual(s6.to_dictionary(), d6)

if __name__ == '__main__':
    unittest.main()
