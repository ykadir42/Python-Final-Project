# print '0. csvToDict'

def boolean(string):
    if string=="True":
        return True
    elif string=="False":
        return False
    else:
        return string

def csvToDict (fileName): #Will produce a dictionary
    source = open( fileName, 'rU')
    content = source.read()
    source.close()
    listOfLines = content.split('\n')
    titles=listOfLines.pop(0).split(',')
    output={}
    for line in listOfLines:
        elementsList = line.split(',')
        pos=1
        curDict={}
        while pos<len(elementsList):
            try:
                curDict[titles[pos]]=int(elementsList[pos])
            except ValueError:
                curDict[titles[pos]]=boolean(elementsList[pos])
            pos+=1
        output[ elementsList[0]] = curDict
    output["titles"]=titles
    return output

# print csvToDict("sessions.csv")