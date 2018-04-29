# Programmed by MD. Mehedi Hasan

from pythonds.basic.stack import Stack

def bracket_checker(brackets):

	s = Stack()
	index = 0

	while index < len(brackets):
		symbol = brackets[index]

		if symbol == '(':
			s.push(symbol)

		else:
			s.pop()

		index = index + 1

	if s.isEmpty():
		print('{} , the string of parentheses is balanced.'.format(brackets))

	else:
		print('{} , the string of parentheses is not balanced.'.format(brackets))

bracket_checker('()()()')
bracket_checker('(((()))')