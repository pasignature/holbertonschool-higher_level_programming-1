#!/usr/bin/python3
"""UnitTest Module Base"""

import unittest
import pep8
from  os import path, remove
from models import base
from models.base import Base as b
from models.rectangle import Rectangle as r
from models.square import Square as s

class TestBase(unittest.TestCase):
    """Class Test Base"""

    def tearDown(self):
        """Tear Down"""

        b._Base__nb_objects = 0
        self.assertEqual(b._Base__nb_objects, 0)

    def test_pep8(self):
        """Test Pep8"""

        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/base.py'])
        self.assertEqual(result.total_errors, 0)

    def test_attr_method_presence(self):
        """Test Attribute Method Presence"""

        b_list = dir(b)
        self.assertIn("_Base__nb_objects", b_list)
        self.assertIn("__init__", b_list)
        self.assertIn("to_json_string", b_list)
        self.assertIn("save_to_file", b_list)
        self.assertIn("from_json_string", b_list)
        self.assertIn("create", b_list)
        self.assertIn("load_from_file", b_list)

    def test_docstring(self):
        """Test Docstring"""

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

    def test_instance(self):
        """Test Instantiation"""

        b1 = b()
        b2 = b(3)
        b3 = b(None)
        b4 = b(2.5)
        b5 = b("Hi")
        b6 = b(float('nan'))
        b7 = b(['a', 1, [4, 'y']])
        b8 = b(None)

        self.assertIsInstance(b1, b)
        self.assertEqual(b1.id, 1)
        self.assertEqual(b._Base__nb_objects, 3)

        self.assertIsInstance(b2, b)
        self.assertEqual(b2.id, 3)
        self.assertEqual(b._Base__nb_objects, 3)

        self.assertIsInstance(b3, b)
        self.assertEqual(b3.id, 2)
        self.assertEqual(b._Base__nb_objects, 3)

        self.assertIsInstance(b4, b)
        self.assertEqual(b4.id, 2.5)
        self.assertEqual(b._Base__nb_objects, 3)

        self.assertIsInstance(b5, b)
        self.assertEqual(b5.id, "Hi")
        self.assertEqual(b._Base__nb_objects, 3)

        self.assertIsInstance(b6, b)
        self.assertNotEqual(b6.id, float('nan'))
        self.assertEqual(b._Base__nb_objects, 3)

        self.assertIsInstance(b7, b)
        self.assertEqual(b7.id, ['a', 1, [4, 'y']])
        self.assertEqual(b._Base__nb_objects, 3)

        self.assertIsInstance(b8, b)
        self.assertEqual(b8.id, 3)
        self.assertEqual(b._Base__nb_objects, 3)

    def test_to_json_string(self):
        """Test To Json String"""

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

    def test_from_json_string(self):
        """Test From Json String"""

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

    def test_create(self):
        """Test Create"""

        r1d = {'id': 1, 'width': 1, 'height': 2, 'x': 3, 'y': 4}
        r2 = r.create(**r1d)
        self.assertDictEqual(r1d, r2.to_dictionary())

        s1d = {'id': 1, 'size': 1, 'x': 2, 'y': 3}
        s2 = s.create(**s1d)
        self.assertDictEqual(s1d, s2.to_dictionary())

        r1 = r(1, 2)
        r1d = r1.to_dictionary()
        r2 = r.create(**r1d)
        self.assertDictEqual(r1d, r2.to_dictionary())

        r1 = r(1, 2, 3, 4)
        r1d = r1.to_dictionary()
        r2 = r.create(**r1d)
        self.assertDictEqual(r1d, r2.to_dictionary())

        s1 = s(1)
        s1d = s1.to_dictionary()
        s2 = s.create(**s1d)
        self.assertDictEqual(s1d, s2.to_dictionary())

        s1 = s(1, 2, 3)
        s1d = s1.to_dictionary()
        s2 = s.create(**s1d)
        self.assertDictEqual(s1d, s2.to_dictionary())

    def test_save_to_file(self):
        """Test Save To File"""

        r1 = r(10, 7, 2, 8)
        r2 = r(2, 4)
        r.save_to_file([r1, r2])

        s1 = s(6, 5, 3)
        s2 = s(9)
        s.save_to_file([s1, s2])

        self.assertTrue(path.isfile('Rectangle.json'))
        self.assertTrue(path.isfile('Square.json'))

    def test_load_from_file(self):
        """Test Load From File"""

        r1 = r(10, 7, 2, 8)
        r2 = r(2, 4)
        s1 = s(6, 5, 3)
        s2 = s(9)

        rlist = r.load_from_file()
        slist = s.load_from_file()

        self.assertIsInstance(rlist[0], r)
        self.assertIsInstance(rlist[1], r)
        self.assertDictEqual(rlist[0].to_dictionary(),
                             r1.to_dictionary())
        self.assertDictEqual(rlist[1].to_dictionary(),
                             r2.to_dictionary())

        self.assertIsInstance(slist[0], s)
        self.assertIsInstance(slist[1], s)
        self.assertDictEqual(slist[0].to_dictionary(),
                             s1.to_dictionary())
        self.assertDictEqual(slist[1].to_dictionary(),
                             s2.to_dictionary())

        remove("Rectangle.json")
        remove("Square.json")

if __name__ == '__main__':
    unittest.main()
