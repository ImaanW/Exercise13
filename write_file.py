#Question1
with open ('pelican.txt','w') as f:
    pass
file_object = open('pelican2.txt', 'w')
file_object.write("A wonderful bird is the pelican.\n")
file_object.write("His bill holds more than his belican.\n")


lines = ["He can take in his beak,\n","Enough food for a week,\n","But I’m damned if I see how the helican.\n"]
file_object.writelines(lines)
#the \n is needed to make the sentence into seperate lines instead of one single line.

file_object.close()
