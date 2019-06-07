# -*- coding: utf-8 -*-
"""
Molly Saweikis
Module 1 Day 5
"""

cheers = "where everybody knows YOUR name."
print(cheers.capitalize()) # Applies proper casing to the string.
print(cheers.title()) # Applies prper casing for use in titles.
print(cheers.lower()) # Converts entire string to lower case
print(cheers.upper()) # Converts entire string to upper case
print(cheers.swapcase()) # Inverts the case of every character in the string.
print("norm".upper()) #These methods do not have to be applied only to variables. They can also be applied directly to strings or other objects.

spinoff = "Frasier"
yr = 1993
print("The show {} was a spinoff of Cheers that first aired in {}.".format(spinoff, yr))

i = 13
print("{0:2} squared is {1:<3}.".format(i, i**2))

print("{0:2} squared is {1:<4}.".format(i, i**2))
print("{0:2} squared is {1:>4}.".format(i, i**2))
print("{0:2} squared is {1:^5}.".format(i, i**2))

msg = "END OF CODE"
print("{:=^50}".format(msg))

print("{:.5}".format(cheers.capitalize()))

pi = 22/7
print("Pi as a float is {0:f}, as a float with a precision of 2 is {0:.2f}".format(pi))
print("The answer to life, the universe and everything is {0:d} as an integer, or {0:=^10d} as a padded and centered integer.".format(42))

print(f"Pi as a float is {pi:f}, as a float with a precision of 2 is {pi:.2f}")
print(f"The answer to life, the universe, and everything is {42:d} as an integer, or {42:=^10d} as a padded and centered integer.")