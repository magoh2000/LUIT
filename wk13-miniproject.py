"""
EC2 Random Name Generator

Several departments share an AWS environment. You need to ensure that the EC2s are properly named and are unique so team members can easily tell who the EC2 instances belong to. Use Python to create your unique EC2 names that the users can then attach to the instances. The Python Script should:
1. All the user to input how many EC2 instances they want names for and output the same amount of unique names.
2. Allow the user to input the name of their department that is used in the unique name.
3. Generate random characters and numbers that will be included in the unique name.
4. Push your code to GitHub and include the link in your LinkedIn write up.

ADVANCED
The only departments that should use this Name Generator are the Marketing, Accounting, and FinOps Departments. List these departments as options and if a user puts another department, print a message that they should not use this Name Generator. Be sure to account for incorrect upper or lowercase letters in the correct department. Example: a user inputs accounting vs Accounting.

COMPLEX
Turn the above into a Function and execute the Function to verify it works.

"""

import random
import math
import os
import string

# Prompt the user for the number of instances they want to request.
instance_count = int(input('How many instances are you requesting? '))

# Prompt the user for the department name and convert it to lowercase for consistency.
instance_department = input('What is the department name the instance is being requested for? (the only acceptable values are Marketing, Accounting, and FinOps) ')
instance_department = str.lower(instance_department)

# Check if the provided department name is valid. If not, ask the user to provide a valid input.
if not (instance_department == 'marketing' or instance_department == 'accounting' or instance_department == 'finops'):
    instance_department = input('Please try again - Your input is not valid. What is the department name the instance is being requested for? (the only acceptable values are Marketing, Accounting, and FinOps. The program will terminate on another invalid entry.) ')
    instance_department = str.lower(instance_department)

# Generate the requested number of unique EC2 instance names.
for i in range(instance_count):
    # Generate a random string to make the EC2 instance name unique.
    characters = string.ascii_letters + string.digits
    unique = ''.join(random.choice(characters) for i in range(8))
    
    # Print the generated EC2 instance name with the department prefix.
    print(instance_department + '-' + unique)






