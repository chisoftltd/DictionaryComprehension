# Dictionary Comprehension
# new_dict = {new_key:new_value for item in list if test}
# new_dict = {new_key:new_value for (key, value) in dict.items() if test}

import random

#
# names = ['Jon', 'Bill', 'Maria', 'Jenny', 'Jack', 'Ruby', 'Python', 'Perl', 'January', 'February', 'March']
# print(f"Names: {names}")
#
# student_score = {student: random.randint(0, 100) for student in names}  # student score
# print(f"Student Score: {student_score}")
#
# passed_student = {student: score for (student, score) in student_score.items() if score > 60}  # passed students
# print(f"Passed Students: {passed_student}")

# Instructions
# You are going to use Dictionary Comprehension to create a dictionary called result that takes each word in the given
# sentence and calculates the number of letters in each word.
# Try Googling to find out how to convert a sentence into a list of words.

sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
# Don't change code above 👆

# Write your code below:
result = {word: len(word) for word in sentence.split()}

print(result)
