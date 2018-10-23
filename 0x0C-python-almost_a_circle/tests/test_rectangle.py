#!/usr/bin/python3
"""UnitTest Module Rectangle"""

import unittest
import pep8
import sys
import io
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

    def test_area(self):
        """Test Area"""

        r1 = r(1, 1, 1, 1)
        r2 = r(4, 6, 2, 3)
        r3 = r(56, 83, 5, 7)

        self.assertEqual(r1.area(), 1)
        self.assertEqual(r2.area(), 24)
        self.assertEqual(r3.area(), 4648)

    def test_display(self):
        """Test Display"""

        r1 = r(1, 1)
        r2 = r(1, 2)
        r3 = r(2, 1)
        r4 = r(2, 2, 1)
        r5 = r(2, 2, 0, 1)
        r6 = r(2, 2, 2, 2)
        r7 = r(3, 3, 3, 3)

        god_list = ['#\n', '#\n#\n', '##\n', ' ##\n ##\n',
                    '\n##\n##\n', '\n\n  ##\n  ##\n',
                    '\n\n\n   ###\n   ###\n   ###\n']
        obj_list = [r1, r2, r3, r4, r5, r6, r7]
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

        r1 = r(1, 1)
        r2 = r(1, 2, 5)
        r3 = r(2, 1)
        r4 = r(2, 2, 1, id="HAHAHAHA")
        r5 = r(2, 2, 0, 1)
        r6 = r(2, 2, 2, 2)
        r7 = r(3, 3, 3, 3, "MUHAHAHA")

        god_list = ['[Rectangle] (1) 0/0 - 1/1\n',
                    '[Rectangle] (2) 5/0 - 1/2\n',
                    '[Rectangle] (3) 0/0 - 2/1\n',
                    '[Rectangle] (HAHAHAHA) 1/0 - 2/2\n',
                    '[Rectangle] (4) 0/1 - 2/2\n',
                    '[Rectangle] (5) 2/2 - 2/2\n',
                    '[Rectangle] (MUHAHAHA) 3/3 - 3/3\n']
        obj_list = [r1, r2, r3, r4, r5, r6, r7]
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

        r1 = r(1, 1)
        r2 = r(1, 2, 5)
        r3 = r(2, 1)
        r4 = r(2, 2, 1, id="HAHAHAHA")
        r5 = r(2, 2, 0, 1)
        r6 = r(2, 2, 2, 2)
        r7 = r(3, 3, 3, 3, "MUHAHAHA")

        r1.update(34, 64, 34, 12, 64)
        with self.assertRaises(ValueError):
            r2.update(**{'id': 234, 'y': -5})
        r3.update(None, 20, 590)
        r4.update(**{'id': 234, 'height': 64})
        with self.assertRaises(TypeError):
            r5.update(98, {'width': 236, 'y': 98})
        with self.assertRaises(TypeError):
            r6.update("JJJJ", 'L')
        r7.update()

        god_list = ['[Rectangle] (34) 12/64 - 64/34\n',
                    '[Rectangle] (234) 5/0 - 1/2\n',
                    '[Rectangle] (6) 0/0 - 20/590\n',
                    '[Rectangle] (234) 1/0 - 2/64\n',
                    '[Rectangle] (98) 0/1 - 2/2\n',
                    '[Rectangle] (JJJJ) 2/2 - 2/2\n',
                    '[Rectangle] (MUHAHAHA) 3/3 - 3/3\n']
        obj_list = [r1, r2, r3, r4, r5, r6, r7]
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

        r1 = r(1, 1)
        r2 = r(1, 2, 5)
        r3 = r(2, 1)
        r4 = r(2, 2, 1, id="HAHAHAHA")
        r5 = r(2, 2, 0, 1)
        r6 = r(2, 2, 2, 2)
        r7 = r(3, 3, 3, 3, "MUHAHAHA")

        d1 = {'id': 1, 'width': 1, 'height': 1, 'x': 0, 'y': 0}
        d2 = {'id': 2, 'width': 1, 'height': 2, 'x': 5, 'y': 0}
        d3 = {'id': 3, 'width': 2, 'height': 1, 'x': 0, 'y': 0}
        d4 = {'id': 'HAHAHAHA', 'width': 2, 'height': 2, 'x': 1, 'y': 0}
        d5 = {'id': 4, 'width': 2, 'height': 2, 'x': 0, 'y': 1}
        d6 = {'id': 5, 'width': 2, 'height': 2, 'x': 2, 'y': 2}
        d7 = {'id': 'MUHAHAHA', 'width': 3, 'height': 3, 'x': 3, 'y': 3}

        self.assertDictEqual(r1.to_dictionary(), d1)
        self.assertDictEqual(r2.to_dictionary(), d2)
        self.assertDictEqual(r3.to_dictionary(), d3)
        self.assertDictEqual(r4.to_dictionary(), d4)
        self.assertDictEqual(r5.to_dictionary(), d5)
        self.assertDictEqual(r6.to_dictionary(), d6)
        self.assertDictEqual(r7.to_dictionary(), d7)

        r6.update(**{'id': "WUT", "x": 999, "height": 888})
        d6 = {'id': 'WUT', 'width': 2, 'height': 888, 'x': 999, 'y': 2}
        self.assertDictEqual(r6.to_dictionary(), d6)
