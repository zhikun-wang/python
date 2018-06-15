from sys import argv
script = argv
filename = raw_input("create filename:")
print ("We'are going to erase %r" % filename)
target  = open(filename,'w')
target.truncate()
print("Now input new txt for file %r" % filename)
line1 = raw_input("line 1 :")
line2 = raw_input("line 2 :")
line3 = raw_input('line 3 :')

target.writelines(line1)
target.writelines('\n')
target.write(line2)
target.write("\n")
target.writelines(line3)
target.close()