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

    #Get
    return response.text[startPos:endPos]

#Notify User that Target is online
def notifyUser(userName):
    notif = Notify()
    notif.title = 'RobloTrack'
    notif.message = userName + ' is Online!'
    notif.icon = 'icon.png'
    notif.send()