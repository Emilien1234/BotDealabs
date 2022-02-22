
import requests
import time
from bs4 import BeautifulSoup
import datetime
from requests_html import HTMLSession
from datetime import datetime


chanelBotLog = "https://discord.com/api/v9/channels/****************/messages"
chanelEDP = "https://discord.com/api/v9/channels/************/messages"

message = {'content':"test2 @everyone"}

tokenEmilien = {'authorization': '**********************************'}
tokenBotDiscord = {'authorization': '***************************************'}

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36"}

loadTemp = 30;
itemRef = ""

def waitUntilMessage():
    global itemRef
    try:
        session = HTMLSession()
        r = session.get('https://www.dealabs.com/discussions/le-topic-des-erreurs-de-prix-1056379?by=sorting_newest_first#thread-comments')
        print("Get info >> getstates : ",r)
        
          
        r.html.render(scrolldown=2,wait=5,reload=True,sleep=2) 
    
        itemList = r.html.find('.commentList--anchored') # ol
        
        try:
            linkItemList = itemList[0].find('a')[0].attrs['href']        
            textItemList = itemList[0].find('.userHtml')[0].text
        except:
            print("Get error >> decode ?")
            
            print("Get info >> ",textItemList )
        try:      
            if itemRef != textItemList:
                message ={'content':" @everyone " + textItemList + " " + linkItemList }
                
                requests.post(chanelEDP,data=message,headers=tokenBotDiscord)
                itemRef = textItemList
        except:
            print("Get error >> post discord")
        
        try:
                print("Post Discord EDP ",datetime.now(),textItemList )
                with open('log.txt', 'w') as f:
                    f.write(str(datetime.now())  + str(r) + str(textItemList) + "\r\n")
        
        except :
            print("Get error >> Wirte File")
     
        try:
            session.close()
        except:
            print("Get error >> close session")
    except:
        print("error script") 
        
        with open('log.txt', 'w') as f:
            f.write(str(datetime.now()) + " error : "  + str(r) + "\r\n")
   
		#        print("Post Discord error" )
		#        message ={'content':" @everyone " + textItemList +  linkItemList }
		#        requests.post(chanelBotLog,data=message,headers=tokenBotDiscord)
            

if __name__ == "__main__":

    while 1 == 1:
      try:
         waitUntilMessage()
      except:
          print("error run")
      time.sleep(loadTemp)

    
