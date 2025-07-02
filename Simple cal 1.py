9# -*- coding: utf-8 -*-
"""
Created on Wed Jul  2 15:23:46 2025

@author: omagu
"""
num1 = float(input("Enter first number: "))
operator = input("Enter operation (+, -, *, /):")
num2 = float(input("Enter second number:"))

if operator == '+':
    result = num1 + num2 
elif operator == '-':
    result = num1 - num2 
elif operator == '*':
    result= num1 * num2
elif operator == '/':
    if num2 != 0: 
        result = num1 / num2 
    else: 
        result = "Error! Division by zero,"
else: 
    result = "Invalid operator"

print("Result:", result)
