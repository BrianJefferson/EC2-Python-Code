import random
import string

DEPARTMENTS_WITH_ACCESS = ["Marketing", "Accounting", "Finops"]

def generate_ec2_names(num_ec2instances, department_name):
    ec2_names = []
    
    for _ in range(num_ec2instances):
        random_chars = ''.join(random.choices(string.ascii_uppercase + string.digits, k=5))
        ec2_name = f"{department_name}-{random_chars}"
        ec2_names.append(ec2_name)
    
    return ec2_names

def main():
    num_ec2instances = int(input("How many EC2 instances do you want names for?: "))
    department_name = input("What is the name of your department?: ")
    
    department_name = department_name.lower().capitalize()
    
    if department_name in DEPARTMENTS_WITH_ACCESS:
        ec2_names = generate_ec2_names(num_ec2instances, department_name)
        
        print("Generated EC2 names:")
        for name in ec2_names:
            print(name)
    else:
        print("That department can not use this Name Generator. Please choose from the following departments:")
        print(", ".join(DEPARTMENTS_WITH_ACCESS))

if __name__ == "__main__":
    main()