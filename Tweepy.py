from tweepy import API
from tweepy import Cursor
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
from selenium.webdriver.common.keys import Keys
import time
from datetime import date
from io import BytesIO
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import ui
from bs4 import BeautifulSoup as BS
from selenium.webdriver.chrome.options import Options
#this is where i put my CONSUMER_KEY etc.
import keys

def divide(content):
    a=0
    x=0
    twitter_client=TwitterClient()
    api=twitter_client.get_twitter_client_api()
    list=[]
    
    while(a<=len(content)):
        
        icerik=""
        for x in range(x,x+277):
            if(x<len(content)):
                icerik=icerik+content[x]
        a=x
        
        list.append(icerik)
    i=len(list)-1
    while(i>=0):
        api.update_status(list[i])
        i=i-1


                
      

# # # # # TWITTER AUTHENTICATE # # # # #
class TwitterAuthenticator():
    def authenticate_twitter_app(self):
        auth=OAuthHandler(keys.CONSUMER_KEY,keys.CONSUMER_SECRET)
        auth.set_access_token(keys.ACCESS_TOKEN,keys.ACCESS_TOKEN_SECRET)
        return auth



class TwitterClient():
    def __init__(self,twitter_user=None):
        self.auth=TwitterAuthenticator().authenticate_twitter_app()
        self.twitter_client=API(self.auth)
        self.twitter_user=twitter_user

    def get_twitter_client_api(self):
        return self.twitter_client

    # How many tweets we want to accualy share how many tweets we want to extract
    def get_user_timeline_tweets(self,num_tweets):
        tweets=[]
        for tweet in Cursor(self.twitter_client.user_timeline, id=self.twitter_user).items(num_tweets):
            tweets.append(tweet)
        return tweets


    def get_friend_list(self, num_friends):
        friend_list=[]
        for friend in Cursor(self.twitter_client.friends, id=self.twitter_user).items(num_friends):
            friend_list.append(friend)
        return friend_list

    
    def get_home_timeline_tweets(self, num_tweets):
        home_timeline_tweets=[]
        for tweet in Cursor(self.twitter_client.home_timeline_tweets, id=self.twitter_user).items(num_tweets):
            home_timeline_tweets.append(tweet)
        return home_timeline_tweets

class Screenshot():
    def __init__(self):
        o = Options()
        o.add_argument('--headless')
        o.add_argument('--no-sandbox')
        o.add_argument('--disable-dev-shm-usage')
        
       
        self.browser = webdriver.Chrome("./chromedriver",chrome_options=o)
   
    
    

    def tweetatma(icerik1,icerik2):
        
        twitter_client=TwitterClient()
        api=twitter_client.get_twitter_client_api()
        api.update_status(icerik1)
        time.sleep(2)
        api.update_status(icerik2)
        
    def Screenshot(self):

        url="https://covid19.saglik.gov.tr/"
        self.browser.get(url)    

        
        soup = BS(self.browser.page_source, 'html.parser').find("div", {"class":"data_list"}).text.replace("\n","")
 
        self.browser.quit()
        time.sleep(1)
        return(divide(soup))

       





       

if __name__=="__main__":

    
    
    
    screensht=Screenshot()
    screensht.Screenshot()
    
    
    

    #api.update_status("hello_world")
    # api.update_status(status=screensht.Screenshot())
