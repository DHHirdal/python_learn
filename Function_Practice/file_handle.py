# This is file operation program - file handling is an important concept in the live projects.
# python has several functions like create a file, open/read/write/update and deleting files.
import os

os.remove("myfile.txt") # this line of code deleting "myfile.txt" file from the directory and executing 
f= open("python_excercise.txt")
print(f.read())
f.close()

x= open("myfile.txt", "x")
x.write("I created new file")
x.close()
with open ("myfile.txt","r") as y:
    print(y.read())
    y.close()
x= open("myfile.txt", "w")
x.write("I am overwriting the file\n"
"this is tried for new line addition\n"
"3rd line aslo added to the file")
x.close()

print("content after the new write")
with open ("myfile.txt","r") as y:
    print(y.read())
    y.close()


