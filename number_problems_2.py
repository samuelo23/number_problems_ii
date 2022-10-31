import math


def roman_numeral(n):
	m = ["", "M", "MM", "MMM"]
	c = ["", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM "]
	x = ["", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"]
	i = ["", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"]
	
	thousands = m[num // 1000]
	hundreds = c[(num % 1000) // 100]
	tens = x[(num % 100) // 10]
	ones = i[num % 10]
	
	ans = (thousands + hundreds + tens + ones)
	
	return ans

def total_roman(n):
	pass

def chisel_strokes(n):
	pass

def describe(n):
	pass

def binary_without_zeros(n):
	pass
