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
        r1 = Rectangle(10, 7, 2, 8, 6)
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

    def test_from_json_string(self):
        """Test the conversion from json string feature."""
        list_input = [{'id': 89, 'width': 10, 'height': 4}]
        json_list_input = Rectangle.to_json_string(list_input)
        list_output = Rectangle.from_json_string(json_list_input)
        self.assertEqual(type(list_output), list)

        list_input1 = [{"id": 89, "width": 10, "height": 4, "x": 7}]
        json_list_input = Rectangle.to_json_string(list_input1)
        list_output = Rectangle.from_json_string(json_list_input)
        self.assertEqual(list_input1, list_output)

        list_input2 = [
            {'id': 89, 'width': 10, 'height': 4},
            {'id': 7, 'width': 1, 'height': 7}
        ]
        json_list_input = Rectangle.to_json_string(list_input2)
        list_output = Rectangle.from_json_string(json_list_input)
        self.assertEqual(list_input2, list_output)

        list_input3 = [{"id": 89, "size": 10, "height": 4}]
        json_list_input = Square.to_json_string(list_input3)
        list_output = Square.from_json_string(json_list_input)
        self.assertEqual(list_input3, list_output)

        self.assertEqual("[]", Base.from_json_string(None))

        self.assertEqual([], Base.from_json_string("[]"))

    def test_create(self):
        """Test create method."""
        r1 = Rectangle(3, 5, 1, 6, 5)
        r1_dictionary = r1.to_dictionary()
        r2 = Rectangle.create(**r1_dictionary)
        self.assertEqual("[Rectangle] (5) 1/6 - 3/5", str(r1))
        self.assertEqual("[Rectangle] (5) 1/6 - 3/5", str(r2))
        self.assertIsNot(r1, r2)
        self.assertNotEqual(r1, r2)

        s1 = Square(3, 5, 1, 6)
        s1_dictionary = s1.to_dictionary()
        s2 = Square.create(**s1_dictionary)
        self.assertEqual("[Square] (6) 5/1 - 3", str(s1))
        self.assertEqual("[Square] (6) 5/1 - 3", str(s2))
        self.assertIsNot(s1, s2)
        self.assertNotEqual(s1, s2)

    def test_save_to_file(self):
        """Test save_to_file method."""
        r1 = Rectangle(10, 7, 2, 8, 1)
        Rectangle.save_to_file([r1])
        with open("Rectangle.json", "r") as f:
            self.assertTrue(len(f.read()) == 53)

        r2 = Rectangle(2, 4, 1, 2, 3)
        Rectangle.save_to_file([r1, r2])
        with open("Rectangle.json", "r") as f:
            self.assertTrue(len(f.read()) == 105)

        s1 = Square(10, 7, 2, 8)
        Square.save_to_file([s1])
        with open("Square.json", "r") as f:
            self.assertTrue(len(f.read()) == 39)

        s2 = Square(2, 4, 1, 2)
        Square.save_to_file([s1, s2])
        with open("Square.json", "r") as f:
            self.assertTrue(len(f.read()) == 77)

        Base.save_to_file([s1])
        with open("Base.json", "r") as f:
            self.assertTrue(len(f.read()) == 39)

        s3 = Square(2, 7, 21, 6)
        Square.save_to_file([s3])
        s3 = Square(10, 7, 2, 8)
        Square.save_to_file([s3])
        with open("Square.json", "r") as f:
            self.assertTrue(len(f.read()) == 39)

        Square.save_to_file(None)
        with open("Square.json", "r") as f:
            self.assertEqual("[]", f.read())

        Square.save_to_file([])
        with open("Square.json", "r") as f:
            self.assertEqual("[]", f.read())

    def test_load_from_file(self):
        """Test load_from_file method."""
        r1 = Rectangle(10, 7, 2, 8, 1)
        r2 = Rectangle(2, 4, 5, 6, 2)
        Rectangle.save_to_file([r1, r2])
        list_rectangles_output = Rectangle.load_from_file()
        self.assertEqual(str(r1), str(list_rectangles_output[0]))
        list_rectangles_output = Rectangle.load_from_file()
        self.assertEqual(str(r2), str(list_rectangles_output[1]))
        output1 = Rectangle.load_from_file()
        self.assertTrue(all(type(obj) == Rectangle for obj in output1))

        s1 = Square(5, 1, 3, 3)
        s2 = Square(9, 5, 2, 3)
        Square.save_to_file([s1, s2])
        list_squares_output = Square.load_from_file()
        self.assertEqual(str(s1), str(list_squares_output[0]))
        list_squares_output = Square.load_from_file()
        self.assertEqual(str(s2), str(list_squares_output[1]))
        output2 = Square.load_from_file()
        self.assertTrue(all(type(obj) == Square for obj in output2))

if __name__ == '__main__':
    unittest.main()
