""" 
*   Professor B would like to know which of his student have a GPA below 3.0.
    To accomplish this, read the file - students.csv into the program. The program
    should evaluate the GPA to see if it is higher or lower than 3.0. If it is,
    then it should be written out to the file - processedStudents.csv. (This file
    already contains headers and the headers should NOT be overwritten.) 

*   Create a dictionary of each student where the student ID is the key
    and the GPA is the value.

*  print out the dictionary

*  print out the corresponding GPA for student - 567890123

I have outlined comments for each step of the program. You are
not required to use them but it is provided to help you work
through the logic of the problem.


"""


import csv


# create a file object to open the file in read mode
infile = open("students.csv", "r")


# create a csv object from the file object
students_file = csv.reader(infile, delimiter=",")

# skip the header row
next(students_file)

# create an outfile object for the pocessed record
outfile = open("processedStudents.csv", "a")


# create a new dictionary named 'student_dict'
student_dict = {}


# use a loop to iterate through each row of the file
for record in students_file:
    stuID = record[0]
    pin = record[1]
    firstName = record[2]
    lastName = record[3]
    city = record[4]
    state = record[5]
    major = record[6]
    classification = record[7]
    gpa = record[8]
    student_dict["studentID"] = stuID
    student_dict["gpa"] = gpa
    # print(pin)
    # check if the GPA is below 3.0. If so, write the record to the outfile
    if float(gpa) < 3.0:
        print(
            str(stuID)
            + ","
            + firstName
            + ","
            + lastName
            + ","
            + major
            + ","
            + classification
            + ","
            + gpa
            + "\n"
        )
        outfile.write(
            str(stuID)
            + ","
            + firstName
            + ","
            + lastName
            + ","
            + major
            + ","
            + classification
            + ","
            + gpa
            + "\n"
        )


# append the record to the dictionary with the student id as the Key
# and the value as the GPA


# print the entire dictionary
print(student_dict)

# Print the student id
print(student_dict["studentID"])


# print out the corresponding GPA from the dictionary
find_gpa = student_dict.get("567890123", "Key not found")
print(find_gpa)


# close the outfile
outfile.close()
infile.close()
