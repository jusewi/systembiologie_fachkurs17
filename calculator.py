from math import gcd # größter gemeinsamer teiler

class Expression:
	pass

class Operation(Expression):
	def __init__(self, left_operand, right_operand):
		assert isinstance(left_operand, Expression) and \
		isinstance(right_operand,Expression)

		self.left_operand = left_operand
		self.right_operand = right_operand
	

class Sum(Operation):
	def evaluate(self):
		return self.left_operand.evaluate() + self.right_operand.evaluate()

class Product(Operation):
	def evaluate(self):
		return self.left_operand.evaluate() * self.right_operand.evaluate()

class Differenz(Operation):
	def evaluate(self):
		return self.left_operand.evaluate() - self.right_operand.evaluate()

class Quotient(Operation):
	pass
	#def evaluate(self):
	#	return self.left_operand.evaluate()  self.right_operand.evaluate()


class Fraction(Expression):
	def __init__(self,numerator,denominator):
		if denominator == 0:
			raise ZeroDivisionError

		self.numerator = numerator
		self.denominator = denominator
		self.simplify()


	def __eq__(self, other):
		return self.numerator == other.numerator and \
			self.denominator == other.denominator


	def __mul__(self, other):
		return self.product(other)

	def __add__(self, other):
		return self.add(other)

	def add(self, other):
		return Fraction(self.numerator * other.denominator + self.denominator * other.numerator, 
			self.denominator * other.denominator)

	def product(self, other):
		return Fraction(self.numerator*other.numerator, 
			self.denominator*other.denominator)


	def simplify(self):
		divisor = gcd(self.numerator, self.denominator)
		self.numerator = self.numerator // divisor
		self.denominator = self.denominator // divisor


	def evaluate(self):
		return self
