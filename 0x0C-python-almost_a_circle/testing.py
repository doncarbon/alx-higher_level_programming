#!/usr/bin/python3
""" 14-main """
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square

if __name__ == "__main__":
    s1 = Square(5, 2, 7, 4)
    sdictionary1 = s1.to_dictionary()

    s2 = Square(12, 2, 5, 2)
    sdictionary2 = s2.to_dictionary()
    slist_dicts = [sdictionary1, sdictionary2]
    print(len(Base.to_json_string(slist_dicts)))
