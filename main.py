# Dictionary Comprehension
# new_dict = {new_key:new_value for item in list if test}
# new_dict = {new_key:new_value for (key, value) in dict.items() if test}

import random

names = ['Jon', 'Bill', 'Maria', 'Jenny', 'Jack', 'Ruby', 'Python', 'Perl', 'January', 'February', 'March']
print(f"Names: {names}")

student_score = {student: random.randint(0, 100) for student in names}  # student score
print(f"Student Score: {student_score}")

passed_student = {student: score for (student, score) in student_score.items() if score > 40}  # passed students
print(f"Passed Students: {passed_student}")
