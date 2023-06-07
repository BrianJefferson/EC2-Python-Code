import random
import string

DEPARTMENTS_WITH_ACCESS = ["Marketing", "Accounting", "Finops"]

def generate_ec2_names(num_ec2instances, department_name):
    ec2_names = []
    
    for _ in range(num_ec2instances):
        random_chars = ''.join(random.choices(string.ascii_uppercase + string.digits, k=5))
        ec2_name = f"{department_name}-{random_chars}"  # Generate EC2 name by combining department name and random characters
        ec2_names.append(ec2_name)  # Add the generated name to the list of EC2 names
    
    return ec2_names

def main():
    num_ec2instances = int(input("How many EC2 instances do you want names for?: "))  # Prompt the user to enter the number of EC2 instances
    department_name = input("What is the name of your department?: ")  # Prompt the user to enter the department name
    
    department_name = department_name.lower().capitalize()  # Convert the department name to lowercase and capitalize the first letter
    
    if department_name in DEPARTMENTS_WITH_ACCESS:  # Check if the department name is in the list of departments with access
        ec2_names = generate_ec2_names(num_ec2instances, department_name)  # Generate EC2 names based on the given number of instances and department name
        
        print("Generated EC2 names:")
        for name in ec2_names:
            print(name)  # Print each generated EC2 name
    else:
        print("That department can not use this Name Generator. Please choose from the following departments:")
        print(", ".join(DEPARTMENTS_WITH_ACCESS))  # Print the list of departments with access

if __name__ == "__main__":
    main()  # Call the main function if the script is run directly
