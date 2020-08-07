import os
import sys
import speedtest
import json
import random

def main():
    print("Iniciando")
    botInstance = ManageBot()
    botInstance.run()


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
        return speedResult.upload()

    def speedAssessment(self, speedResults):
        speedResults = (speedResults/1024)/1024
        speedThreshold = self.config['internetSpeedThreshold']

        if(speedResults < (speedThreshold*40)/100):
            return "bad"

        elif(speedResults < (speedThreshold*50)/100):
            return "horrible"

    def makeTweet(self, speedTestResult):
        speedStatus = self.speedAssessment(speedTestResult)
        speedTestResult = round((speedTestResult/1024)/1024)

        try:
            message = self.config["tweetSelection"][speedStatus][random.randint(0,1)].replace('{speedTestResults}', str(speedTestResult)).replace('{atISP}', self.config["atISP"])
            print(message)
        except:
            print("Not valid")


if __name__ == "__main__":
    main()
    print("Finalizado")