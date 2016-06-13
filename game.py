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
playerList=['player0','player1','player2','player3']
hiddenForm=htmlFunctions.element(False,1,"input",'type="hidden" name="sessID" value="'+sessID+'"','')

print htmlFunctions.htmlSetup()
print htmlFunctions.headSetup('Payday',"")
for player in playerList:
    if sessionData[sessID][player]=="":
        output="Name "+player+" and give them a class <br>"+htmlFunctions.element(True,0,'form','action="game.py" method="POST"',
        "Name: "+htmlFunctions.element(False,1,'input','name='+player,"")+ hiddenForm+'<br>' +
        htmlFunctions.element(False,1,'input','type=submit',"")
        )
print htmlFunctions.bodySetup(output)
print htmlFunctions.html_end()