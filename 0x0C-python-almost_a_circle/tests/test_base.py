#!/usr/bin/python3
"""UnitTest Module Base"""

import unittest
import pep8
from models import base
from models.base import Base as b


class TestBase(unittest.TestCase):
    """Class Test Base"""

    def test_base_class(self):
        """Test Base Class"""

        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/base.py'])
        self.assertEqual(result.total_errors, 0)

        b_list = dir(b)
        self.assertIn("_Base__nb_objects", b_list)
        self.assertIn("__init__", b_list)
        self.assertIn("to_json_string", b_list)
        self.assertIn("save_to_file", b_list)
        self.assertIn("from_json_string", b_list)
        self.assertIn("create", b_list)
        self.assertIn("load_from_file", b_list)

        b1_list = dir(b())
        self.assertIn("id", b1_list)

        self.assertIsNot(base.__doc__, None)
        self.assertIsNot(b.__doc__, None)
        self.assertIsNot(b.__init__.__doc__, None)
        self.assertIsNot(b.to_json_string.__doc__, None)
        self.assertIsNot(b.save_to_file.__doc__, None)
        self.assertIsNot(b.from_json_string.__doc__, None)
        self.assertIsNot(b.create.__doc__, None)
        self.assertIsNot(b.load_from_file.__doc__, None)

        b1 = b()
        self.assertIsInstance(b1, b)
        self.assertEqual(b1.id, 2)
        self.assertEqual(b._Base__nb_objects, 2)

        b2 = b(3)
        self.assertIsInstance(b2, b)
        self.assertEqual(b2.id, 3)
        self.assertEqual(b._Base__nb_objects, 2)

        b3 = b(None)
        self.assertIsInstance(b3, b)
        self.assertEqual(b3.id, 3)
        self.assertEqual(b._Base__nb_objects, 3)

        b4 = b(2.5)
        self.assertIsInstance(b4, b)
        self.assertEqual(b4.id, 2.5)
        self.assertEqual(b._Base__nb_objects, 3)

        b5 = b("hi")
        self.assertIsInstance(b5, b)
        self.assertEqual(b5.id, "hi")
        self.assertEqual(b._Base__nb_objects, 3)

        b6 = b(float('nan'))
        self.assertIsInstance(b6, b)
        self.assertNotEqual(b6.id, float('nan'))
        self.assertEqual(b._Base__nb_objects, 3)

        b7 = b(['a', 1, [4, 'y']])
        self.assertIsInstance(b7, b)
        self.assertEqual(b7.id, ['a', 1, [4, 'y']])
        self.assertEqual(b._Base__nb_objects, 3)

        b8 = b(None)
        self.assertIsInstance(b8, b)
        self.assertEqual(b8.id, 4)
        self.assertEqual(b._Base__nb_objects, 4)

        d1 = []
        d2 = [{'a': 'a'}]
        d3 = [{'a': 1, 'b': 2}]
        d4 = [{'a': 1, 'b': 2}, {'c': 3, 'd': 4}]
        self.assertEqual(b.to_json_string(d1), '[]')
        self.assertEqual(b.to_json_string(d2), '[{"a": "a"}]')
        self.assertEqual(b.to_json_string(d3), '[{"a": 1, "b": 2}]')
        self.assertEqual(b.to_json_string(d4),
                         '[{"a": 1, "b": 2}, {"c": 3, "d": 4}]')
        d1 = None
        d2 = [[1, 2]]
        d3 = "Not a dictionary"
        d4 = 666
        self.assertEqual(b.to_json_string(d1), '[]')
        self.assertEqual(b.to_json_string(d2), '[[1, 2]]')
        self.assertEqual(b.to_json_string(d3), '"Not a dictionary"')
        with self.assertRaises(TypeError):
            b.to_json_string(d4)

        b9 = b()
        self.assertEqual(b._Base__nb_objects, 5)

        d1 = []
        d2 = [{'a': 'a'}]
        d3 = [{'a': 1, 'b': 2}]
        d4 = [{'a': 1, 'b': 2}, {'c': 3, 'd': 4}]
        s1 = b.to_json_string(d1)
        s2 = b.to_json_string(d2)
        s3 = b.to_json_string(d3)
        s4 = b.to_json_string(d4)
        self.assertEqual(b.from_json_string(s1), d1)
        self.assertEqual(b.from_json_string(s2), d2)
        self.assertEqual(b.from_json_string(s3), d3)
        self.assertEqual(b.from_json_string(s4), d4)

        d1 = None
        d2 = [[1, 2]]
        d3 = "Not a dictionary"
        s1 = b.to_json_string(d1)
        s2 = b.to_json_string(d2)
        s3 = b.to_json_string(d3)
        self.assertEqual(b.from_json_string(s1), [])
        self.assertEqual(b.from_json_string(s2), d2)
        self.assertEqual(b.from_json_string(s3), d3)

        b10 = b()
        self.assertEqual(b._Base__nb_objects, 6)

if __name__ == '__main__':
    unittest.main()
