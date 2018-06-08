## ReadWrite to File
## Date: 17 Apr 2018
## Hridin. During Python Class

import sys


file = "C:/Users/ab55981/Desktop/test.txt"
text = open(file, "r")
newtext = text.readlines()
for line in newtext:
    print (line)
file2 = "C:/Users/ab55981/Desktop/test2.txt"
text2 = open(file2, "w")

for line in newtext:
	text2.write("sh run " + str(line).strip('\n') + "\n")
text2.write("\n")	
for line in newtext:
	text2.write("sh " + str(line).strip('\n') + " status \n")
text2.write("\n")	
for line in newtext:
	text2.write("sh mac address-table " + str(line).strip('\n') + "\n")
text2.write("\n")
for line in newtext:
	text2.write("sh arp | inc  " + str(line))

text2.write("\n\n#################\n")
text2.write("Execution \n")
text2.write("#################\n\n")
for line in newtext:
	text2.write(str(line).strip('\n') + "\n")
	text2.write("shut" + "\n\n")

text2.write("\n\n#################\n")
text2.write("After 72 Hours \n")
text2.write("#################\n\n")
for line in newtext:
	text2.write("default " + str(line).strip('\n') + "\n")

text2.write("\n")
for line in newtext:
	text2.write(str(line).strip('\n') + "\n")
	text2.write("description Available" + "\n\n")
text.close() 
text2.close()

