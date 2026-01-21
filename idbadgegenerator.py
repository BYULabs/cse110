print("Please enter the following information")
print("")

first_name = input("First Name: ")
last_name = input("Last Name: ")
email_address = input("Email Address: ")
phone_number = input("Phone Number: ")
job_title = input("Job Title: ")
id_number = input("ID Number: ")

print("")
print("The ID Card is:")
print("----------------------------------------")
# Capitalize last name
print(last_name.upper() + ", " + first_name)
# Title case job title
print(job_title.title())
# ID format 12-3456
id_number = id_number[:2] + "-" + id_number[2:]
print("ID: " + id_number)
print()
print(email_address)
# Phone number format (123) 456-7890
phone_number = "(" + phone_number[:3] + ") " + phone_number[3:6] + "-" + phone_number[6:]
print(phone_number)
print("----------------------------------------")
