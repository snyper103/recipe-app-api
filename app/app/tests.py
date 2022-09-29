"""
Sample tests
"""
from django.test import SimpleTestCase

from app import calc


class CalcTests(SimpleTestCase):
	"""Test the calc module."""
	
	def test_add_numbers(self):
		res = calc.Add(4, 5)

		self.assertEqual(res, 9)

	def test_subtract_numbers(self):
		"""Test subtract numbers."""
		res = calc.Subtract(9, 4)

		self.assertEqual(res, 5)