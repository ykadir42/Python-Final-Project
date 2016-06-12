def dictToCsv(dictionary):
    dest=open('sessions.csv',"w",0)
    titlesList=dictionary['titles']
    for title in titlesList:
        dest.write(title)
        if titlesList.index(title)<len(titlesList)-1:
            dest.write(",")
    for sessID in dictionary:
        if sessID != 'titles':
            dest.write("\n"+str(sessID))
            for title in titlesList:
                if title != 'sessID':
                    dest.write(","+str(dictionary[sessID][title]))

if __name__=="__main__":
    import csvToDict
    # print csvToDict.csvToDict("sessions.csv")
    dictToCsv(csvToDict.csvToDict("sessions.csv"))