#! /usr/bin/python

import cgitb
cgitb.enable()

import cgi
fromClient = cgi.FieldStorage()

import htmlFunctions
import csvToDict
import addAccount

print 'content-type: text/html\n'

passwordDict=csvToDict.csvToDict('sessions.csv')
sessID = fromClient["sessID"].value
password = fromClient["password"].value

if "login" in fromClient:
    if sessID in passwordDict:
        if password==passwordDict[sessID]['password']:
            output=""
            redirect='<meta http-equiv="refresh" content="1; url=http://lisa.stuy.edu/~jawadul.kadir/project/game.py" >'
        else:
            output='Login Failed'
            redirect='<meta http-equiv="refresh" content="3; url=http://lisa.stuy.edu/~jawadul.kadir/project/login.html" >'
    else:
        output='Login Failed'
        redirect='<meta http-equiv="refresh" content="3; url=http://lisa.stuy.edu/~jawadul.kadir/project/login.html" >'
else:
    if sessID in passwordDict:
        output="Session Name already taken!"
        redirect='<meta http-equiv="refresh" content="3; url=http://lisa.stuy.edu/~jawadul.kadir/project/login.html" >'
    else:
        if "," in sessID or "\n" in sessID or "," in password or "\n" in password:
            output='Session name or password may not contain commas or newlines. <br><a href="http://lisa.stuy.edu/~jawadul.kadir/project/login.html">Go back</a>'
            redirect=''
        else:
            addAccount.addAccount(sessID,password)
            output="Registered!"
            redirect='<meta http-equiv="refresh" content="3; url=http://lisa.stuy.edu/~jawadul.kadir/project/login.html" >'

print htmlFunctions.htmlSetup()
print htmlFunctions.headSetup("Verifying...", redirect)
print htmlFunctions.element( True, 0, 'body', 'style="background-color:black;"', htmlFunctions.element( False, 1, 'h1', 'style="color:white;"', output))
print htmlFunctions.html_end()
