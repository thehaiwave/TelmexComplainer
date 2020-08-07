import os
import sys
import speedtest
import json

def main():
    print("Iniciando")
    botInstance = ManageBot()
    botInstance.run()


class DownloadSpeedTest():
    def __init__(self):
        self.config = json.load(open('./config.json'))

    def test(self):
        speedResult = speedtest.Speedtest()
        speedResult.get_servers()
        speedResult.get_best_server()
        return speedResult.upload()


class ManageBot():
    def __init__(self):
        self.config = json.load(open('./config.json'))
        
    def run(self):
        botSpeedTest = DownloadSpeedTest()
        speedResults = botSpeedTest.test()
        self.speedAssessment(speedResults)
    
    def speedAssessment(self, speedResults):
        speedResults = (speedResults/1024)/1024
        speedThreshold = self.config['internetSpeedThreshold']



if __name__ == "__main__":
    main()
    print("Finalizado")