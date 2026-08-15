#print("hello world")

# Students list - stores [Name, Email, Major] for each student 

students_list = [["Alice.Johnson","alicejohnson@university.edu","CS"], ["Bob.Smith","bobsimith@university.edu","Math"]] 

def display_student(student): 

    print(f"Name: {student[0]}") 
    print(f"Email: {student[1]}") 
    print(f"Major: {student[2]}") 
    print("-" * 40) 

def add_student(): 
    
    Name = input("Please enter the name of the student ")
    Email =input("Please enter the email adress ")
    Major =input("Please enter the major ")
    student = [Name, Email, Major]
    students_list.append(student)
    print("New Student informations are added to the list ")
    return student

def remove_student(): 

    Name = input("Please enter the name of the student ")
    NameFound=False
    for student in students_list:
        if Name==student[0]:
            NameFound=True
            confirmation=input("Are you sure Y/N ")
            if (confirmation=="y" or confirmation=="Y"):
                students_list.remove(student)
                print("Student " + Name + " removed")
            else:
                print("Operation cancelled")
    if NameFound==False:  
       print("There is no such student in students list")

def search_students(): 
    NameFound=False
    search_criteria=input("Do you want see all students and Information Y/N")
    if (search_criteria=="Y" or search_criteria=="y"):
        for student in students_list:
            display_student(student)
    else:
        Name=input("Please enter the name to see the informations ")
        for student in students_list:
            if Name==student[0]:
                display_student(student)
                NameFound=True
        if NameFound==False:  
           print("There is no such student in students list")

 

def update_student(): 
    NameFound=False
    
    Name=input("\nWhich person would you like to update")
    for student in students_list:
        if Name==student[0]:
           NameFound=True
           display_student(student)
           criteria=input("Would you like to update the name Y/N")
           if (criteria=="Y" or criteria=="y"):
                    student[0]=input("Please enter the new Name ")
           criteria=input("Would you like to update the email adress Y/N")  
           if (criteria=="Y" or criteria=="y"):
                     student[1]=input("Please enter the new Email ")
           criteria=input("Would you like to update the major Y/N")  
           if (criteria=="Y" or criteria=="y"):
                     student[2]=input("Please enter the new major ")
           display_student(student)
    if NameFound==False:  
        print("There is no such student in students list")
    
# Main program 

while True: 

    print("\n=== Student Rostering System ===") 

    print("1. Add Student") 

    print("2. Remove Student") 

    print("3. Search Students") 

    print("4. Update Student") 

    print("5. Exit") 

    choice = input("Enter your choice (1-5): ") 

    if choice == "1": 

        student=add_student() 

        display_student(student)

    elif choice == "2": 

        remove_student()

    elif choice == "3": 
        
      search_students()

    elif choice == "4":

      update_student()

    else:

       print("Program terminated.")
       break
   