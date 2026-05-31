#File Access Modes.
#R
#The file is opened in read-only mode. The file pointer is present at the start. If no access mode is
#defined, the file is opened in this mode by default.

#rb
#It converts the binary file into a read-only mode. The file pointer is present at the start of the file

#r+
#It opens the file for both reading and writing. The file pointer is present at the start of the file.

#rb+
#It opens the file in binary format for reading and writing. The file pointer is present at the start of the
#file.

#W
#It only allows you to write to the file. If a file with the same name already exists, it is overwritten;
#otherwise, it is created. The file pointer is present at the start of the file.

#wb
#It opens the file so it can only be written in binary format. If the file already exists, it is overwritten;
#otherwise, it generates a new one. The file pointer is present at the start of the file.

#w+
#It opens the file for both writing and reading. It differs from r+ in that it overwrites the previous file if
#one exists, while r+ leaves the previously written file alone. If no such file exists, it creates one. The
#file pointer is present at the start of the file.

#wb+
#It opens the file in binary format for both writing and reading. The file pointer is present at the start of
#the file.

#A
#The file is opened in append mode. If there is one, the file pointer is at the end of the previously
#written file. If no file with the same name exists, it creates a new one.

#ab
#It opens the file in binary format in append mode. The pointer is at the end of the file that was
#previously written. If no file of the same name remains, it produces a new binary file.

#a+
#It opens a file for both appending and reading. If a file exists, the file pointer stays at the end of it. If
#no file with the same name exists, it produces a new one.

#ab+
#It opens a binary file for appending and reading. The file pointer is already at the file's end.





#Syntax
#File_object_Name = open (<file_name>,<access_mode>,<buffering>)