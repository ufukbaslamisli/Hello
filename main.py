#print("hello world")

# Students list - stores [Name, Email, Major] for each student 

students_list = [["Alice.Johnson","alicejohnson@university.edu","CS"], ["Bob.Smith","bobsimith@university.edu","Math"]] 

def display_student(student): 

    print(f"Name: {student[0]}") 
    print(f"Email: {student[1]}") 
    print(f"Major: {student[2]}") 
    print("-" * 40) 

def add_student(): 

    # Ask for name, email, and major 
    # Create a list with the student info 
    # Add it to students_list 
    # Print a confirmation message 
    
    Name = input("Please enter the name of the student ")
    Email =input("Please enter the email adress ")
    Major =input("Please enter the major ")
    student = [Name, Email, Major]
    students_list.append(student)
    print("New Student informations are added to the list")
    return student

def remove_student(): 

    # TODO: Ask for name to remove 

    # TODO: Search for the student 

    # TODO: Ask for confirmation 

    # TODO: Remove if confirmed 

    pass  # Replace with your code 

def search_students(): 

    # TODO: Ask if viewing all or searching 

    # TODO: Display results 

    pass  # Replace with your code 

def update_student(): 

    # TODO: Ask for name to update 

    # TODO: Find the student 

    # TODO: Show current info and ask what to update 

    # TODO: Get new value and update 

    pass  # Replace with your code 

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

    # TODO: Add remaining cases