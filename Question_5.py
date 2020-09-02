"""for n in [30,31,32,33,34,47,48,49]:
    square = n**2
    print(n,'squared is',square)

    squares = [d**2 for d in range(30,49)]
print(squares)"""
"""
for n in range(30, 49): 
    square = n**2
    print(square) 
    """
"""
n = 30
while n < 50:
    square = n**2
    print(square)
    n += 1
"""

"""
1. Create a python function ‘assign_grade(list)’ which records the marks of ten students
from a list and assign a grade based on the following conditions:
If marks>=90 then grade A
If marks >=80 && <90 then grade B
If marks >65 &&<80 then grade C
If marks>=40 && <=65 then grade D
If marks <40 then grade E
Consider the list of marks of 10 students in English.

"""
"""
def assign_grades(list):
    
    marks=[]

    for i in range(0,10):
        print('Enter the marks of 10 students in English: ')
        ele = int(input())

        marks.append(ele)
    print(marks)
    if marks>=90:
        print('Grade A')
    if marks >=80 and marks <90:
        print('Grade B')
    if marks >65 and marks<80:
        print('Grade C')
    if marks>=40 and marks <=65:
        print('Grade D')
    if marks <40:
        print('Grade E')
        """


# creating an empty list 
marks = [] 
  

  
# iterating till the range 
for i in range(1, 11): 
    print('Enter the marks of student', i)

    ele = int(input()) 
  
    marks.append(ele) # adding the element 
      
print(marks) 
#assigning grades
for mark in marks:
     if mark>=90:
            print('Grade A')
     if mark>=80 and mark <90:
        print('Grade B')
     if mark >65 and mark<80:
        print('Grade C')
     if mark>=40 and mark <=65:
        print('Grade D')
     if mark <40:
        print('Grade E')

