from time import sleep
from requests import get
from datetime import datetime
import sys
import os

#Utils.py For Freezing
from requests import get
from notifypy import Notify

#function to check if user is online
def checkIfOnline(response):
    if '"IsOnline":true' in response.text:
        return True
    elif '"IsOnline":false' in response.text:
        return False
    else:
        return 'Error'

#function to check when user was last online
def whenLastOnline(response):
    return response.text[71:81] + '|' +  response.text[82:90]

#function to get UserId from a username using roblox api
def getUserID(userName):
    
    #Send username to get userID
    response = get('https://api.roproxy.com/users/get-by-username?Username=' + userName)

    #Trim to get only userID
    startPos = response.text.find(':') + 1
    endPos = response.text.find(',')

    #Return User ID
    return response.text[startPos:endPos]

#Notify User that Target is online
def notifyUser(userName):
    notif = Notify()
    notif.title = 'RobloTrack'
    notif.message = userName + ' is Online!'
    notif.icon = icon
    notif.send()







#Pyinstaller stuff
def resource_path(relative_path):
    absolute_path = os.path.abspath(__file__)
    root_path = os.path.dirname(absolute_path)
    base_path = getattr(sys, '_MEIPASS', root_path)
    return os.path.join(base_path, relative_path)



#Define Icon.png path
icon = resource_path('icon.png')





#Main.py

#Get User ID
userName = input('Username of Target: ')

userID = getUserID(userName)


#Generate URL
URL = 'https://api.roproxy.com/users/' + userID + '/onlinestatus'


#Get Roblox Info
response = get(URL)




#Inital check of if Target is Online
if checkIfOnline(response):
    print('Target Online')
    

    #If User is Offline record it
if checkIfOnline(response) == False:
    print('Target Offline')
    
    #Print Last Online Time
    print('Last Online At:', whenLastOnline(response), 'EST')


#Main Loop
while True:

    #Wait 1 min
    sleep(60.0)

    #Get Roblox Info
    response = get(URL)

    #Create Timestamp
    time = datetime.today()

    #Check if User is Online and if so Record It
    if checkIfOnline(response):

        #If the time is 2 characters long print it normally
        if len(str(time.minute)) == 2:
            print('Target Online as Of', str(time.hour) + ':' + str(time.minute), 'EST')
        #If the time is 1 character long print it with a zero
        else:
            print('Target Online as Of', str(time.hour) + ':0' + str(time.minute), 'EST')

        #Notify User that player is online
        notifyUser(userName)
        
    #If User is Offline record it
    if checkIfOnline(response) == False:
        
         #If the time is 2 characters long print it normally
        if len(str(time.minute)) == 2:
            print('Target Offline as Of', str(time.hour) + ':' + str(time.minute), 'EST')
        
        #If the time is 1 character long print it with a zero
        else:
            print('Target Offline as Of', str(time.hour) + ':0' + str(time.minute), 'EST')