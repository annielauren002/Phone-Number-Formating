# -*- coding: utf-8 -*-
"""phone_num_formatting.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1jCprkoku3MjfUwhdnAnUAtDd7mDn6AO9
"""

def phone_num_format(numbers):
    if len(numbers) != 10 or not all(n.isdigit() for n in numbers):
        print("Input must be exactly 10 digits (0-9).")

    return "({}{}{}) {}{}{}-{}{}{}{}".format(*numbers)

# Taking user input:
user_input = input("Enter a 10-digit phone number (no spaces or dashes): ")

# Checking and formatting the input
if len(user_input) == 10 and user_input.isdigit():
  formatted_number = phone_num_format(user_input)
  print("Formatted Phone Number:", formatted_number)
else:
  print("Invalid input! Please enter exactly 10 digits (0-9).")