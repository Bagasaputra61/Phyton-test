#reading files
example_file = open("Detective name.txt", "r")
for Employee in example_file.readlines():
    print(Employee)
    
example_file.close()
