#Step 1: Plan the Data Storage
employee_data = {
    101: {'name': 'Vinay', 'age': 20, 'department': 'IT', 'salary': 65000},
    102: {'name': 'Vastav', 'age': 23, 'department': 'IT', 'salary': 95000},
    103: {'name': 'Kavita', 'age': 32, 'department': 'Finance', 'salary': 65000},
    104: {'name': 'Arshia', 'age':25, 'department': 'HR', 'salary': 55000}
}

#Step 2: Define the Menu System
def main_menu():
    while True:
        print("\nEmployee Management System")
        print("1. Add Employee")
        print("2. View All Employees")
        print("3. Search for Employee")
        print("4. Exit")    
        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            add_employee()
        elif choice == '2':
            view_employees()
        elif choice == '3':
            search_employee()
        elif choice == '4':     #Step 6: Exit the Program
            print("Thank you!")
            break
        else:
            print("Invalid choice. Please enter correct data.")

#Step 3: Add Employee Functionality
def add_employee():
    try:
        emp_id = int(input("Enter Employee ID: "))
        if emp_id in employee_data:
            print("Employee ID already exists. Please enter a unique ID.")
            return
        
        name = input("Enter Employee Name: ")
        age = int(input("Enter Employee Age: "))
        department = input("Enter Employee Department: ")
        salary = float(input("Enter Employee Salary: "))

        employee_data[emp_id] = {
            'name': name,
            'age': age,
            'department': department,
            'salary': salary
        }
        print(f"Employee {name} added successfully!")
    except ValueError: 
        #If non-numeric then asks to retry with valid input.
        print("Invalid input. Please try again.")

#Step 4: View All Employees
def view_employees():
    if not employee_data:
        print("No employees available.")
        return

    print("\nEmployee Details:")
    print(f"{'ID':<10}{'Name':<20}{'Age':<10}{'Department':<15}{'Salary':<10}") #Proper Formatting
    print("-" * 65)
    for emp_id, details in employee_data.items():
        print(f"{emp_id:<10}{details['name']:<20}{details['age']:<10}{details['department']:<15}{details['salary']:<10.2f}")

#Step 5: Search for an Employee by ID
def search_employee():
    try:
        emp_id = int(input("Enter Employee ID to search: "))
        if emp_id in employee_data:
            details = employee_data[emp_id]
            print("\nEmployee Found:")
            print(f"Name: {details['name']}")
            print(f"Age: {details['age']}")
            print(f"Department: {details['department']}")
            print(f"Salary: {details['salary']:.2f}")
        else:
            print("Employee not found.")
    except ValueError:
        print("Invalid input. Please try again.")



#Program execution
if __name__ == "__main__":
    main_menu()
