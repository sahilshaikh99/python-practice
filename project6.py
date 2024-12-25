#Project: Student Record Management System
#Create a Python script that manages student records using tuples, sets, and frozen sets, and demonstrates various operations and methods.

#1. Create tuples to store student information (name, age, grade).
student_tuple = ('sahil', 26, 85)

#2. Use tuple methods to count and index elements.

print("Here is the student Information in Tuple", student_tuple)
print(student_tuple.count(26)) #counting occurences of 26 in tuple
print(student_tuple.index(85)) #checking index of element

#3. Create sets to store unique student IDs and courses.


id_set = {1,2,3,4,5}
course_set = {"database", "software eng.", "networking", "cyber security"}

#4. Perform set operations like union, intersection, and difference.

print("Union Sets", id_set.union(course_set))
print("Intersection Sets", id_set.intersection(course_set))
print("Difference Sets", id_set.difference(course_set))

#5. Use frozen sets to create immutable sets of student data.
frozen_set = frozenset([1,2,3,4])

print(frozen_set)
