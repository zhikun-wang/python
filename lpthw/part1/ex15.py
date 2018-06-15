from sys import argv
script,filename = argv
txt = open(filename)
print("Here is your file %r" % filename)
print(txt.read())

file_again = raw_input("input file name:")
txt_again = open(file_again)
print(txt_again.read())