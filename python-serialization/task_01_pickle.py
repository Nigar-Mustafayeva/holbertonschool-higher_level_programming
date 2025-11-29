#!/usr/bin/env python3
"""
Serialization and deserialization of a custom Python object using pickle
"""

import pickle


class CustomObject:
    """
    A custom Python class with attributes:
        - name (str)
        - age (int)
        - is_student (bool)
    """

    def __init__(self, name, age, is_student):
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        """
        Prints the attributes of the object in a readable format.
        """
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Is Student: {self.is_student}")

    def serialize(self, filename):
        """
        Serialize the current object instance to the specified file using pickle.
        Args:
            filename (str): The filename to save the object to.
        """
        try:
            with open(filename, "wb") as f:
                pickle.dump(self, f)
        except (OSError, pickle.PickleError):
            # In case of file write errors or pickling errors
            return None

    @classmethod
    def deserialize(cls, filename):
        """
        Deserialize an object from a file and return the object instance.
        Args:
            filename (str): The filename to load the object from.
        Returns:
            CustomObject | None: Returns the loaded object or None on failure.
        """
        try:
            with open(filename, "rb") as f:
                obj = pickle.load(f)
                return obj
        except (OSError, pickle.PickleError, EOFError):
            # Handles file not found, invalid file, or unpickling errors
            return None
