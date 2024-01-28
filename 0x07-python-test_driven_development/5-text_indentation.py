#!/usr/bin/python3
"""Defines that prints a text with 2 new lines after each of these characters: ., ? and :"""


def text_indentation(text):
    """Prints a text with 2 new lines after each of these characters: ., ? and :

    Args:
        text (string): the text to indent.

    Raises:
        TypeError: If the text isn't a string.

    Return:
        Nothing.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    delim = ['.', '?', ':']

    text_list = list(text)

    for char in range(0, len(text_list)):
        for i in range(0, len(delim)):
            if text_list[char] == delim[i]:
                if text_list[char + 1] == " ":
                    text_list[char + 1] = "\n\n"
                elif text_list[char + 1] == "":
                    text_list[char + 1] = ""
                else:
                    text_list[char] += "\n\n"

    new_text = ''.join(text_list)

    print(new_text, end="")
