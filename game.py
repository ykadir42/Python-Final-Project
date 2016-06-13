#! /usr/bin/python

import cgitb
cgitb.enable()

import cgi
fromClient = cgi.FieldStorage()

import htmlFunctions
import csvToDict
import dictToCsv
import addAccount

print 'content-type: text/html\n'

# sessionData=csvToDict.csvToDict('sessions.csv')
# sessID=fromClient['sessID'].value
# hiddenForm=htmlFunctions.element(False,1,"input",'type="hidden" name="sessID" value="'+sessID+'"','')
# for key in fromClient:
    # if key != 'sessID':
        # sessionData[key]=fromClient[key].value
# print htmlFunctions.htmlSetup()
# print htmlFunctions.headSetup('Payday',"")
# player=0
# while player<=3:
    # if sessionData[sessID]['player'+str(player)]=="":
        # output="Name "+"player"+str(player)+" and give them a class <br>"+htmlFunctions.element(True,0,'form','action="game.py" method="POST"',
        # "Name: "+htmlFunctions.element(False,1,'input','name='+"player"+str(player),"")+ hiddenForm+'<br>' +
        # htmlFunctions.element(False,1,'input','type=submit',"")
        # )
    # break
# print htmlFunctions.bodySetup(output)
# print htmlFunctions.html_end()
# print sessionData
# dictToCsv.dictToCsv(sessionData)

mainEntrance = "Go to CUSTOMER WAITING AREA"
customerWaitingArea = "Go to TELLER AREA, VAULT ACCESS, OFFICE AREA, ACCESS CORRIDOR, MAIN ENTRANCE"
tellerArea = "Go to VAULT ACCESS, CUSTOMER WAITING AREA"
officeArea = "Go to CUSTOMER WAITING AREA, ROOF ACCESS, "
accessCorridor = "Go to VAULT ACCESS, CUSTOMER WAITING AREA"
managersOffice = "Go to OFFICE AREA"
securityRoom = "Go to ROOF ACCESS"
roofAccess = "Go to ROOF"
vaultAccess = "Go to VAULT, CUSTOMER WAITING AREA, TELLER AREA"
vault = "Go to VAULT ACCESS"
parkingLot = "Go to BACK ENTRANCE"
staffEntrance = "Go to VAULT ACCESS, CUSTOMER WAITING AREA"
backEntrance = "Go to ROOF ACCESS, SECURITY ROOM"
roof = "Go to ROOF ACCESS"
van = "Heist complete!"

outputSetup= "'''<form> <input type= "radio" name= "location" value= "
player = 0
while player < 3:
    if 0Loc == "mainEntrance" #also, change value in csv file to mainEntrance
	    output= outputSetup + "mainEntrance> Main Entrance <br> </form>"
	elif 1Loc
	    output= outputSetup + "customerWaitingArea> Customer Waiting Area <br> </form>"
	elif 2Loc
	player += 1
	
	
    