#!/usr/bin/env python3
"""Unittest for command line interpreter"""

import unittest
import pep8
import console
import inspect
HBNBCommand = console.HBNBCommand


class TestConsole(unittest.TestCase):
    """Unittest for command line interpreter"""

    def test_pep8_console(self):
        """Tests pep8 style"""
        style = pep8.StyleGuide(quiet=True)
        result = style.check_files(['console.py'])
        self.assertEqual(result.total_errors, 0, "fix pep8")

    def test_docstrings_in_console(self):
        """Tests docstrings"""
        self.assertIsNot(console.__doc__, None,
                         "Missing docstring")
        self.assertTrue(len(console.__doc__) >= 1,
                        "Missing docstring")

    def test_docstrings_in_class(self):
        """Tests docstrings"""
        self.assertIsNot(HBNBCommand.__doc__, None,
                         "Missing docstring")
        self.assertTrue(len(HBNBCommand.__doc__) >= 1,
                        "Missing docstring")

    def test_console_module_docstring(self):
        """Test console.py module docstring"""
        self.assertIsNot(console.__doc__, None,
                         "console.py needs a docstring")
        self.assertTrue(len(console.__doc__) >= 1,
                        "console.py needs a docstring")

    def test_console_function_docstrings(self):
        """Test docstrings in console.py functions"""
        for func in dir(HBNBCommand):
            self.assertIsNot(func.__doc__, None,
                             "{:s} method needs a docstring".format(func))
            self.assertTrue(len(func.__doc__) >= 1,
                            "{:s} method needs a docstring".format(func))
