#!/usr/bin/python3
"""UnitTest Module Base"""

import unittest
import pep8
from  os import path, remove
from models import base
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square

class TestBase(unittest.TestCase):
    """Class Test Base"""

    def tearDown(self):
        """Tear Down"""

        Base._Base__nb_objects = 0
        self.assertEqual(Base._Base__nb_objects, 0)

    def test_pep8(self):
        """Test Pep8"""

        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/base.py'])
        self.assertEqual(result.total_errors, 0)

    def test_attr_method_presence(self):
        """Test Attribute Method Presence"""

        b_list = dir(Base)
        self.assertIn("_Base__nb_objects", b_list)
        self.assertIn("__init__", b_list)
        self.assertIn("to_json_string", b_list)
        self.assertIn("save_to_file", b_list)
        self.assertIn("from_json_string", b_list)
        self.assertIn("create", b_list)
        self.assertIn("load_from_file", b_list)

    def test_docstring(self):
        """Test Docstring"""

        b1_list = dir(Base())
        self.assertIn("id", b1_list)

        self.assertIsNot(base.__doc__, None)
        self.assertIsNot(Base.__doc__, None)
        self.assertIsNot(Base.__init__.__doc__, None)
        self.assertIsNot(Base.to_json_string.__doc__, None)
        self.assertIsNot(Base.save_to_file.__doc__, None)
        self.assertIsNot(Base.from_json_string.__doc__, None)
        self.assertIsNot(Base.create.__doc__, None)
        self.assertIsNot(Base.load_from_file.__doc__, None)

    def test_instance(self):
        """Test Instantiation"""

        b1 = Base()
        b2 = Base(3)
        b3 = Base(None)
        b4 = Base(2.5)
        b5 = Base("Hi")
        b6 = Base(float('nan'))
        b7 = Base(['a', 1, [4, 'y']])
        b8 = Base(None)

        self.assertIsInstance(b1, Base)
        self.assertEqual(b1.id, 1)
        self.assertEqual(Base._Base__nb_objects, 3)

        self.assertIsInstance(b2, Base)
        self.assertEqual(b2.id, 3)
        self.assertEqual(Base._Base__nb_objects, 3)

        self.assertIsInstance(b3, Base)
        self.assertEqual(b3.id, 2)
        self.assertEqual(Base._Base__nb_objects, 3)

        self.assertIsInstance(b4, Base)
        self.assertEqual(b4.id, 2.5)
        self.assertEqual(Base._Base__nb_objects, 3)

        self.assertIsInstance(b5, Base)
        self.assertEqual(b5.id, "Hi")
        self.assertEqual(Base._Base__nb_objects, 3)

        self.assertIsInstance(b6, Base)
        self.assertNotEqual(b6.id, float('nan'))
        self.assertEqual(Base._Base__nb_objects, 3)

        self.assertIsInstance(b7, Base)
        self.assertEqual(b7.id, ['a', 1, [4, 'y']])
        self.assertEqual(Base._Base__nb_objects, 3)

        self.assertIsInstance(b8, Base)
        self.assertEqual(b8.id, 3)
        self.assertEqual(Base._Base__nb_objects, 3)

    def test_to_json_string(self):
        """Test To Json String"""

        d1 = []
        d2 = [{'a': 'a'}]
        d3 = [{'a': 1, 'b': 2}]
        d4 = [{'a': 1, 'b': 2}, {'c': 3, 'd': 4}]
        self.assertEqual(Base.to_json_string(d1), '[]')
        self.assertEqual(Base.to_json_string(d2), '[{"a": "a"}]')
        self.assertEqual(Base.to_json_string(d3), '[{"a": 1, "b": 2}]')
        self.assertEqual(Base.to_json_string(d4),
                         '[{"a": 1, "b": 2}, {"c": 3, "d": 4}]')
        d1 = None
        d2 = [[1, 2]]
        d3 = "Not a dictionary"
        d4 = 666
        self.assertEqual(Base.to_json_string(d1), '[]')
        self.assertEqual(Base.to_json_string(d2), '[[1, 2]]')
        self.assertEqual(Base.to_json_string(d3), '"Not a dictionary"')
        with self.assertRaises(TypeError):
            Base.to_json_string(d4)

    def test_from_json_string(self):
        """Test From Json String"""

        d1 = []
        d2 = [{'a': 'a'}]
        d3 = [{'a': 1, 'b': 2}]
        d4 = [{'a': 1, 'b': 2}, {'c': 3, 'd': 4}]
        s1 = Base.to_json_string(d1)
        s2 = Base.to_json_string(d2)
        s3 = Base.to_json_string(d3)
        s4 = Base.to_json_string(d4)
        self.assertEqual(Base.from_json_string(s1), d1)
        self.assertEqual(Base.from_json_string(s2), d2)
        self.assertEqual(Base.from_json_string(s3), d3)
        self.assertEqual(Base.from_json_string(s4), d4)

        d1 = None
        d2 = [[1, 2]]
        d3 = "Not a dictionary"
        s1 = Base.to_json_string(d1)
        s2 = Base.to_json_string(d2)
        s3 = Base.to_json_string(d3)
        self.assertEqual(Base.from_json_string(s1), [])
        self.assertEqual(Base.from_json_string(s2), d2)
        self.assertEqual(Base.from_json_string(s3), d3)

    def test_create(self):
        """Test Create"""

        r1d = {'id': 1, 'width': 1, 'height': 2, 'x': 3, 'y': 4}
        r2 = Rectangle.create(**r1d)
        self.assertDictEqual(r1d, r2.to_dictionary())

        s1d = {'id': 1, 'size': 1, 'x': 2, 'y': 3}
        s2 = Square.create(**s1d)
        self.assertDictEqual(s1d, s2.to_dictionary())

        r1 = Rectangle(1, 2)
        r1d = r1.to_dictionary()
        r2 = Rectangle.create(**r1d)
        self.assertDictEqual(r1d, r2.to_dictionary())

        r1 = Rectangle(1, 2, 3, 4)
        r1d = r1.to_dictionary()
        r2 = Rectangle.create(**r1d)
        self.assertDictEqual(r1d, r2.to_dictionary())

        s1 = Square(1)
        s1d = s1.to_dictionary()
        s2 = Square.create(**s1d)
        self.assertDictEqual(s1d, s2.to_dictionary())

        s1 = Square(1, 2, 3)
        s1d = s1.to_dictionary()
        s2 = Square.create(**s1d)
        self.assertDictEqual(s1d, s2.to_dictionary())

    def test_save_to_file(self):
        """Test Save To File"""

        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        Rectangle.save_to_file([r1, r2])

        s1 = Square(6, 5, 3)
        s2 = Square(9)
        Square.save_to_file([s1, s2])

        self.assertTrue(path.isfile('Rectangle.json'))
        self.assertTrue(path.isfile('Square.json'))

    def test_load_from_file(self):
        """Test Load From File"""

        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        s1 = Square(6, 5, 3)
        s2 = Square(9)

        rlist = Rectangle.load_from_file()
        slist = Square.load_from_file()

        self.assertIsInstance(rlist[0], Rectangle)
        self.assertIsInstance(rlist[1], Rectangle)
        self.assertDictEqual(rlist[0].to_dictionary(),
                             r1.to_dictionary())
        self.assertDictEqual(rlist[1].to_dictionary(),
                             r2.to_dictionary())

        self.assertIsInstance(slist[0], Square)
        self.assertIsInstance(slist[1], Square)
        self.assertDictEqual(slist[0].to_dictionary(),
                             s1.to_dictionary())
        self.assertDictEqual(slist[1].to_dictionary(),
                             s2.to_dictionary())

        remove("Rectangle.json")
        remove("Square.json")
