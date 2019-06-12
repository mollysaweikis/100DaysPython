# -*- coding: utf-8 -*-
"""
Molly Saweikis
Module 1 Day 8
"""

#3
theme = "East", "Bound", "West"
print(type(theme))
print(theme)
good = ("Bandit", "Frog", "Snowman")
print(type(good))
print(good)

#4
#theme[0] = "West"
print(theme)
#5
return_trip = "West", theme[1], theme[2]
print(return_trip)

#6
movie = ("Smokey and the Bandit", 1977, "Hal Needham", ("Burt Reynolds", "Sally Field", "Jerry Reed"))
title, year, director, stars = movie
bandit, frog, snowman = stars
print("Title: {}\nYear: {}\nDirector: {}".format(title, year, director))
print(type(stars))
print("Stars: {}\nBandit: {}\nFrog: {}\nSnowman: {}".format(stars, bandit, frog, snowman))
#7
movie_list = ("Smokey and the Bandit", 1977, "Hal Needham", ["Burt Reynolds", "Sally Field", "Jerry Reed"])
title, year, director, cast = movie_list
print(type(cast))
print(cast)
cast.append("Jackie Gleason")
print(cast)
#8
del movie_list

