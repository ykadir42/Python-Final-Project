import csvToDict

dataDict=csvToDict.csvToDict('sessions.csv')

def addAccount(sessID,password):
    dest=open('sessions.csv','a',0)
    dest.write("\n"+sessID+","+password+",0,False"+","*(len(dataDict['titles'])-4))
    dest.close
