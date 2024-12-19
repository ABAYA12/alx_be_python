#!/usr/bin/env python3

# Prompt for user input
number = int(input("Enter a number to see its multiplication table: "))

# Generate and display the multiplication table
for X in range(1, 11):
    Z = number * X
    print(f"{number} * {X} = {Z}")

