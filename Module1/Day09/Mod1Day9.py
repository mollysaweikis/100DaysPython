# -*- coding: utf-8 -*-
"""
Molly Saweikis
Module 1 Day 9
"""

#2
quotes = ["Pitter patter, let's get at 'er", "Hard no!", "H'are ya now?", "Good-n-you?", "Not so bad.", "Is that what you appreciates about me?"]
print(quotes[0])
print(f"{quotes[2]}\n\t{quotes[3]}\n{quotes[4]}")

#3
print(quotes[2:5])

#4
print(quotes[::2])

#5
print(quotes[::-1])

#6
print(quotes[0][::2])
print(quotes[0][::-1])

#7
wayne = "Toughest Guy in Letterkenny"
print(wayne[::-1])

#8
print("That's a Texas sized 10-4."[0:9:2])

#9
print(quotes[:])
print(quotes[3:])
print(quotes[:3])
print(quotes[::3])
#10

exchange = quotes[2:5]
print(exchange)