import csvToDict

dataDict=csvToDict.csvToDict('sessions.csv')

def addAccount(sessID,password):
    dest=open('sessions.csv','a',0)
    dest.write("\n"+sessID+","+password+",0,"*(len(dataDict['titles'])-3))
    dest.close
