This project sends a tweet everday, which contains data about covid 19

My application will send out tweets. It will be a twitter bot that tweets about the daily positive patients in Turkey. If you are interested in this project I can do for your country too of course. I will take data from our government web page which is “https://covid19.saglik.gov.tr/” and tweet it.

For running python Tweepy.py:
$python Tweepy.py

But for running in linux container :

for build the container
$docker build -t bot .

for run running the container
$docker run -ti bot# TwitterBotForCovid19


#This project for linux container
