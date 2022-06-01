#file_object = open('pelican2.txt','r+')
#print(file_object.read())


#lines = open('/Users/getintotech/PycharmProjects/Exercise13/pelican2.txt').readlines()
print(lines,end ="")


print(len(lines))

for line in open('pelican2.txt') :
    print(line, end = "")
    #one line at atime