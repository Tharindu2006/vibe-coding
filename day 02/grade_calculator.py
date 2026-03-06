# Grade Calculator Script
while True:
    # Get student name
    name = input("Enter student's name: ")
    
    # Get 3 subject marks
    mark1 = float(input("Enter mark for subject 1: "))
    mark2 = float(input("Enter mark for subject 2: "))
    mark3 = float(input("Enter mark for subject 3: "))
    
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
