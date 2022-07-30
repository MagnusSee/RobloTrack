from time import sleep
from requests import get
import utils
from datetime import datetime


#Get User ID
userName = input('Username of Target: ')

userID = utils.getUserID(userName)


#Generate URL
URL = 'https://api.roproxy.com/users/' + userID + '/onlinestatus'


#Get Roblox Info
response = get(URL)




#Inital check of if Target is Online
if utils.checkIfOnline(response):
    print('Target Online')
    

    #If User is Offline record it
if utils.checkIfOnline(response) == False:
    print('Target Offline')
    
    #Print Last Online Time
    print('Last Online At:', utils.whenLastOnline(response), 'EST')



#Main Loop
while True:

    #Wait 1 min
    sleep(60.0)

    #Get Roblox Info
    response = get(URL)

    #Create Timestamp
    time = datetime.today()

    #Check if User is Online and if so Record It
    if utils.checkIfOnline(response):

        #If the time is 2 characters long print it normally
        if len(str(time.minute)) == 2:
            print('Target Online as Of', str(time.hour) + ':' + str(time.minute), 'EST')
        #If the time is 1 character long print it with a zero
        else:
            print('Target Online as Of', str(time.hour) + ':0' + str(time.minute), 'EST')

        #Notify User that player is online
        utils.notifyUser(userName)
        
    #If User is Offline record it
    if utils.checkIfOnline(response) == False:
        
         #If the time is 2 characters long print it normally
        if len(str(time.minute)) == 2:
            print('Target Offline as Of', str(time.hour) + ':' + str(time.minute), 'EST')
        
        #If the time is 1 character long print it with a zero
        else:
            print('Target Offline as Of', str(time.hour) + ':0' + str(time.minute), 'EST')