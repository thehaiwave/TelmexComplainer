import os
import sys
import speedtest
import json
import random
import twitter
import time
from datetime import datetime, timedelta

def main():

    botInstance = ManageBot()

    while True:
        try:
            botInstance.run()
            dt = datetime.now() + timedelta(hours=1)
            dt = dt.replace(minute=10)
            
            while datetime.now() < dt:
                time.sleep(1)

        except:
            sys.exit(1)
            
class ManageBot():
    def __init__(self):
        self.config = json.load(open('./config.json'))
        
    def run(self):
        speedTestResult = self.runSpeedTest()
        self.makeTweet(speedTestResult)
    
    def runSpeedTest(self):
        speedResult = speedtest.Speedtest()
        speedResult.get_servers()
        speedResult.get_best_server()
        return speedResult.download()

    def speedAssessment(self, speedResults):
        speedResults = (speedResults/1024)/1024
        speedThreshold = self.config['internetSpeedThreshold']

        if(speedResults < (speedThreshold*60)/100):
            return "bad"
        elif(speedResults < (speedThreshold*50)/100):
            return "horrible"
        else:
            return None

    def makeTweet(self, speedTestResult):
        speedStatus = self.speedAssessment(speedTestResult)
        speedTestResult = round((speedTestResult/1024)/1024)

        if speedStatus is not None:
            message = self.config["tweetSelection"][speedStatus][random.randint(0,1)].replace('{speedTestResults}', str(speedTestResult)).replace('{atISP}', self.config["atISP"]).replace('{internetSpeedThreshold}', str(self.config["internetSpeedThreshold"]))
            self.sendTweet(message)

    def sendTweet(self, message):
        api = twitter.Api(consumer_key=self.config["twitterAuth"]["twitterApiKey"],
                        consumer_secret=self.config["twitterAuth"]["twitterApiKeyScret"],
                        access_token_key=self.config["twitterAuth"]["twitterAccessToken"],
                        access_token_secret=self.config["twitterAuth"]["twitterAccessTokenSecret"])

        api.PostUpdate(message)


if __name__ == "__main__":
    main()