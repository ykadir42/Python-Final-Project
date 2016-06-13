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

sessionData=csvToDict.csvToDict('sessions.csv')
playerList=['0','1','2','3']
sessID=fromClient['sessID'].value
hiddenForm=htmlFunctions.element(False,1,"input",'type="hidden" name="sessID" value="'+sessID+'"','')
player=sessionData[sessID]['player']
def nextPlayer():
    if player == 3:
        return 0
    else:
        return player+1
def value(key):
    return sessionData[sessID][key]
def printKeys():
    outputKeys=''
    for key in sessionData[sessID]:
        if key != 'password':
            outputKeys+=str(key)+": "+str(value(key))+'<br>'
    return outputKeys
def changeValue(key,value):
    sessionData[sessID][key]=value
# def generateChoices(player):
#     choices=''
#     def addChoice(choice,text):
#         choices+=htmlFunctions.element(False,1,"input",'type="radio" name="'+player+'choice" value="'+choice+'"',text)
#     location=value(player+'Loc')
#     if location = "van":
#         addChoice(''
#     return htmlFunctions.element(True,2,"form",'action="game.py" method="POST"',choices)
for key in fromClient:
    if key != 'sessID':
        sessionData[sessID][key]=fromClient[key].value
dictToCsv.dictToCsv(sessionData)
print htmlFunctions.htmlSetup()
print htmlFunctions.headSetup('Payday',"")
if sessionData[sessID]['player'+str(player)]=="":
    output="Name "+"player"+str(player)+" and give them a class <br>"+htmlFunctions.element(True,0,'form','action="game.py" method="POST"',
    "Name: "+htmlFunctions.element(False,1,'input','name='+"player"+str(player),"")+ hiddenForm+'<br>' +
    '''<input type="radio" name="'''+str(player)+'''Class" value="technician"> Technician: Explosives,
Silent Drill,
Sentry Gun<br>
	<input type="radio" name="'''+str(player)+'''Class" value="enforcer"> Enforcer: Ammo Bag,
Silent Saw,
Increased health <br>
    <input type="radio" name="'''+str(player)+'''Class" value="mastermind"> Mastermind: Health Kit,
Intimidation,
Revive in 1 turn<br>
    <input type="radio" name="'''+str(player)+'''Class" value="ghost"> Ghost: EMC Jammer,
Silenced Weapon,
Lockpick without drill<br>'''+
    htmlFunctions.element(False,1,'input','type="submit"',"")
    )
    changeValue('player',nextPlayer())
elif sessionData[sessID]['initiated']==False:
    for player in playerList:
        if player+"Class"=="enforcer":
            changeValue(player+"Health",6)
        else:
            changeValue(player+'Health',3)
        changeValue(player+'Ammo',6)
        changeValue(player+'Downs',0)
        changeValue(player+'Location','van')
    changeValue('vaultProgress',10)
    changeValue('managerProgress',5)
    changeValue('corridorProgress',5)
    changeValue('alert',False)
    changeValue('points',0)
    changeValue('gateProgress',5)
    changeValue('choices',True)
    changeValue('initiated',True)
    output='Initalized <form action="game.py" method="POST">' +hiddenForm+htmlFunctions.element(False,1,'input','type="submit" value="Continue"',"")+"</form>"
else:
    output="<h1>That is it for this free trial.</h1><br> <p>The customization and data saving parts of this project ended up taking such an enormous amount of time that the gameplay didn't come into play. The data saving is the main thing about this project, if you leave now and log back in, you will be on this page again, with your data intact.</p> <p>Here is your data for this game:</p><br>"+ '<ul>' + printKeys() +'</ul>'
    # if value('choices'):
    #     output=htmlFunctions.element(True,0,'div', 'style="height:50%"',
    #         htmlFunctions.element(True,1,'div', 'style="width:50%;float:left"',
    #         generateChoices('0')
    #         )+
    #         htmlFunctions.element(True,1,'div', 'style="width:50%;float:right"',
    #         generateChoices('1')
    #         )
    #     )+htmlFunctions.element(True,0,'div', 'style="height:50%"',
    #         htmlFunctions.element(True,1,'div', 'style="width:50%;float:left"',
    #         generateChoices('2')
    #         )+
    #         htmlFunctions.element(True,1,'div', 'style="width:50%;float:right"',
    #         generateChoices('3')
    #         )
    #     )
print htmlFunctions.bodySetup(output)
print htmlFunctions.html_end()
dictToCsv.dictToCsv(sessionData)