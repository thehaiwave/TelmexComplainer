import os
import sys
import speedtest

def test():
    speedResult = speedtest.Speedtest()
    speedResult.get_servers()
    speedResult.get_best_server()
    return speedResult.download()


def main():
    downloadSpeed = test()


if __name__ == "__main__":
    main()
    print("Finalizado")