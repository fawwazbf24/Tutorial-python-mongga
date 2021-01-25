#file handling

file=open("C:\\Users\\fawwa\\OneDrive\\Desktop\\file\\example1.txt", "r")
#print(dir(f))
#print(f.read())
#f.seek(0)
#print(f.read())
#f.seek(1)
#print(f.read())

#a=file.readlines()
#file.seek(0)
#print(file.readline())
#print(file.readline())

#for f in a:
#    print(f)

print("a")
print("b")

for f in file:
    print(f,end="")

file.close()

file1=open("C:\\Users\\fawwa\\OneDrive\\Desktop\\file\\contohappend.txt", "a")
file1.write("testing")
file2=open("C:\\Users\\fawwa\\OneDrive\\Desktop\\file\\contohwrite.txt.txt", "w")
file2.write("testing2")

file2.writelines(("nama saya fawwaz ", "saya suka main PC"))

file1.close()
file2.close()