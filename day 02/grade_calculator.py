# Grade Calculator Script

def get_mark(subject_num):
    """Get a valid mark for a subject (0-100)"""
    while True:
        try:
            mark = float(input(f"Enter mark for subject {subject_num}: "))
            if mark < 0:
                print("Invalid input. Marks cannot be negative. Please try again.")
                continue
            if mark > 100:
                print("Invalid input. Marks cannot be greater than 100. Please try again.")
                continue
            break
        except ValueError:
            print("Invalid input. Please enter a valid number.")
    return mark

while True:
    # Get student name
    name = input("Enter student's name: ")
    
    # Get 3 subject marks
    mark1 = get_mark(1)
    mark2 = get_mark(2)
    mark3 = get_mark(3)
    
    # Calculate average
    average = (mark1 + mark2 + mark3) / 3
    
    # Assign grade based on average
    if average >= 75:
        grade = "A"
    elif average >= 60:
        grade = "B"
    elif average >= 40:
        grade = "C"
    else:
        grade = "Fail"
    
    # Display result
    print("------------------------------")
    print(f"Name  : {name}")
    print(f"Average: {average:.2f}")
    print(f"Grade : {grade}")
    print("------------------------------")
    
    # Ask to continue or exit
    continue_choice = input("\nEnter another student or type 'Exit' to quit: ").strip()
    if continue_choice.lower() == "exit":
        print("Program ended. Goodbye!")
        break
    print()
