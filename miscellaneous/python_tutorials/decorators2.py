"""
decorators2.py

Each person has a first name, last name, age, and sex. Print their names in a specific format (Mr./Ms. + First Name + Last Name) sorted by their age in ascending order (youngest first).
"""

number = input()
count = 0
master_list = []

while(count < number):
    record = raw_input()
    record_list = record.split()
    record_tuple = tuple(record_list)
    #Tuple of the form firstname, lastname, age, gender

    master_list.append(record_tuple)
    count += 1
