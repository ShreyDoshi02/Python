# Create an empty dictionary called dog
dog = {}


# Add name, color, breed, legs, age to the dog dictionary
Dog = {
     'Name': 'Leo',
    'Color': 'White',
    'Breed': 'Pomeranian',
     'Legs': 4,
      'Age': 2
}
for Tittle , Details in Dog.items():
    print(f"{Tittle.title()} : {Details}")


# Create a student dictionary and add first_name, last_name, gender, age, marital status, skills, country, city and address as keys for the dictionary
Student = {
    'First_Name': 'Shrey',
     'Last_Name': 'Doshi',
        'Gender': 'Male',
           'Age': 19,
'Marital Status': "Un-Married",
        'Skills': ['Cricket', 'Python', 'Communication', 'Skating'],
       'Country': 'Newzealand',
          'City': 'Auckland',
       'Address': ' 202 North High Brooklyn Bridge, Homai , Bl.No. 20 '
}


# Get the length of the student dictionary
print(len(Student))


# Get the value of skills and check the data type, it should be a list
print(type(Student['Skills']))


# Modify the skills values by adding one or two skills
Student['Skills'].append('Valorant')
for a in Student['Skills']:
    print(a)


# Get the dictionary keys as a list
print(Student.keys())


# Get the dictionary values as a list
print(Student.values())


# Change the dictionary to a list of tuples using items() method
Stu_Tuple = Student.items()
print(Stu_Tuple)


# Delete one of the items in the dictionary
Student.pop('Marital Status')
for Tittle, Details in Student.items():
    print(f"{Tittle.title()} : {Details}")



# Delete one of the dictionaries
del Student
# print(Student) --> Gives Variable not defined coz' in LOC 66 we deleted the Student