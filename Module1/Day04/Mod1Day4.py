# -*- coding: utf-8 -*-
"""
Molly Saweikis
Module 1 Day 4
"""

greeting = "Hello"
_name = "General Kenobi"
Greeting = "There"
_bestLine_ep3_ = "You are a bold one."

print(greeting+ " " + Greeting + "\n\t" + _name + " " + _bestLine_ep3_)
print("{} {}\n\t{} {}".format(greeting, Greeting, _name, _bestLine_ep3_))

released = 2005

print("Revenge of the Sith was released on May 4, " + str(released) + ".")
print("Revenge of the Sith was released on May 4, {}.".format(released))

a = 3
b = 4
c = (a**2 + b**2)**0.5
print("Pythagorean Theorum: a^2 + b^2 = c^2, so when a = {} and b = {}, then c = {}".format(a,b,c))

film = "Revenge of the Sith"
print("Sith" in film)
print("sith" in film)
print("sith" in film.lower())

var = "Variables are mutable"
print(type(var))
var = 3
print(type(var))
var = 3.5 
print(type(var))
var=int(var) # If the variable contains a numberic value, it can be converted to an integer type with the int() function.
print(type(var))
var = float(var) # If the variable contains a numeric value, it can be converted to a float type with the float() function.
print(type(var))
var = True
print(type(var))