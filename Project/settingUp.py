# open the input file (finalpt1.txt)
with open("finalp1.txt", "r") as file:
    # read content of the file
    content = file.readlines()

# remove all comments, blank lines, and clean up spaces 
new_content = []
prevLine=""
addedLine=""
addLineFlag = True

#iterate through the string
for line in content:
    addedLine=line
    addLineFlag = True

    # remove all the comments in the form; //comment, //comment//, and block comments. *can't have aspace after*
    if addedLine.endswith("//\n") and prevLine.startswith("//"):
        addLineFlag = False
        continue
    elif "//" in addedLine:
       addedLine = addedLine[:addedLine.index("//")]
       
    # remove all the blank lines
    if addedLine.strip() == "":
        prevLine = line
        addLineFlag = False
        continue
    
    # clean up all the spaces
    addedLine = " ".join(addedLine.split())
    
    # append the modified line to the new content
    if addLineFlag is True:
        new_content.append(addedLine)
    
    prevLine=line
    
# open the output file
with open("finalp2.txt", "w") as file:
    # write modified content to the output file
    file.write("\n".join(new_content))