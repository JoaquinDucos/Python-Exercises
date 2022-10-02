# files are important in making softwares
# you can store your application data locally
# or application state locally
# first lets create a file
# python has open("file name", "operation") method for working with files
#   writing
# we pass the w parameter, if the file doesnt exist it will create
# deletes all the data in the file if it exists and then writes to it
import os


def read_file(file_name):
    file = open(file_name, "r")
    print("file contents: \n"+file.read())
    file.close()


file = open("file.txt", "w")
file.write("Every thing was cool until you showed up")
file.close()
# reading the file in the read mode
file = open("file.txt", "r")
print("file contents: \n"+file.read())
file.close()
# adding data to the end of the file
file = open("file.txt", "a")
file.write(" but now its better")
file.close()
# lets read the file again
read_file("file.txt")
# deleting a file
# make sure the file exists
# os.remove("file.txt")

#error handing 
"""
def read_file(file_name):
    try:

        file = open(file_name, "r")
        print("file contents: \n"+file.read())
        file.close()
    except :
        print("Something went wrong with reading file")    """

#Another example
"""
if len(password)<10 :
    raise Exception ("The password must be greater than 10 digits!")  
    """     

