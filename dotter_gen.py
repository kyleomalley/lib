#!/usr/bin/env python
""" Yield all email usernames that contain all valid '.' placements (primarily for gmail username accounts)

"""

from __future__ import print_function

__author__ = "Kyle O'Malley"
__license__ = "GPL"
__version__ = "1.0.1"
__maintainer__ = "kylepomalley@gmail.com"


def dotter_gen(email):
	""" Yield email string for valid input email address """


	user,domain = email.split("@")
	nodots = list(user[:-1])
	dotted = [n+"." for n in user[:-1]]

	for i in range(2 ** len(user)-1):

		new_word = ""
		for j in range(len(user)-1):
			if i % 2 == 0:
				new_word += nodots[j]
			else:
				new_word += dotted[j]
			i = i // 2
		result = (new_word+user[-1:]+"@"+domain)
		yield result


if __name__ == '__main__':
	for n in dotter_gen("billy@ms.com"):
		print(n)