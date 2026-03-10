# 9.4 Challenge: List of lists
"""
9.4. Challenge: List of lists
9.4 Challenge: List of lists
Write a program that contains the following lists of lists:
universities = [
['California Institute of Technology', 2175, 37704],
['Harvard', 19627, 39849],
['Massachusetts Institute of Technology', 10566, 40732],
['Princeton', 7802, 37000],
['Rice', 5879, 35551],
['Stanford', 19535, 40569],
['Yale', 11701, 40500]
]
Define a function, enrollment_stats(), with a single parameter. This
parameter should be a list of lists in which each individual list contains
three elements:
1. The name of a university
2. The total number of enrolled students
3. The annual tuition fees
enrollment_stats() should return two lists, the first containing all the
student enrollment values and the second containing all the tuition
fees.
Next, define two functions, mean() and median(), that take a single list
argument and return the mean or median of the values in each list,
respectively.
Using universities, enrollment_stats(), mean(), and median(), calculate
the total number of students, the total tuition, the mean and median
numbers of students, and the mean and median tuition values.
256
9.5. Challenge: Wax Poetic
Finally, output all values and format the output so that it looks like
this:
******************************
Total students: 77,285
Total tuition: $ 271,905
Student mean: 11,040.71
Student median: 10,566
Tuition mean: $ 38,843.57
Tuition median: $ 39,849
******************************
You can пnd the solutions to this code challenge and many other bonus
resources online at realpython.com/python-basics/resources
"""

universities = [
    ["California Institute of Technology", 2175, 37704],
    ["Harvard", 19627, 39849],
    ["Massachusetts Institute of Technology", 10566, 40732],
    ["Princeton", 7802, 37000],
    ["Stanford", 19535, 40569],
    ["Yale", 11701, 40500]
]

def enrollment_stats(university_list):
    """ Returns two lists, the first containing all the student enrollment values and the 
    second containing all the tuition fees. """
    student_enrollments = [uni[1] for uni in university_list]
    print(student_enrollments)
    tuition_fees = [uni[2] for uni in university_list]
    return [student_enrollments, tuition_fees]

def mean(items):
    """ Returns the mean of the values in the list """
    pass

def median(item_list):
    """ Returns the median of the values in the list """
    pass

total_students = 0
total_tuition = 0

student_mean = 0
student_median = 0

tuition_mean = 0
tuition_median = 0

print(enrollment_stats(universities))

print("*" * 30)
print("Total students:\t", total_students)
print("Total tuition:\t", total_tuition)
print()
print("Student mean:\t", student_mean)
print("Student median:\t", student_median)
print()
print("Tuition mean:\t", tuition_mean)
print("Tuition median:\t", tuition_median)
