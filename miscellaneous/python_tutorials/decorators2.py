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

master_list = sorted(master_list, key=lambda x: x[2])

for entry in master_list:
    if entry[3] is "M":
        print "Mr. %s %s" % (entry[0], entry[1])
    else:
        print "Ms. %s %s" % (entry[0], entry[1])
