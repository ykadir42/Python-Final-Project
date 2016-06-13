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
sessID=fromClient['sessID'].value
hiddenForm=htmlFunctions.element(False,1,"input",'type="hidden" name="sessID" value="'+sessID+'"','')
player=sessionData[sessID]['player']
def nextPlayer():
    if player == 3:
        return 0
    else:
        return player+1
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
Infinite Cable Ties<br>
    <input type="radio" name="'''+str(player)+'''Class" value="ghost"> Ghost: EMC Jammer,
Silenced Weapon,
Lockpick without drill<br>'''+
    htmlFunctions.element(False,1,'input','type=submit',"")
    )
    sessionData[sessID]['player']=nextPlayer()
print htmlFunctions.bodySetup(output)
print htmlFunctions.html_end()
print sessionData
dictToCsv.dictToCsv(sessionData)