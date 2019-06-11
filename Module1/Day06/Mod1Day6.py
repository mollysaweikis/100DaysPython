# -*- coding: utf-8 -*-
"""
Molly Saweikis
Module 1 Day 6
"""

#2
list_1 = []
list_2 = list()
print("List 1 Type: {}\nList 2 Type: {}".format(type(list_1), type(list_2)))

#3
text = "Luggage Combination"
print(list(text))

#4
luggage = [1, 3, 5, 2, 4]
print(luggage)
luggage.sort()
print(luggage)

#5
numbers = [1, 2, 3, 4, 5]
print("numbers: {}".format(numbers))
numbers_sorted = numbers
numbers_sorted.sort(reverse=True)
print("numbers: {}\nnumbers_sorted: {}".format(numbers, numbers_sorted))

#6
numbers = [1, 2, 3, 4, 5]
numbers_sorted = list(numbers)
numbers_sorted.sort(reverse=True)
print("numbers: {}\nnumbers_sorted: {}".format(numbers, numbers_sorted))

#7
odd = [1, 3, 5]
even = [2, 4]
luggage = odd + even
print(luggage)

#9
print("Unsorted list: {}".format(luggage))
print("Using the sorted() function: {}".format(sorted(luggage)))
print("Unsorted list: {}".format(luggage))
luggage.sort()
print("Using the .sort() method: {}".format(luggage))

#8
luggage = [1, 3, 5]
even = [2, 4]
luggage.extend(even)
print("Luggage: {}".format(luggage))

#10
lines = []
lines.append("They told me to comb the desert, so I'm combing the desert.")
lines.append("YOGURT! I hate Yogurt! Even with strawberries!")
lines.append("We'll meet again in Spaceballs 2: The Quest for Mo Money.")
print(lines)

#11
print(luggage.index(2))

#12
quote = list("YOGURT! I hate yogurt! Even with strawberries!")
print(quote.count("r"))

#13
luggage = [1, 2, 4, 5]
print(luggage)
luggage.insert(2,3)
print(luggage)

#14
luggage = [1, 2, 3, 4, 5, 6]
print(luggage)
print(luggage.pop())
print(luggage)
print(luggage.pop(2))
print(luggage)

#15
rng = list(range(0,10))
print(rng)
rng.remove(7)
print(rng)

#16
countdown = [5, 4, 3, 2, 1]
countdown.reverse()
print(countdown)

#17
sample = list(range(1, 13))
times_12 = [i*12 for i in sample]
print(sample)
print(times_12)

#18
print(luggage)
luggage.clear()
print(luggage)

#19
luggage = [2, 2, 3, 4, 5]
print(luggage)
luggage[0] = 1
print(luggage)
