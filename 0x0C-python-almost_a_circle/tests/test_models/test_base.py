#!/usr/bin/python3
"""
Unittest for Base class.
"""
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestBase(unittest.TestCase):
    """Define unittests for Base class."""
    def test_id(self):
        """Test id attribute."""
        b1 = Base()
        b2 = Base()
        b3 = Base(12)
        b4 = Base()
        b5 = Base(12.3)
        b6 = Base(None)
        b7 = Base(None)
        b8 = Base("alxschool")
        b9 = Base({"first": 1, "second": 2})
        b10 = Base(True)
        b11 = Base([1, 2, 3])
        b12 = Base((1, 2))
        b13 = Base({1, 2, 3})

        self.assertEqual(b1.id, b2.id - 1)

        self.assertEqual(b3.id, 12)

        self.assertEqual(b4.id, b2.id + 1)

        self.assertEqual(b5.id, 12.3)

        self.assertEqual(b6.id, b7.id - 1)

        self.assertEqual(b8.id, "alxschool")

        self.assertEqual(b9.id, {"first": 1, "second": 2})

        self.assertEqual(b10.id, True)

        self.assertEqual(b11.id, [1, 2, 3])

        self.assertEqual(b12.id, (1, 2))

        self.assertEqual(b13.id, {1, 2, 3})

    def test_to_json_string(self):
        """Test the conversion to json string feature."""
        r1 = Rectangle(10, 7, 2, 8)
        rdictionary1 = r1.to_dictionary()
        self.assertEqual(str, type(Base.to_json_string([rdictionary1])))
        self.assertTrue(len(Base.to_json_string([rdictionary1])) == 53)

        r2 = Rectangle(4, 3, 9, 15, 7)
        rdictionary2 = r2.to_dictionary()
        list_dicts = [rdictionary1, rdictionary2]
        self.assertTrue(len(Base.to_json_string(list_dicts)) == 106)

        s1 = Square(5, 2, 7, 4)
        sdictionary1 = s1.to_dictionary()
        self.assertEqual(str, type(Base.to_json_string([sdictionary1])))

        s2 = Square(12, 2, 5, 2)
        sdictionary2 = s2.to_dictionary()
        self.assertTrue(len(Base.to_json_string([sdictionary2])) == 39)

        slist_dicts = [sdictionary1, sdictionary2]
        self.assertTrue(len(Base.to_json_string(slist_dicts)) == 77)

        self.assertEqual("[]", Base.to_json_string([]))

        self.assertEqual("[]", Base.to_json_string(None))

if __name__ == '__main__':
    unittest.main()
