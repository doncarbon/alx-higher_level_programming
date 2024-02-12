#!/usr/bin/python3
""" 14-main """
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square

if __name__ == "__main__":
    r1 = Rectangle(10, 7, 2, 8)
    rdictionary1 = r1.to_dictionary()
    print(len(Base.to_json_string([rdictionary1])))
