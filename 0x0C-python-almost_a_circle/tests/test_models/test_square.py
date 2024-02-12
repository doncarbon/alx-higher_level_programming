#!/usr/bin/python3
"""
Unittest for Square class.
"""
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestSquare(unittest.TestCase):
    """Define unittests for Square class."""
    def test_init(self):
        """Initialization tests for Square class."""
        self.assertIsInstance(Square(2), Base)
        self.assertIsInstance(Square(2), Square)
        with self.assertRaises(TypeError):
            Square()

        s1 = Square(2)
        s2 = Square(3)
        self.assertEqual(s1.id, s2.id - 1)

        s3 = Square(10, 2)
        s4 = Square(2, 10)
        self.assertEqual(s3.id, s4.id - 1)

        s5 = Square(10, 2, 2)
        s6 = Square(2, 2, 10)
        self.assertEqual(s5.id, s6.id - 1)

        self.assertEqual(7, Square(10, 2, 2, 7).id)

        with self.assertRaises(TypeError):
            Square(1, 2, 3, 4, 5)
        with self.assertRaises(AttributeError):
            print(Square(10, 2, 3, 4).__size)

        self.assertEqual(19, Square(19, 5, 20, 10).size)

        s = Square(9, 3, 5, 2)
        s.size = 8
        self.assertEqual(8, s.size)
        self.assertEqual(8, s.width)
        self.assertEqual(8, s.height)

        self.assertEqual(0, Square(3).x)
        self.assertEqual(0, Square(3).y)

    def test_sizeraises(self):
        """Tests for size initialization errors."""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square(None)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square("alxschool")
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square(2.5)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square({"a": 1, "b": 2}, 2)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square([1, 2, 3])
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square({1, 2, 3}, 2)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square((1, 2, 3), 2, 3)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Square(-1, 2)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Square(0, 2)

    def test_xraises(self):
        """Tests for x initialization errors."""
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(1, None)
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(1, "invalid")

        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(1, 5.5)
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(1, {"a": 1, "b": 2}, 2)
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(1, [1, 2, 3])
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(1, {1, 2, 3})
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(1, (1, 2, 3))
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(1, range(5))
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            Square(5, -1, 0)

    def test_yraises(self):
        """Tests for y initialization errors."""
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(1, 1, None)
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(1, 1, "invalid")
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(1, 1, 5.5)
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(1, 1, {"a": 1, "b": 2}, 2)
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(1, 1, [1, 2, 3])
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(1, 1, {1, 2, 3})
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(1, 1, (1, 2, 3))
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(1, 1, range(5))
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            Square(5, 0, -1)

    def test_area(self):
        """Tests for area method."""
        self.assertEqual(100, Square(10, 0, 0, 1).area())

        s1 = Square(999999999999999999, 0, 0, 1)
        self.assertEqual(999999999999999998000000000000000001, s1.area())

        s2 = Square(10, 5, 0, 1)
        s2.size = 5
        self.assertEqual(25, s2.area())

    def test_update(self):
        """Tests for update method."""
        s = Square(10, 10, 10, 10)
        s.update()
        self.assertEqual("[Square] (10) 10/10 - 10", str(s))
        s.update(89)
        self.assertEqual("[Square] (89) 10/10 - 10", str(s))
        s.update(89, 2)
        self.assertEqual("[Square] (89) 10/10 - 2", str(s))
        s.update(89, 2, 3)
        self.assertEqual("[Square] (89) 3/10 - 2", str(s))
        s.update(89, 2, 3, 4)
        self.assertEqual("[Square] (89) 3/4 - 2", str(s))
        s.update(89, 2, 3, 4, 5)
        self.assertEqual("[Square] (89) 3/4 - 2", str(s))
        s.update(89, 2)
        self.assertEqual(2, s.width)
        s.update(89, 2)
        self.assertEqual(2, s.height)
        s.update(None)
        tocompare1 = "[Square] ({}) 3/4 - 2".format(s.id)
        self.assertEqual(tocompare1, str(s))
        s.update(None, 4, 5)
        tocompare2 = "[Square] ({}) 5/4 - 4".format(s.id)
        self.assertEqual(tocompare2, str(s))
        s.update(89, 2, 3, 4)
        s.update(4, 3, 2, 89)
        self.assertEqual("[Square] (4) 2/89 - 3", str(s))

        s = Square(10, 10, 10, 10)
        s.update(id=1)
        self.assertEqual("[Square] (1) 10/10 - 10", str(s))
        s.update(size=1, id=2)
        self.assertEqual("[Square] (2) 10/10 - 1", str(s))
        s.update(y=1, size=3, id=89)
        self.assertEqual("[Square] (89) 10/1 - 3", str(s))
        s.update(id=89, x=1, y=3, size=4)
        self.assertEqual("[Square] (89) 1/3 - 4", str(s))
        s.update(id=89, size=8)
        self.assertEqual(8, s.width)
        s.update(id=89, size=9)
        self.assertEqual(9, s.height)
        s.update(id=None)
        tocompare3 = "[Square] ({}) 1/3 - 9".format(s.id)
        self.assertEqual(tocompare3, str(s))
        s.update(id=None, size=7, x=18)
        tocompare4 = "[Square] ({}) 18/3 - 7".format(s.id)
        self.assertEqual(tocompare4, str(s))
        s.update(id=89, x=1)
        s.update(y=3, x=15, size=2)
        self.assertEqual("[Square] (89) 15/3 - 2", str(s))

    def test_to_dictionary(self):
        """Tests for to_dictionary method."""
        s = Square(4, 3, 1, 7)
        self.assertDictEqual( {'id': 7, 'x': 3, 'size': 4, 'y': 1}, s.to_dictionary())

        s1 = Square(10, 2, 1, 2)
        s2 = Square(1, 2, 10)
        s2.update(**s1.to_dictionary())
        self.assertNotEqual(s1, s2)

if __name__ == '__main__':
    unittest.main()
