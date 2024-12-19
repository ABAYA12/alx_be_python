#!/usr/bin/env python3

# Prompt for task details
task = input("Enter the task description: ")
priority = input("Enter the task's priority (high, medium, low): ").lower()
time_bound = input("Is the task time-bound (yes or no)? ").lower()

# Process the task based on priority
match priority:
    case "high":
        reminder = f"Task '{task}' is HIGH priority."
    case "medium":
        reminder = f"Task '{task}' is MEDIUM priority."
    case "low":
        reminder = f"Task '{task}' is LOW priority."
    case _:
        reminder = f"Task '{task}' has an UNKNOWN priority level."

# Check if the task is time-sensitive
if time_bound == "yes":
    reminder += " This task requires immediate attention today!"

# Print the customized reminder
print(reminder)

