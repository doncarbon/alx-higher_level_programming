#!/usr/bin/python3
"""
Unittest for Rectangle class.
"""
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestRectangle(unittest.TestCase):
    """Define unittests for Rectangle class."""

    def test_init(self):
        """Initialization tests for Rectangle class."""
        self.assertIsInstance(Rectangle(10, 2), Base)

        with self.assertRaises(TypeError):
            Rectangle()
        with self.assertRaises(TypeError):
            Rectangle(1)
        with self.assertRaises(TypeError):
            Rectangle(1, 2, 3, 4, 5, 6)

        r1 = Rectangle(10, 2)
        r2 = Rectangle(2, 10)
        self.assertEqual(r1.id, r2.id - 1)

        r3 = Rectangle(2, 2, 4)
        r4 = Rectangle(4, 4, 2)
        self.assertEqual(r3.id, r4.id - 1)

        r5 = Rectangle(1, 2, 3, 4)
        r6 = Rectangle(4, 3, 2, 1)
        self.assertEqual(r5.id, r6.id - 1)

        self.assertEqual(10, Rectangle(10, 2, 0, 0, 10).id)

        r = Rectangle(5, 7, 7, 5, 1)
        self.assertEqual(5, r.width)
        r.width = 10
        self.assertEqual(10, r.width)
        self.assertEqual(7, r.height)
        r.height = 10
        self.assertEqual(10, r.height)
        self.assertEqual(7, r.x)
        r.x = 10
        self.assertEqual(10, r.x)
        self.assertEqual(5, r.y)
        r.y = 10
        self.assertEqual(10, r.y)

    def test_width(self):
        """Tests for Rectangle width attribute."""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(None, 2)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle("invalid", 2)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(5.5, 1)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(complex(5), 2)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle({"a": 1, "b": 2}, 2)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle([1, 2, 3], 2)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle({1, 2, 3}, 2)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle((1, 2, 3), 2)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(range(5), 2)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Rectangle(-1, 2)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Rectangle(0, 2)

    def test_height(self):
        """Tests for Rectangle height attribute."""
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(1, None)
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(1, "invalid")
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(1, 5.5)
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(1, {"a": 1, "b": 2})
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(1, [1, 2, 3])
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(1, {1, 2, 3})
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(1, (1, 2, 3))
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            Rectangle(1, -1)
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            Rectangle(1, 0)

    def test_x(self):
        """Tests for Rectangle x attribute."""
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(1, 2, None)
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(1, 2, "invalid", 2)
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(1, 2, 5.5, 9)
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(1, 2, complex(5))
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(1, 2, {"a": 1, "b": 2}, 2)
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(1, 2, [1, 2, 3], 2)
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(1, 2, {1, 2, 3}, 2)
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(1, 2, (1, 2, 3), 2)
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            Rectangle(5, 3, -1, 0)

    def test_y(self):
        """Tests for Rectangle y attribute."""
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(1, 2, 3, None)
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(1, 2, 1, "invalid")
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(1, 2, 3, 5.5)
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(1, 2, 1, {"a": 1, "b": 2})
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(1, 2, 1, [1, 2, 3])
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(1, 2, 1, {1, 2, 3})
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(1, 2, 1, (1, 2, 3))
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            Rectangle(3, 5, 0, -1)

    def test_area(self):
        """Tests for Rectangle area method."""
        r = Rectangle(10, 2, 0, 0, 0)
        self.assertEqual(20, r.area())

        r = Rectangle(999999999999999, 999999999999999999, 0, 0, 1)
        self.assertEqual(999999999999998999000000000000001, r.area())

        r = Rectangle(2, 10, 1, 1, 1)
        r.width = 7
        r.height = 14
        self.assertEqual(98, r.area())

        r = Rectangle(2, 10, 1, 1, 1)
        with self.assertRaises(TypeError):
            r.area(1)

if __name__ == '__main__':
    unittest.main()
