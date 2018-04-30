## ReadWrite to File
## Date: 17 Apr 2018
## Hridin. During Python Class


file = "C:/Users/ab55981/Desktop/test.txt"
text = open(file, "r")
newtext = text.readlines()
for line in newtext:
    print line
file2 = "C:/Users/ab55981/Desktop/test2.txt"
text2 = open(file2, "w")
for line in newtext:
    text2.write(str(line))

text.close()
text2.append("By Hridin")
text2.close()

