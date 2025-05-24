# ERP SYSTEM

## DATA SET ##
database = {}

## FUNCTIONS ##
def get_data():
    n = int(input("Enter the number of studenrs in class: "))
    for i in range(n):
        #getting inputs
        rollno = int(input("Enter the roll no.: "))
        name = input("Enter student name: ")
        marks = list(input("Enter subject wise marks in a list: [maths, science, languages] "))
        # avg_marks = sum(marks) / len(marks)
        
        #pushing to db
        # database[rollno]['name'] = name
        # database[rollno]['marks'] = marks
        # database['rollno']['avg_marks'] = avg_marks
    print(database)


def find_student():
    pass

def add_student():
    pass

def edit_student():
    pass

def del_student():
    pass

def display_class():
    pass

def display_student():
    pass

def find_subject_topper():
    pass

def find_class_topper():
    pass

def find_subject_average():
    pass

def find_class_average():
    pass

## INPUTS ##

## _main_ ##
get_data()
while True:
    print("\tL I S T   O F   O P E R A T I O N S\t")
    print("1. Add student to record")
    print("2. Edit student record")
    print("3. Delete student record")
    print("4. Display class record")
    print("5. Display student record")
    print("6. Find subject-wise toppers")
    print("7. Find overall class topper")
    print("8. Find subject-wise averages")
    print("9. Find class average")
    print("10. To quit")
    print("----------------------------------")
    
    choice = int(input("Enter the operation you wish to perform: "))

    if choice == 10:
        break
    elif choice == 1:
        add_student()
    elif choice == 2:
        edit_student()
    elif choice == 3:
        del_student()
    elif choice == 4:
        display_class()
    elif choice == 5:
        display_student()
    elif choice == 6:
        find_subject_topper()
    elif choice == 7:
        find_class_topper()
    elif choice == 8:
        find_subject_average()
    elif choice == 9:
        find_class_average()
    else:
        print("Invalid input! Operation does not exist")
        print("Press any key to continue.....")