import sys
import time

# from cls_SocketServer import SocketServer
from cls_instrument import DeviceM


def main():
    # server = SocketServer()
    device_m = DeviceM('fluke45cfg.txt')
    trg_v = 0
    ini = 0

    # while True:
    #     pass



if __name__ == "__main__":
    main()